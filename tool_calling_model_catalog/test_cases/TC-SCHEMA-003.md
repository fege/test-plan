---
test_case_id: TC-SCHEMA-003
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-003: Store chat_template_path and chat_template_file_name fields

**Objective**: Verify that the Model Catalog schema correctly stores and retrieves both `chat_template_path` and `chat_template_file_name` string fields for upstream and downstream template locations.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog database deployed and accessible
- Database schema migration applied with tool-calling fields

**Test Steps**:
1. Insert a model entry with upstream chat template values:
   ```json
   {
     "chat_template_path": "examples/tool_chat_template_granite.jinja",
     "chat_template_file_name": "tool_chat_template_granite.jinja"
   }
   ```
2. Query the database and verify both fields are stored correctly
3. Insert a second model entry with downstream chat template values:
   ```json
   {
     "chat_template_path": "opt/app-root/template/tool_chat_template_granite.jinja",
     "chat_template_file_name": "tool_chat_template_granite.jinja"
   }
   ```
4. Query and verify the downstream path is stored correctly
5. Verify both entries can coexist with different `chat_template_path` values but the same `chat_template_file_name`

**Expected Results**:
- Both `chat_template_path` and `chat_template_file_name` are stored as strings
- Upstream path format (`examples/<filename>`) is preserved
- Downstream path format (`opt/app-root/template/<filename>`) is preserved
- File name is consistent across path formats

**Notes**: To be filled later in the process.
