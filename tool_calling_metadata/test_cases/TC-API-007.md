---
test_case_id: TC-API-007
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-007: Validate tag consistency for correctly tagged model

**Objective**: Verify that a model tagged as "Tool Calling Enabled" in the UI has a corresponding validated entry in the Catalog with complete metadata.

**Preconditions**:
- A model has been ingested with validated tool-calling metadata
- The model is tagged as "Tool Calling Enabled" in the UI

**Test Steps**:
1. Identify a model displayed as "Tool Calling Enabled" in the catalog UI
2. Query the Model Catalog API for the same model's metadata
3. Verify the catalog entry contains a validated tool-calling metadata set
4. Verify `tool_calling_supported` is `true` in the catalog entry
5. Verify all required tool-calling fields are populated (not null/empty)

**Expected Results**:
- The catalog entry for the UI-tagged model has `tool_calling_supported: true`
- All metadata fields (`required_cli_args`, `chat_template_file_name`, `chat_template_path`, `tool_call_parser`) are populated
- There is no mismatch between the UI tag and the catalog data

**Notes**: To be filled later in the process.
