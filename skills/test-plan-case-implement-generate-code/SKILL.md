---
name: test-plan-case-implement-generate-code
description: Generate test code files from test cases with quality scoring and revision (internal sub-agent)
context: fork
model: opus
user-invocable: false
allowedTools:
  - Read
  - Write
  - Bash
  - Skill
---

# Test Code Generation Sub-Agent

**Internal forked sub-agent** for test-plan-case-implement. Handles Steps 5.1-5.6: checking existing tests, generating code, scoring, and auto-revision.

## Inputs (from parent skill)

Expects these variables passed from parent:
- `file_mapping` - Array of {file_path, test_cases[], function_names[]}
- `test_cases` - Parsed TC data with placement decisions
- `framework` - Test framework (pytest, go, jest, etc.)
- `conventions_file` - Path to test_implementation_conventions.md
- `pattern_guide` - Testing pattern guide content (or null)
- `repo_instructions` - Combined CLAUDE.md/AGENTS.md content (or null)
- `common_setup_requirements` - Shared preconditions for fixtures
- `code_repo_path` - Target repository path
- `feature_dir` - Feature directory for output

## Process

### Step 1: Check Existing Test Implementations

For each file in `file_mapping`:

1. Get full file path: `<code_repo_path>/<file_path>`

2. **If file exists**, list existing functions:
   ```bash
   (cd $(git -C ${CLAUDE_SKILL_DIR} rev-parse --show-toplevel) && uv run python scripts/list_test_functions.py "$full_file_path")
   ```
   
   Returns JSON with all test functions: `{"functions": [{"name": "...", "line": 42, "docstring": "..."}]}`

3. **Semantic matching** - For each TC and expected function name, check if semantic match exists:
   
   **Examples of semantic equivalence:**
   - TC-API-001 "Create notebook" expects `test_create_notebook`
   - Existing `test_notebook_creation` at line 42 → **MATCH** (same concept)
   - Existing `test_delete_notebook` at line 67 → no match (different action)
   
   **How to match:**
   - Read TC title and objective
   - Read existing function name and docstring
   - Determine if they test the same thing (LLM judgment)
   - If match found:
     - Mark TC as `already_implemented`
     - Store existing function name and line number
     - Update TC frontmatter using `update_tc_frontmatter.py`

4. **If file doesn't exist**, all TCs need implementation (set `mode = "create"`)

5. **If already-implemented tests found**, ask user via AskUserQuestion:
   ```
   ✓ Found {N} already-implemented test(s) in {file_path}:
     - TC-API-001: test_notebook_creation (line 42)
     - TC-API-002: test_notebook_deletion (line 67)
   
   Options:
   1. Skip them - Only implement missing tests
   2. Re-generate - Overwrite existing functions (mode=append)
   3. Review - Show me existing code first
   ```
   
   Handle user choice accordingly.

### Step 2: Generate File Header (if mode == "create")

Generate header based on framework and conventions (docstring, imports, common setup fixtures).

### Step 3: Generate Test Functions (PARALLEL)

Invoke `test-plan-create-test-function` forked sub-agent for each TC in parallel:

```python
for tc in test_cases_for_file:
    invoke_skill_forked(
        "test-plan-create-test-function",
        args={
            'tc_file': tc['file'],              # TC specification to implement
            'function_name': function_names[i], # Target function name (e.g., test_create_notebook)
            'framework': framework,              # pytest, unittest, go, jest, etc.
            'conventions_file': conventions_file, # Repo-specific conventions (naming, markers, etc.)
            'pattern_guide': pattern_guide,      # Tiger Team patterns (fixtures, mocking, assertions)
            'repo_instructions': repo_instructions, # CLAUDE.md/AGENTS.md content (high authority)
            'common_setup': common_setup_requirements, # Shared preconditions for fixture generation
            'target_repo': code_repo_path,       # For context (imports, existing utilities)
            'placement': tc['placement_location'] # same_repo or downstream (affects imports)
        }
    )
```

**Why parallel:** 5 TCs = same time as 1 TC. Independent failures don't block others.

Each sub-agent returns test function code (decorator + def + docstring + implementation).

### Step 4: Assemble File Content

- If `mode == "create"`: Combine header + test functions
- If `mode == "append"`: Append to existing content

### Step 5: Validate Python Syntax

Run `python -m py_compile`:
```bash
echo "$final_content" > /tmp/test_file.py
python -m py_compile /tmp/test_file.py 2>&1
```

**If syntax error:**
- Capture error message
- Re-invoke generator with feedback:
  ```
  Syntax error in generated code:
  {error message}
  
  Please fix the syntax error and regenerate.
  ```
- Run syntax check again
- If still invalid after fix: Save as .draft, skip scoring
- **MAX FIX ATTEMPTS: 1**

**If valid:** Proceed to Step 6 (scoring)

### Step 6: Score Quality and Auto-Revise

For each file with valid syntax:

1. Invoke `test-plan-score-test-function`:
   ```bash
   /test-plan-score-test-function \
     --test-code-file <temp_file> \
     --tc-file <tc_file> \
     --conventions-file <conventions_file> \
     --framework <framework> \
     --output-file test_scores/<tc_id>_score.md
   ```

2. Parse score:
   ```bash
   (cd $(git -C ${CLAUDE_SKILL_DIR} rev-parse --show-toplevel) && uv run python scripts/parse_test_score.py test_scores/<tc_id>_score.md)
   ```

4. **Handle verdict based on score:**

   **If verdict == "Ready" or "Good"** (score 7-10):
   - Accept test code as-is
   - Add to `files_to_write` array
   - Log: "✓ Test quality score: {score}/10 ({verdict})"
   - Continue to next test

   **If verdict == "Revise"** (score 4-6):
   - Log: "⚠ Test quality score: {score}/10 - auto-revising"
   - Extract issues from parsed result (contains `### Issues Found` and `### Revision Needed` sections)
   - Re-invoke `test-plan-create-test-function` sub-agent with **same args** PLUS additional feedback:
     ```
     Additional instructions based on quality assessment:
     
     {paste full issues content from parse_test_score.py result}
     ```
   - Generator produces revised code
   - Save revised code to temp file
   - Re-invoke scorer: `/test-plan-score-test-function --output-file test_scores/<tc_id>_score_revised.md`
   - Parse revised score: `parse_test_score.py test_scores/<tc_id>_score_revised.md`
   - **Accept revised code if:**
     - Revised score >= 7 (improved to Good/Ready), OR
     - Max revisions reached (1 revision max to avoid loops)
   - Log: "✓ Auto-revised: {original_score} → {revised_score}"
   - **MAX REVISIONS: 1 per test** (prevents infinite loops)

   **If verdict == "Rework"** (score 0-3):
   - Log: "❌ Test quality score: {score}/10 - significant issues"
   - Save test code as draft: `<full_file_path>.draft`
   - Keep score assessment: `test_scores/<tc_id>_score.md` (already written)
   - Add to `draft_files` array
   - Show issues to user:
     ```
     Test {tc_id} requires manual review (score {score}/10):
     
     Issues found:
     {paste issues from parse result}
     
     Draft saved to: {file_path}.draft
     Score details: test_scores/{tc_id}_score.md
     
     Please review and fix manually.
     ```
   - **DO NOT** add to `files_to_write` (user must fix draft manually)

5. **Track quality metrics** during scoring:
   - `ready_count` (score 9-10)
   - `good_count` (score 7-8)
   - `revised_count` (auto-revised from 4-6 to 7+)
   - `flagged_count` (score 0-3, saved as .draft)
   - List of revised TCs with before/after scores

6. **Present quality summary** after all tests scored:
   ```
   Test Quality Summary:
   - {ready_count} tests scored 9-10 (Ready - excellent quality)
   - {good_count} tests scored 7-8 (Good - minor improvements needed)
   - {revised_count} tests auto-revised (improved from 4-6 to 7+)
     {if revised_count > 0, list: TC-XXX: 5→8, TC-YYY: 4→7}
   - {flagged_count} tests flagged for review (score 0-3)
     {if flagged_count > 0, list draft files with scores}
   
   {if common_setup_requirements present}
   Suggested Fixtures:
   - '{requirement}' used by {count} TCs → Consider extracting to fixture
   ```

## Error Handling

**If generator sub-agent fails:**
- Log error with TC ID
- Try once more with simplified instructions
- If still fails: Add to `errors` array, continue with remaining TCs

**If syntax validation fails after fix attempt:**
- Save as `.draft` with syntax error message
- Add to `draft_files` with reason
- Continue with remaining TCs

**If scorer sub-agent fails:**
- Accept test code without scoring (better than blocking)
- Log warning
- Continue

**Philosophy:** Partial success is better than total failure. One bad TC shouldn't block the entire batch.

## Output

Returns to parent skill:
```json
{
  "files_to_write": [
    {"path": "tests/test_api.py", "content": "...", "test_cases": ["TC-API-001", "TC-API-002"]},
  ],
  "quality_summary": {
    "ready_count": 3,
    "good_count": 2,
    "revised_count": 1,
    "flagged_count": 0,
    "revised_details": [
      {"tc_id": "TC-API-003", "before": 5, "after": 8}
    ]
  },
  "draft_files": [
    {"path": "tests/test_e2e.py.draft", "tc_id": "TC-E2E-001", "score": 2, "reason": "Rework needed"}
  ],
  "errors": [
    {"tc_id": "TC-XXX-999", "error": "Generator failed after retry"}
  ]
}
```
