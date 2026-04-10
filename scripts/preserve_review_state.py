#!/usr/bin/env python3
"""Save and restore cumulative review state across re-assessment cycles.

Saves before_scores and revision history to a JSON state file before
re-review, then restores them after the new review file is written.

Usage:
    python3 scripts/preserve_review_state.py save <feature_dir>
    python3 scripts/preserve_review_state.py restore <feature_dir>
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artifact_utils import read_frontmatter, update_frontmatter


def _review_path(feature_dir):
    return os.path.join(feature_dir, "TestPlanReview.md")


def _state_path(feature_dir):
    return os.path.join(feature_dir, ".review-state.json")


def _extract_revision_history(filepath):
    """Extract the ## Revision History section content from a review file."""
    with open(filepath) as f:
        content = f.read()

    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:].lstrip("\n")

    match = re.search(r"^## Revision History\s*\n(.*)", content,
                      re.MULTILINE | re.DOTALL)
    if not match:
        return ""

    section = match.group(1)

    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading:
        section = section[:next_heading.start()]

    return section.strip()


def save(feature_dir):
    """Save before_scores and revision history to a state file."""
    rpath = _review_path(feature_dir)
    if not os.path.exists(rpath):
        print(f"SKIP (no review file in {feature_dir})")
        return

    data, _ = read_frontmatter(rpath)
    state = {
        "before_score": data.get("before_score"),
        "before_scores": data.get("before_scores"),
        "revision_history": _extract_revision_history(rpath),
    }

    spath = _state_path(feature_dir)
    with open(spath, "w") as f:
        json.dump(state, f, indent=2)

    print(f"SAVED state for {feature_dir}")


def restore(feature_dir):
    """Restore before_scores and revision history from the state file."""
    spath = _state_path(feature_dir)
    if not os.path.exists(spath):
        print(f"SKIP (no state file for {feature_dir})")
        return

    with open(spath) as f:
        state = json.load(f)

    rpath = _review_path(feature_dir)
    if not os.path.exists(rpath):
        print(f"SKIP (no review file to restore into for {feature_dir})")
        return

    fm_updates = {}
    if state.get("before_score") is not None:
        fm_updates["before_score"] = state["before_score"]
    if state.get("before_scores"):
        fm_updates["before_scores"] = state["before_scores"]
    if fm_updates:
        update_frontmatter(rpath, fm_updates, "test-plan-review")

    saved_history = state.get("revision_history", "").strip()
    if saved_history:
        with open(rpath) as f:
            content = f.read()

        marker = "## Revision History"
        idx = content.find(marker)
        if idx != -1:
            after_marker = idx + len(marker)
            current_after = content[after_marker:]
            content = (content[:after_marker] + "\n" +
                       saved_history + "\n" + current_after.lstrip("\n"))
            with open(rpath, "w") as f:
                f.write(content)

    os.remove(spath)
    print(f"RESTORED state for {feature_dir}")


def main():
    if len(sys.argv) != 3:
        print("Usage: preserve_review_state.py save|restore <feature_dir>",
              file=sys.stderr)
        sys.exit(2)

    action = sys.argv[1]
    feature_dir = sys.argv[2]

    if action == "save":
        save(feature_dir)
    elif action == "restore":
        restore(feature_dir)
    else:
        print(f"Unknown action: {action}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
