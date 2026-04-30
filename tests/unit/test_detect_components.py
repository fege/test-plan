"""
Unit tests for scripts/detect_components.py

Tests component detection and repository mapping logic.
"""

import json
from pathlib import Path

import pytest

from scripts.detect_components import detect_components


class TestDetectComponents:
    """Test detect_components function."""

    def _create_testplan(self, tmp_path, components=None, scope_text="", endpoints_text=""):
        """Helper to create TestPlan.md with minimal valid frontmatter."""
        components_yaml = ""
        if components is not None:
            if components:
                components_yaml = "components:\n" + "\n".join(f"  - {c}" for c in components)
            else:
                components_yaml = "components: []"

        testplan = tmp_path / "TestPlan.md"
        testplan.write_text(f"""---
source_key: RHAISTRAT-1507
feature: Test Feature
version: 1.0.0
{components_yaml}
---

## 1. Test Objectives
Test objectives here.

### 1.2 Scope
{scope_text}

## 4. Endpoints Under Test
{endpoints_text}
""")

        # Create test_cases directory
        tc_dir = tmp_path / "test_cases"
        tc_dir.mkdir()
        (tc_dir / "INDEX.md").write_text("# Test Cases Index")

        return testplan

    def test_detects_frontmatter_components_only(self, tmp_path):
        """Should extract components from frontmatter only."""
        self._create_testplan(
            tmp_path,
            components=["AI Hub", "Notebooks"],
            scope_text="Test notebook spawning."
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert 'ai hub' in data['frontmatter_components']
        assert 'notebooks' in data['frontmatter_components']
        assert len(data['frontmatter_components']) == 2

        assert data['repos']['ai hub'] == 'opendatahub-io/model-registry'
        assert data['repos']['notebooks'] == 'opendatahub-io/notebooks'

        assert len(data['unique_repos']) == 2
        assert 'opendatahub-io/model-registry' in data['unique_repos']
        assert 'opendatahub-io/notebooks' in data['unique_repos']

    def test_detects_content_components_only(self, tmp_path):
        """Should extract components from content when no frontmatter components."""
        self._create_testplan(
            tmp_path,
            components=None,
            scope_text="Tests the ODH Dashboard REST API for managing notebooks.",
            endpoints_text="| `/api/v1/dashboard/config` | GET | Config |\n| `/api/v1/notebooks` | POST | Create |"
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert 'dashboard' in data['content_components']
        assert 'notebooks' in data['content_components']

        assert data['repos']['dashboard'] == 'opendatahub-io/odh-dashboard'
        assert data['repos']['notebooks'] == 'opendatahub-io/notebooks'

    def test_merges_and_deduplicates_components(self, tmp_path):
        """Should merge frontmatter and content components, deduplicating."""
        self._create_testplan(
            tmp_path,
            components=["KServe"],
            scope_text="Tests KServe model serving and MLServer runtime.",
            endpoints_text="| `/api/v1/serving/models` | GET | Models |"
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert 'kserve' in data['frontmatter_components']
        assert 'kserve' in data['content_components']
        assert 'mlserver' in data['content_components']

        # Should deduplicate kserve (appears in both frontmatter and content)
        kserve_count = data['all_components'].count('kserve')
        assert kserve_count == 1

    def test_handles_multiple_components_to_same_repo(self, tmp_path):
        """Should handle multiple components mapping to the same repository."""
        self._create_testplan(
            tmp_path,
            components=["Notebooks", "Workbenches"]
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert data['repos']['notebooks'] == 'opendatahub-io/notebooks'
        assert data['repos']['workbenches'] == 'opendatahub-io/notebooks'

        # Both map to same repo, unique_repos should have 1 entry
        assert len(data['unique_repos']) == 1
        assert data['unique_repos'][0] == 'opendatahub-io/notebooks'

    def test_handles_unknown_components(self, tmp_path):
        """Should handle components not in the mapping."""
        self._create_testplan(
            tmp_path,
            components=["UnknownComponent", "Notebooks"]
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        # Unknown component maps to null
        assert data['repos']['unknowncomponent'] is None

        # Known component still maps correctly
        assert data['repos']['notebooks'] == 'opendatahub-io/notebooks'

        # unique_repos should only include valid repos (not null)
        assert 'opendatahub-io/notebooks' in data['unique_repos']
        assert None not in data['unique_repos']

    def test_prioritizes_frontmatter_components(self, tmp_path):
        """Should mark frontmatter components separately for priority."""
        self._create_testplan(
            tmp_path,
            components=["AI Hub"],
            scope_text="Tests dashboard and notebooks."
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert len(data['frontmatter_components']) == 1
        assert 'ai hub' in data['frontmatter_components']

        # content should have dashboard, notebooks
        assert 'dashboard' in data['content_components']
        assert 'notebooks' in data['content_components']

        # repos_from_frontmatter should only include AI Hub's repo
        assert 'opendatahub-io/model-registry' in data['repos_from_frontmatter']
        assert 'opendatahub-io/odh-dashboard' not in data['repos_from_frontmatter']

    def test_handles_missing_testplan(self, tmp_path):
        """Should raise error if TestPlan.md is missing."""
        with pytest.raises(FileNotFoundError, match="TestPlan.md not found"):
            detect_components(str(tmp_path))

    def test_handles_missing_or_empty_components(self, tmp_path):
        """Should handle missing or empty components field."""
        # Test with empty list
        self._create_testplan(
            tmp_path,
            components=[],
            scope_text="Tests dashboard API."
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        assert data['frontmatter_components'] == []
        assert 'dashboard' in data['content_components']

    def test_case_insensitive_matching(self, tmp_path):
        """Should handle different cases for component names."""
        self._create_testplan(
            tmp_path,
            components=["AI Hub", "Model Registry"]
        )

        result = detect_components(str(tmp_path))
        data = json.loads(result)

        # Should normalize to lowercase
        assert 'ai hub' in data['frontmatter_components']
        assert 'model registry' in data['frontmatter_components']

        # Both map to same repo
        assert data['repos']['ai hub'] == 'opendatahub-io/model-registry'
        assert data['repos']['model registry'] == 'opendatahub-io/model-registry'

        assert len(data['unique_repos']) == 1
