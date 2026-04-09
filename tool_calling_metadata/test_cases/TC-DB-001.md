---
test_case_id: TC-DB-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-DB-001: Store all tool-calling metadata fields for a model

**Objective**: Verify the Model Catalog database can successfully persist all required tool-calling metadata fields for a model entry.

**Preconditions**:
- Model Catalog database is accessible
- Admin user has write permissions to the catalog

**Test Steps**:
1. Insert a model entry with all tool-calling metadata fields populated
2. Query the database to retrieve the stored record
3. Verify all fields were stored correctly with expected types and values

**Test Data**:
```yaml
model_name: granite-3.1-8b-instruct
tool_calling_supported: true
required_cli_args:
  - "--max-model-len"
  - "8192"
chat_template_file_name: tool_chat_template_granite.jinja
chat_template_path: /opt/app-root/template/tool_chat_template_granite.jinja
tool_call_parser: granite
```

**Expected Results**:
- `tool_calling_supported` is stored as a boolean value `true`
- `required_cli_args` is stored as a list containing `["--max-model-len", "8192"]`
- `chat_template_file_name` is stored as string `tool_chat_template_granite.jinja`
- `chat_template_path` is stored as string `/opt/app-root/template/tool_chat_template_granite.jinja`
- `tool_call_parser` is stored as string `granite`

**Validation**:
- Direct database query confirms all fields are present and correctly typed
- No data truncation or encoding issues in stored values

**Notes**: To be filled later in the process.
