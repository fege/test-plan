---
test_case_id: TC-INGEST-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-005: Ingest model with partial tool-calling metadata

**Objective**: Verify the ingestion pipeline's behavior when a model is submitted with only some tool-calling fields populated (e.g., tool_calling_supported is true but chat_template_path is missing).

**Test Steps**:
1. Prepare a model metadata payload with `tool_calling_supported: true` but `chat_template_path` and `chat_template_file_name` omitted
2. Submit the model to the ingestion pipeline
3. Observe whether the ingestion succeeds with a warning or is rejected with a validation error
4. If accepted, verify the model entry in the database has null values for the missing fields
5. If rejected, verify the error message identifies the missing required fields

**Expected Results**:
- The ingestion pipeline either:
  - Accepts the partial entry with warnings and stores null for missing fields, OR
  - Rejects the entry with a clear validation error listing missing required fields
- In either case, no partial or corrupted data is written to the catalog

**Test Data**:
```json
{
  "model_id": "granite-3.0-2b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "4096"],
  "tool_call_parser": "hermes"
}
```

**Notes**: To be filled later in the process.
