#!/usr/bin/env python3
"""
browser_common.py — Shared browser connection helpers for test-plan.ui-verify.

Provides get_page() and release() used by ui_interact.py and ui_assert.py.
Centralised here so CDP connection logic is maintained in one place.
"""
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("NODE_NO_WARNINGS", "1")

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed — run: pip install playwright && playwright install chromium")
    sys.exit(1)

from paths import SKILL_DIR, TMP_DIR

def get_page():
    """Connect to the persistent browser and return (playwright, browser, page, ctx).

    Uses contexts[-1] (the login context created by ui_prepare.py, not the
    default empty CDP context at index 0) and pages[-1] (the most recently
    active page). This is consistent across all script calls.
    """
    ctx_path = TMP_DIR / "ui_context.json"
    if not ctx_path.exists():
        print("ERROR: ui_context.json not found — run ui_prepare.py first", file=sys.stderr)
        sys.exit(1)
    ctx = json.loads(ctx_path.read_text())
    cdp = ctx.get("browser_cdp")
    if not cdp:
        print("ERROR: No browser CDP endpoint — run ui_prepare.py first", file=sys.stderr)
        sys.exit(1)

    try:
        pw      = sync_playwright().start()
        browser = pw.chromium.connect_over_cdp(cdp)
    except Exception as e:
        print(f"ERROR: Cannot connect to browser ({e}) — run ui_prepare.py first", file=sys.stderr)
        sys.exit(1)

    # Always use the last context (login context) and its FIRST page.
    # contexts[0] is the default empty CDP context; login creates contexts[1+].
    # pages[0] is the original app window created during login.
    # pages[-1] would be wrong if a popup or new tab opened — those are appended
    # after pages[0]. We close any extra pages to keep the context clean.
    contexts = browser.contexts
    if contexts:
        ctx_b = contexts[-1]
        if not ctx_b.pages:
            page = ctx_b.new_page()
        else:
            page = ctx_b.pages[0]
            # Close unexpected popups / new tabs that may have opened
            for extra in ctx_b.pages[1:]:
                try:
                    extra.close()
                except Exception:
                    pass
    else:
        ctx_b = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True,
        )
        page = ctx_b.new_page()

    return pw, browser, page, ctx


def release(pw) -> None:
    """Stop playwright library. CDP browser subprocess keeps running independently."""
    pw.stop()


def do_oauth_login(page, username: str, password: str, idp: str,
                   timeout: int = 20000) -> bool:
    """Perform the OpenShift OAuth login flow: click IDP → fill credentials → wait.

    Shared by ui_prepare.py (initial login) and ui_interact.py (_relogin).
    Returns True if login succeeded, False otherwise.
    Each caller handles its own error-recovery on False.
    """
    # Click IDP selector — some clusters skip straight to the login form
    for loc in [
        page.locator(f'a:text-is("{idp}")'),
        page.locator(f'a:has-text("{idp}")'),
        page.locator(f'button:has-text("{idp}")'),
    ]:
        try:
            if loc.count() > 0:
                loc.first.click(timeout=4000)
                page.wait_for_load_state("domcontentloaded", timeout=8000)
                break
        except Exception:
            continue

    # Fill credentials
    try:
        page.locator(
            '[name="username"], #username, input[type="text"]'
        ).first.fill(username, timeout=5000)
        page.locator(
            '[name="password"], #password, input[type="password"]'
        ).first.fill(password, timeout=5000)
        page.locator(
            '[type="submit"], button:text-is("Log in"), button:text-is("Login")'
        ).first.click(timeout=5000)
    except Exception:
        return False

    # Wait for redirect away from all auth pages
    try:
        page.wait_for_function(
            "() => !window.location.href.includes('/oauth/') && "
            "!window.location.href.includes('/login') && "
            "document.body.innerText.trim().length > 50",
            timeout=timeout,
        )
    except Exception:
        pass

    final = page.url
    return not any(p in final.lower() for p in
                   ("login", "oauth/authorize", "access_denied"))
