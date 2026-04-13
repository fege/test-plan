---
test_case_id: TC-SCHEMA-004
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-004: Store tool_call_parser string field in Model Catalog

**Objective**: Verify that the Model Catalog schema correctly stores and retrieves the `tool_call_parser` string field identifying the parser type for tool calling.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog database deployed and accessible
- Database schema migration applied with tool-calling fields

**Test Steps**:
1. Insert a model entry with `tool_call_parser: "hermes"` for a Granite model
2. Query the database and verify the value is stored as `"hermes"`
3. Insert a second model entry with `tool_call_parser: "llama3_json"` for a Llama model
4. Query and verify the value is stored as `"llama3_json"`
5. Insert a third model entry with `tool_call_parser: "mistral"` for a Mistral model
6. Query and verify all three parser values are retrievable

**Expected Results**:
- The `tool_call_parser` field is stored as a string
- Different parser values (`hermes`, `llama3_json`, `mistral`) are all accepted
- No validation errors on storage or retrieval

**Test Data**:
```json
[
  {"model_id": "granite-3.1-8b-instruct", "tool_call_parser": "hermes"},
  {"model_id": "llama-3.3-70b-instruct", "tool_call_parser": "llama3_json"},
  {"model_id": "mistral-7b-instruct-v0.3", "tool_call_parser": "mistral"}
]
```

**Notes**: To be filled later in the process.
