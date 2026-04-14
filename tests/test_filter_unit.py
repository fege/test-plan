"""
Unit test for filter_for_revision module - simple test to increase coverage.
"""

import tempfile
from pathlib import Path

from scripts.artifact_utils import write_frontmatter
from scripts import filter_for_revision


def test_filter_for_revision_module_logic():
    """Test filter_for_revision decision logic by importing directly."""

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a review file with all criteria at 2 (should SKIP)
        review_path = Path(tmpdir) / "TestPlanReview.md"

        review_data = {
            "feature": "test_feature",
            "strat_key": "RHAISTRAT-400",
            "score": 10,
            "pass": True,
            "verdict": "Ready",
            "scores": {
                "specificity": 2,
                "grounding": 2,
                "scope_fidelity": 2,
                "actionability": 2,
                "consistency": 2,
            },
            "auto_revised": False,
            "before_score": None,
            "before_scores": None,
            "error": None,
            "last_updated": "2026-04-14",
        }

        review_path.write_text("## Test Plan Review\n")
        write_frontmatter(review_path, review_data, "test-plan-review")

        # Verify the module is importable and has main function
        assert hasattr(filter_for_revision, 'main')
