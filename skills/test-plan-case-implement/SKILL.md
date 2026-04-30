---
name: test-plan-case-implement
description: Generate executable test automation code from test case specifications with intelligent placement in component or downstream repos. Use after test cases are reviewed to create production-ready pytest code that follows repository conventions.
argument-hint: "[FEATURE_SOURCE] [--test-cases TC-ID,TC-ID] [--target-repo PATH]"
user-invocable: true
model: opus
allowedTools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Skill
  - AskUserQuestion
---

# Test Case Implementation Generator

Generate executable test automation code (pytest, etc.) from TC-*.md test case specification files, with intelligent auto-placement in component repos or downstream E2E repo.

## Usage

```
/test-plan-case-implement [FEATURE_SOURCE] [--test-cases TC-API-001,TC-API-002] [--target-repo ~/Code/opendatahub-tests]
```

Examples:
- `/test-plan-case-implement` (auto-detects from prior `/test-plan-publish` or `/test-plan-create-cases` run)
- `/test-plan-case-implement features/notebooks/RHAISTRAT-400-notebook-spawning`
- `/test-plan-case-implement test-plan/RHAISTRAT-400` (GitHub branch)
- `/test-plan-case-implement --test-cases TC-API-001,TC-API-002` (selective)
- `/test-plan-case-implement features/notebooks/RHAISTRAT-400 --target-repo ~/Code/opendatahub-tests`

## Inputs

### From arguments
Parse `$ARGUMENTS` to extract:
1. **First argument** (optional): Feature source - local directory or GitHub branch containing test case artifacts
   - Local path: `features/notebooks/RHAISTRAT-400-notebook-spawning`
   - GitHub branch: `https://github.com/org/repo/tree/test-plan/RHAISTRAT-400` or `test-plan/RHAISTRAT-400`
2. **`--test-cases`** (optional): Comma-separated list of test case IDs to implement (e.g., `TC-API-001,TC-API-002,TC-E2E-001`)
3. **`--target-repo`** (optional): Override auto-detected target repository path or URL

### Interactive fallback
If no feature source argument is provided, ask the user via AskUserQuestion:
> **Where is the test plan with test cases to implement?**
>
> You can provide:
> - Local directory path (e.g., `~/Code/collection-tests/evalhub_metrics`)
> - GitHub branch URL (e.g., `https://github.com/org/repo/tree/test-plan/RHAISTRAT-1507`)
> - GitHub PR URL (e.g., `https://github.com/fege/collection-tests/pull/4`)

## Process

### Step 0: Pre-flight Checks

#### 0.0 Python dependencies

Install the test-plan package (makes all scripts importable):
```bash
(cd $(git -C ${CLAUDE_SKILL_DIR} rev-parse --show-toplevel) && rm -rf .venv && uv venv && uv pip install -e ".[dev]")
```

If installation fails, inform the user and do NOT proceed.

#### 0.1 Locate feature directory

If feature source is a GitHub branch or PR URL:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/repo.py locate-feature-dir "$ARGUMENTS"
```

Extract `feature_dir` from the JSON result.

If feature source is a local path, use it directly as `feature_dir`.

#### 0.2 Run preflight checks

Run unified preflight validation and detection:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/preflight.py "$feature_dir"
```

The script returns JSON with:
- `valid` (bool) - If false, show error and stop
- `feature_dir`, `tc_count`, `testplan_frontmatter`
- `frontmatter_components`, `content_components`, `all_components`
- `repos` (component → repo mapping)
- `unique_repos` (list of detected repositories)
- `repos_from_frontmatter` (repos from Jira components - highest priority)
- `odh_test_context_path` (or null if not found)

Extract values from the JSON result as needed for subsequent steps.

#### 0.3 Handle odh-test-context if not found

If `odh_test_context_path == "null"`, ask user via AskUserQuestion:
> odh-test-context not found. Provides test conventions for ~162 opendatahub-io repos.
>
> 1. Specify path to existing clone
> 2. Clone from GitHub to ~/Code/
> 3. Proceed without it (slower, less accurate)

Handle user choice.

#### 0.4 Confirm target repository

Based on `unique_repos` from preflight:

**If 1 repo:** Ask "Proceed with {repo}?" (yes/specify-different)

**If multiple repos:** Show list prioritized by frontmatter components, ask user to choose

**If no repos:** Ask user to specify repository manually

Store: `code_repo` (e.g., `opendatahub-io/notebooks`)

#### 0.5 Locate code repository

Find code repo locally:
```bash
code_repo_path=$(uv run python ${CLAUDE_SKILL_DIR}/scripts/repo.py find-target "$code_repo")
```

If not found, ask to clone or specify path.

### Step 1: Load Testing Context

#### 1.0 Load odh-test-context for code repository

Use `scripts/utils/repo_utils.py::load_repo_test_context(repo_name, odh_test_context_path)`:

If odh-test-context is available:
1. Checks for `<odh_test_context_path>/tests/<repo_name>.json`
2. If found:
   - Reads and parses JSON
   - Returns context dict with: framework, directories, commands, conventions, linting, agent_readiness, container_recipe
3. If NOT found:
   - Returns None

Script saves context to `<feature_dir>/test_implementation_context.json` if found.

Returns:
- `test_context` (dict or None)
- `use_odh_context` (bool)

#### 1.0b Load downstream E2E repository context

Use `scripts/utils/repo_utils.py::load_repo_test_context('opendatahub-tests', odh_test_context_path)`:

Returns:
- `downstream_context` (dict with framework, conventions, markers, agent_readiness)
- Falls back to defaults if not found: pytest, basic markers, agent_readiness=medium

#### 1.1 Detect test framework

Use `scripts/utils/repo_utils.py::get_framework(test_context)`:

If `test_context` exists: returns `test_context['testing']['framework']`

If NOT (manual detection):
1. Checks for pytest indicators (pytest.ini, pyproject.toml, conftest.py)
2. Checks for unittest indicators (import unittest in .py files)
3. Checks for Playwright indicators (playwright.config.js/ts)
4. Checks for Robot Framework indicators (*.robot files)
5. Checks for Go testing indicators (*_test.go files, Ginkgo imports)
6. Checks for Jest indicators (jest.config.js, .spec.ts files, describe/it blocks)
7. Checks for Cypress indicators (.cy.ts/.cy.js files, cy. commands)
8. If unknown: asks user via AskUserQuestion

Returns: `framework` (str: pytest, unittest, playwright, robot, ginkgo, go-testing, jest, cypress)

#### 1.2 Load test conventions

If `use_odh_context == True`:
1. Use `scripts/utils/repo_utils.py::extract_conventions_from_context(test_context)` to extract:
   - File patterns, function patterns, import style, markers
   - Linting tools and commands
   - Testing directories and execution commands
2. Generate conventions summary markdown
3. Write to `<feature_dir>/test_implementation_conventions.md`

If `use_odh_context == False` (no odh-test-context available):
1. Conventions will be minimal (framework only, from Step 1.1)
2. Test generation will rely more heavily on Tiger Team pattern guides (Step 1.2b)
3. Generated tests may be less optimized for the specific repo
4. **For new components**: Consider contributing to odh-test-context for future use:
   - Repository: https://github.com/opendatahub-io/odh-test-context
   - Add JSON file: `tests/<repo_name>.json` with discovered framework, test directories, conventions, linting tools
   - See existing files in `tests/` directory as examples
   - Improves test quality for all future test generation on this component

Store: `conventions` (dict or markdown content)

#### 1.2b Load testing pattern guides

Load repo instructions and pattern guides:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/load_pattern_guides.py "$code_repo_path" "$framework"
```

Returns JSON with:
- `repo_instructions_files` - Found CLAUDE.md, AGENTS.md, CONSTITUTION.md
- `repo_instructions_content` - Combined content
- `pattern_guide_files` - Found {framework}-tests.md, testing-standards.md
- `pattern_guide_content` - Combined content
- `needs_generation` - true if no pattern guides found

**If `needs_generation == true`:**

1. Locate Tiger Team: `uv run python scripts/repo.py find-known tiger-team`
2. If found: Invoke `/test-rules-generator <code_repo_path>` to generate guides
3. If not found: Ask user to clone Tiger Team or proceed without guides

**Pattern guides** describe HOW to write tests (fixtures, naming, mocking). Passed to code generation sub-agents in Step 5.

#### 1.3 Offer container validation

If `use_odh_context == True` AND `test_context` contains `container_recipe`:
1. Show user the container validation option via AskUserQuestion:
   > Container validation is available using odh-test-context.
   > - Base image: <container_recipe.base_image>
   > - Can validate linting and test execution in isolated environment
   >
   > Validate generated tests in container after creation? [yes/no]

2. If **yes**: Set `validate_in_container = True` and store `validation_recipe = test_context['container_recipe']`
3. If **no**: Set `validate_in_container = False`

If container recipe NOT available:
1. Set `validate_in_container = False`

### Step 2: Per-TC Placement Analysis

Extract repository capabilities from Step 1:
- `code_repo_readiness` from `test_context.get('agent_readiness', 'unknown')`
- `code_repo_has_tests` from checking if 'tests' in `test_context.get('testing', {}).get('directories', [])`
- `downstream_readiness` from `downstream_context.get('agent_readiness', 'medium')`

Invoke **`test-plan.analyze.placement`** forked subagent:

```python
placement_decisions = invoke_skill_forked(
    "test-plan.analyze.placement",
    args={
        'feature_dir': feature_dir,
        'code_repo': code_repo,
        'code_repo_readiness': code_repo_readiness,
        'code_repo_has_tests': code_repo_has_tests,
        'downstream_readiness': downstream_readiness
    }
)
```

The subagent analyzes each TC and returns placement recommendations with:
- Test level classification (unit, integration, k8s-integration, api, e2e)
- Placement scores (same_repo, downstream, both)
- Recommended placement with reasoning
- User confirmation (accept all or review/override per TC)

**Placement Philosophy** (applied by subagent):
- **P0 strongly prefers upstream** for fast feedback (blocks PRs early)
- **K8s API ≠ Full Stack**: K8s integration tests can use envtest in component repo
- **E2E requires appropriate stack**: Mocked E2E → component repo, full-stack E2E → downstream

Store the returned placement decisions in `test_cases` list (each TC dict includes `placement_location`, `level`, `scores`, `reasons`).

If any TCs are placed `downstream` or `both`, locate downstream repository:
1. Find the downstream repo:
   ```bash
   downstream_repo_path=$(uv run python ${CLAUDE_SKILL_DIR}/scripts/repo.py find-target "opendatahub-io/opendatahub-tests")
   ```
2. If NOT found (exit code 1): Ask user to clone it:
   ```bash
   downstream_repo_path=$(uv run python ${CLAUDE_SKILL_DIR}/scripts/repo.py clone "<downstream_url>" "~/Code/opendatahub-tests")
   ```
3. Set `downstream_repo_path`

### Step 3: Select Test Cases to Implement

#### 3.1 Parse --test-cases argument

If `--test-cases` was provided:
1. Parse comma-separated list (e.g., `TC-API-001,TC-API-002,TC-E2E-001`)
2. Validate each TC ID exists in `test_cases/`
3. If any TC ID not found, inform user and stop
4. Set `selected_test_cases = [parsed TC IDs]`
5. Set `mode = "selective"`

If `--test-cases` was NOT provided:
1. Read all TC IDs from `test_cases/INDEX.md`
2. Set `selected_test_cases = [all TC IDs]`
3. Set `mode = "batch"`

Present summary:
- If selective: `Implementing <N> selected test case(s): <TC IDs>`
- If batch: `Implementing ALL test cases for feature: <feature_name>. Total: <N> test cases`

Show counts by priority (P0/P1/P2) and by category.

Ask for confirmation via AskUserQuestion: `Proceed? [yes/no]`

#### 3.2 Filter already-implemented test cases

Filter test cases by automation_status:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/filter_test_cases.py "$feature_dir" $selected_test_cases
```

Returns JSON with `to_implement` and `already_implemented` arrays.

If `already_implemented` is not empty, ask via AskUserQuestion: `Re-implement these? [yes/no]`

Use `to_implement` list for subsequent steps.

#### 3.3 Read and parse TC files

For each TC in `selected_test_cases`:
1. Use `scripts/utils/parse_tc_file(tc_file)` to read and parse
2. Store in `test_cases` list as dict with all TC data + placement decisions from Step 2.2

### Step 4: Map Test Cases to Test Files

Determine file organization strategy from conventions:
- If `test_context` shows subdirectories (unit/, api/, etc.) → `by-category-with-subdirs`
- Default → `by-category` (flat structure, one file per category)
- If unclear, ask user (by-category / one-per-tc)

Generate file mapping:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/map_test_files.py \
    "$feature_dir" "$org_pattern" "$test_dir" \
    --feature-name "$feature_name" \
    --tc-ids "$(echo $selected_test_cases | tr ' ' ',')"
```

Returns JSON with:
- `file_mapping` - Array of {file_path, test_cases[], function_names[]}
- `strategy`, `total_test_cases`, `total_files`

Groups TCs by category, generates file paths and function names from TC titles.

Present mapping table to user and ask for confirmation.

### Step 5: Generate Test Code

Identify common setup requirements:
```bash
uv run python ${CLAUDE_SKILL_DIR}/scripts/utils/test_analyzer.py "$feature_dir"
```

Returns preconditions used by 2+ TCs for fixture generation.

Invoke forked sub-agent to generate code:
```bash
/test-plan-case-implement-generate-code \
  --file-mapping "$file_mapping_json" \
  --test-cases "$test_cases_json" \
  --framework "$framework" \
  --conventions-file "$conventions_file" \
  --pattern-guide "$pattern_guide_content" \
  --repo-instructions "$repo_instructions_content" \
  --common-setup "$common_setup_json" \
  --code-repo-path "$code_repo_path" \
  --feature-dir "$feature_dir"
```

Sub-agent handles:
- Check existing tests (list_test_functions.py)
- Generate functions (parallel sub-agents)
- Validate syntax (py_compile)
- Score quality (parse_test_score.py)
- Auto-revise if needed

Returns JSON with `files_to_write`, `quality_summary`, `draft_files`.

### Step 6: Write Tests to Repositories

#### 6.1 Write test files

For each entry in `files_to_write`:
1. Create parent directories: `mkdir -p <dirname>`
2. Write file content
3. Run syntax check: `python -m py_compile <file_path>`
4. If syntax check fails, warn user but continue

#### 6.2 Validate imports in repo context

For each written file:
1. Try importing in the target repo's Python environment:
   ```bash
   cd <target_repo_path>
   python -c "import sys; sys.path.insert(0, '.'); exec(open('<file_path>').read())"
   ```
2. If import fails, warn user with error message but do not block

#### 6.3 Container validation (optional)

If `validate_in_container == True`:

1. **Start container**:
   ```bash
   podman run -d --name test-context-<repo_name>-validation \
     -v <target_repo_path>:/app:Z \
     -w /app \
     <validation_recipe.base_image> \
     sleep infinity
   ```

2. **Install system dependencies**:
   ```bash
   podman exec test-context-<repo_name>-validation bash -c \
     "apt-get update && apt-get install -y <system_deps>"
   ```

3. **Run setup commands** from `validation_recipe.setup_commands`

4. **Run lint on generated files**:
   Report lint results (pass/fail)

5. **Run tests on generated files**:
   For each generated test file, run pytest and report results

6. **Cleanup container**:
   ```bash
   podman rm -f test-context-<repo_name>-validation
   ```

Present validation summary to user.

### Step 7: Update Test Case Frontmatter and Present Summary

Build updates array from `test_cases` and `file_mapping`, then update in bulk:
```bash
# updates.json: [{"tc_id": "TC-API-001", "automation_status": "Implemented", "file": "...", "function": "..."}]
echo "$updates_json" | uv run python ${CLAUDE_SKILL_DIR}/scripts/update_tc_frontmatter.py "$feature_dir" -
```

Returns JSON with `updated_count`, `updated_tcs`, `errors`. Show any errors to user.

If feature source is a GitHub branch, commit updated TC files:
```bash
git add <feature_dir>/test_cases/*.md
git commit -m "test-plan(<source_key>): mark TCs as implemented"
git push origin <branch_name>
```

#### 7.2 Present Summary Report

Display implementation summary:
- Feature name, source key, TC count
- Files created with TC mapping
- Test quality distribution (Ready/Good/Revised/Flagged)
- Suggested fixtures (if common setup found)
- Next steps (review, run tests, create PR)

$ARGUMENTS
