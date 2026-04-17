---
test_case_id: TC-SCHEMA-006
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-006: Schema handles empty required_cli_args list

**Objective**: Verify that the Model Catalog schema correctly handles a model entry with an empty `required_cli_args` list, representing a model that requires no special CLI arguments to run.

**Test Steps**:
1. Insert a model entry with `tool_calling_supported: true` and `required_cli_args: []` (empty list)
2. Query the database and verify `required_cli_args` is stored as an empty list (not null)
3. Retrieve the model via the BFF API
4. Verify the API response includes `required_cli_args` as an empty array `[]`, not omitted or null

**Expected Results**:
- Empty list `[]` is distinct from `null` in storage
- API response correctly reflects the empty list
- No errors during storage or retrieval

**Test Data**:
```json
{
  "model_id": "granite-3.1-2b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": [],
  "tool_call_parser": "hermes",
  "chat_template_path": "examples/tool_chat_template_granite_2b.jinja",
  "chat_template_file_name": "tool_chat_template_granite_2b.jinja"
}
```

**Notes**: To be filled later in the process.
