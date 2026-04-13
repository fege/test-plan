---
test_case_id: TC-SCHEMA-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-001: Store tool_calling_supported boolean field in Model Catalog

**Objective**: Verify that the Model Catalog schema correctly stores and retrieves the `tool_calling_supported` boolean field for a model entry.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog database deployed and accessible
- Database schema migration applied with tool-calling fields

**Test Steps**:
1. Insert a model entry with `tool_calling_supported: true` into the Model Catalog database
2. Query the database to retrieve the stored value for the model entry
3. Verify the field value is `true` (boolean, not string)
4. Insert a second model entry with `tool_calling_supported: false`
5. Query the database and verify the field value is `false`

**Expected Results**:
- The `tool_calling_supported` field is persisted as a boolean type
- `true` and `false` values are stored and retrieved without type coercion issues
- No database errors on insert or query

**Validation**:
- Direct database query confirms field type is boolean
- `SELECT tool_calling_supported FROM model_catalog WHERE model_id = '<model_id>'` returns the correct boolean value

**Notes**: To be filled later in the process.
