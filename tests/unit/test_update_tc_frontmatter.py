"""
Unit tests for scripts/update_tc_frontmatter.py

Tests bulk TC frontmatter updates for automation tracking.
"""

import json

from scripts.update_tc_frontmatter import update_tc_frontmatter
from tests.constants import MINIMAL_TC_CONTENT


def test_updates_automation_status(tmp_path):
    """Should update automation_status and related fields."""
    tc_dir = tmp_path / "test_cases"
    tc_dir.mkdir()
    (tc_dir / "TC-API-001.md").write_text(MINIMAL_TC_CONTENT)

    updates = [
        {
            "tc_id": "TC-API-001",
            "automation_status": "Implemented",
            "file": "tests/test_api.py",
            "function": "test_create_notebook"
        }
    ]

    result = update_tc_frontmatter(str(tmp_path), updates)
    data = json.loads(result)

    assert data['updated_count'] == 1
    assert "TC-API-001" in data['updated_tcs']

    # Verify file was actually updated
    from scripts.utils.frontmatter_utils import read_frontmatter
    fm, _ = read_frontmatter(str(tc_dir / "TC-API-001.md"))
    assert fm['automation_status'] == 'Implemented'
    assert fm['file'] == 'tests/test_api.py'
    assert fm['function'] == 'test_create_notebook'


def test_handles_missing_tc_file(tmp_path):
    """Should report error for missing TC file."""
    tc_dir = tmp_path / "test_cases"
    tc_dir.mkdir()

    updates = [{"tc_id": "TC-MISSING-001", "automation_status": "Implemented"}]

    result = update_tc_frontmatter(str(tmp_path), updates)
    data = json.loads(result)

    assert data['updated_count'] == 0
    assert len(data['errors']) == 1
    assert "TC-MISSING-001" in data['errors'][0]
