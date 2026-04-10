---
test_case_id: TC-DB-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-DB-002: Retrieve stored tool-calling metadata fields

**Objective**: Verify the database correctly returns all tool-calling metadata fields when queried for a specific model version.

**Preconditions**:
- A model entry with complete tool-calling metadata has been stored in the database

**Test Steps**:
1. Query the database for the model entry by model identifier
2. Verify the returned record contains all five tool-calling metadata fields
3. Verify the data types match what was originally stored

**Expected Results**:
- Query returns exactly one record for the specified model
- All five tool-calling fields are present: `tool_calling_supported`, `required_cli_args`, `chat_template_file_name`, `chat_template_path`, `tool_call_parser`
- Values match the originally inserted data
- Data types are preserved (boolean, list, string, string, string)

**Notes**: To be filled later in the process.
