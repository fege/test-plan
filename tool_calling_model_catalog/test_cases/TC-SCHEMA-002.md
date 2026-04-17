---
test_case_id: TC-SCHEMA-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-002: Store required_cli_args list field in Model Catalog

**Objective**: Verify that the Model Catalog schema correctly stores and retrieves the `required_cli_args` list field containing CLI arguments needed to run a model.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog database deployed and accessible
- Database schema migration applied with tool-calling fields

**Test Steps**:
1. Insert a model entry with the following `required_cli_args` list:
   ```json
   ["--max-model-len", "8192", "--dtype", "float16"]
   ```
2. Query the database to retrieve the stored `required_cli_args` for the model
3. Verify the returned value is a list with 4 elements in the correct order
4. Verify each element is preserved as a string

**Expected Results**:
- The `required_cli_args` field is stored as a list/array type
- All list elements are preserved in order without truncation
- String values within the list are not modified or escaped

**Test Data**:
```json
{
  "model_id": "granite-3.1-8b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192", "--dtype", "float16"]
}
```

**Validation**:
- Direct database query confirms the list contains exactly 4 elements
- JSON array roundtrip preserves order and values

**Notes**: To be filled later in the process.
