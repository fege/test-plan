---
test_case_id: TC-SCHEMA-007
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-007: Schema rejects invalid field types for tool-calling metadata

**Objective**: Verify that the Model Catalog schema rejects or handles gracefully when tool-calling fields receive values of incorrect types.

**Test Steps**:
1. Attempt to insert a model entry with `tool_calling_supported: "yes"` (string instead of boolean)
2. Verify the insertion is rejected with a validation error or the value is not accepted
3. Attempt to insert a model entry with `required_cli_args: "--max-model-len 8192"` (string instead of list)
4. Verify the insertion is rejected or handled gracefully
5. Attempt to insert a model entry with `tool_call_parser: 12345` (integer instead of string)
6. Verify the insertion is rejected or handled gracefully

**Expected Results**:
- Invalid type inputs are rejected with descriptive error messages
- No partial writes that could leave the database in an inconsistent state
- Valid entries in the same batch are not affected by invalid entries

**Notes**: To be filled later in the process.
