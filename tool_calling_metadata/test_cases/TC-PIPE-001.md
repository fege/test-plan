---
test_case_id: TC-PIPE-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-PIPE-001: Ingest validated model data with complete tool-calling metadata

**Objective**: Verify the ingestion pipeline accepts validated model data from the Model Validation team and creates a complete catalog entry with all tool-calling metadata fields.

**Preconditions**:
- Ingestion pipeline is running and accessible
- Admin user has permissions to trigger ingestion

**Test Steps**:
1. Submit a validated model data payload to the ingestion pipeline containing all tool-calling metadata fields
2. Verify the ingestion completes successfully
3. Query the Model Catalog to confirm the model entry was created
4. Verify all tool-calling metadata fields are populated in the catalog entry

**Test Data**:
```json
{
  "model_name": "granite-3.1-8b-instruct",
  "model_version": "1.0",
  "category": "Other model",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192"],
  "chat_template_file_name": "tool_chat_template_granite.jinja",
  "chat_template_path": "/opt/app-root/template/tool_chat_template_granite.jinja",
  "tool_call_parser": "granite"
}
```

**Expected Results**:
- Ingestion pipeline returns a success status
- A new catalog entry exists for granite-3.1-8b-instruct
- All five tool-calling metadata fields are present and correctly populated
- The model is categorized under 'Other model'

**Validation**:
- Query the catalog database directly to confirm the entry matches the submitted payload

**Notes**: To be filled later in the process.
