---
test_case_id: TC-DB-004
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-DB-004: Store metadata preserves downstream chat template path format

**Objective**: Verify the database correctly stores the downstream chat template path format used in RHOAI deployments, distinct from the upstream path.

**Preconditions**:
- Model Catalog database is accessible

**Test Steps**:
1. Insert a model entry where `chat_template_path` uses the downstream format (`/opt/app-root/template/...`)
2. Query the database to retrieve the stored record
3. Verify the path is stored exactly as provided, with no path normalization or modification

**Test Data**:
```yaml
model_name: mistral-7b-instruct-v0.3
tool_calling_supported: true
required_cli_args:
  - "--max-model-len"
  - "8192"
chat_template_file_name: tool_chat_template_mistral.jinja
chat_template_path: /opt/app-root/template/tool_chat_template_mistral.jinja
tool_call_parser: mistral
```

**Expected Results**:
- `chat_template_path` is stored as `/opt/app-root/template/tool_chat_template_mistral.jinja` without any modification
- `chat_template_file_name` is stored as `tool_chat_template_mistral.jinja`
- The distinction between upstream (`examples/...`) and downstream (`/opt/app-root/template/...`) paths is preserved

**Notes**: To be filled later in the process.
