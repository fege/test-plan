---
test_case_id: TC-VER-003
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-VER-003: Multiple model versions with different template paths coexist

**Objective**: Verify the catalog correctly maintains different tool-calling metadata for multiple versions of the same model.

**Preconditions**:
- The catalog supports multiple versions per model

**Test Steps**:
1. Ingest version 1.0 of granite-3.1-8b-instruct with one set of tool-calling metadata
2. Ingest version 2.0 of the same model with updated tool-calling metadata (different chat template path and parser)
3. Query the API for version 1.0 metadata
4. Query the API for version 2.0 metadata
5. Verify each version returns its own distinct metadata

**Test Data**:
```json
[
  {
    "model_name": "granite-3.1-8b-instruct",
    "model_version": "1.0",
    "chat_template_path": "/opt/app-root/template/tool_chat_template_granite.jinja",
    "tool_call_parser": "granite"
  },
  {
    "model_name": "granite-3.1-8b-instruct",
    "model_version": "2.0",
    "chat_template_path": "/opt/app-root/template/v2/tool_chat_template_granite.jinja",
    "tool_call_parser": "granite_v2"
  }
]
```

**Expected Results**:
- Version 1.0 returns `chat_template_path: "/opt/app-root/template/tool_chat_template_granite.jinja"` and `tool_call_parser: "granite"`
- Version 2.0 returns `chat_template_path: "/opt/app-root/template/v2/tool_chat_template_granite.jinja"` and `tool_call_parser: "granite_v2"`
- No cross-contamination between version metadata
- Both versions are independently accessible

**Notes**: To be filled later in the process.
