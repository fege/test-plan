---
test_case_id: TC-SCHEMA-005
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-SCHEMA-005: Existing models without tool-calling fields remain functional after schema update

**Objective**: Verify that models ingested before the tool-calling schema enhancement continue to function correctly, with tool-calling fields defaulting to null or empty values.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog containing pre-existing models ingested before schema update
- Database schema migration applied with tool-calling fields

**Test Steps**:
1. Identify an existing model in the catalog that was ingested before the tool-calling schema update (e.g., a text-generation model without tool-calling support)
2. Query the database for the model's full record including new tool-calling fields
3. Verify that `tool_calling_supported` is `null` or `false` (not an error)
4. Verify that `required_cli_args`, `chat_template_path`, `chat_template_file_name`, and `tool_call_parser` are `null` or empty
5. Verify the model's existing fields (summary, description, tags, task) remain unchanged
6. Access the model via the BFF API and verify the response is valid JSON without errors

**Expected Results**:
- Pre-existing models are not broken by the schema migration
- New tool-calling fields default to safe null/empty values
- No data corruption or loss of existing metadata
- API responses for legacy models remain well-formed

**Notes**: To be filled later in the process.
