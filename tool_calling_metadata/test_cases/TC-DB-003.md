---
test_case_id: TC-DB-003
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-DB-003: Store metadata with multiple CLI arguments

**Objective**: Verify the database correctly stores and retrieves a model entry with a large set of CLI arguments in the required_cli_args list.

**Preconditions**:
- Model Catalog database is accessible
- Admin user has write permissions

**Test Steps**:
1. Insert a model entry with multiple CLI arguments in required_cli_args
2. Query the database to retrieve the stored record
3. Verify all CLI arguments are preserved in order

**Test Data**:
```yaml
model_name: llama-3.1-70b-instruct
tool_calling_supported: true
required_cli_args:
  - "--max-model-len"
  - "32768"
  - "--tensor-parallel-size"
  - "4"
  - "--gpu-memory-utilization"
  - "0.95"
  - "--enforce-eager"
chat_template_file_name: tool_chat_template_llama3.1_json.jinja
chat_template_path: /opt/app-root/template/tool_chat_template_llama3.1_json.jinja
tool_call_parser: llama3_json
```

**Expected Results**:
- All 7 CLI argument entries are stored and retrievable
- Arguments maintain their original order
- No truncation of the list occurs

**Notes**: To be filled later in the process.
