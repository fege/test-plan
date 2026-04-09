---
test_case_id: TC-DB-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-DB-005: Store metadata with tool_calling_supported set to false

**Objective**: Verify the database correctly stores a model entry where tool calling is explicitly marked as not supported.

**Preconditions**:
- Model Catalog database is accessible

**Test Steps**:
1. Insert a model entry with `tool_calling_supported` set to `false` and other tool-calling fields empty or null
2. Query the database to retrieve the stored record
3. Verify the boolean field is stored correctly as `false`

**Test Data**:
```yaml
model_name: granite-3.0-2b-instruct
tool_calling_supported: false
required_cli_args: []
chat_template_file_name: null
chat_template_path: null
tool_call_parser: null
```

**Expected Results**:
- `tool_calling_supported` is stored as boolean `false`
- `required_cli_args` is stored as an empty list
- `chat_template_file_name`, `chat_template_path`, and `tool_call_parser` are null or empty
- The model entry does not appear in tool-calling filtered queries

**Notes**: To be filled later in the process.
