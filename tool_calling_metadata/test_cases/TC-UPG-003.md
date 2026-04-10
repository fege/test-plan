---
test_case_id: TC-UPG-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-09'
---
# TC-UPG-003: Ingestion pipeline and API function correctly after RHOAI upgrade

**Objective**: Verify that the ingestion pipeline can accept new tool-calling metadata and the BFF API continues to serve requests correctly after a RHOAI platform upgrade.

**Preconditions**:
- RHOAI platform has been upgraded successfully (TC-UPG-001 and TC-UPG-002 completed)
- Ingestion pipeline endpoint is accessible
- BFF API is responding

**Test Steps**:
1. Submit a new model entry with complete tool-calling metadata via the ingestion pipeline post-upgrade
2. Verify the ingestion completes successfully and the model appears in the catalog
3. Query the BFF API for the newly ingested model's tool-calling metadata
4. Verify the API response includes all tool-calling fields in the expected JSON format
5. Update an existing model's tool-calling metadata via the ingestion pipeline
6. Verify the update is reflected in the API response and UI modelcard
7. Verify the 'Tool Calling' filter includes the newly ingested model

**Test Data**:
```json
{
  "model_name": "post-upgrade-test-model",
  "model_version": "1.0",
  "tool_calling_supported": true,
  "required_cli_args": ["--enable-auto-tool-choice", "--tool-call-parser", "hermes"],
  "chat_template_file_name": "tool_chat_template_hermes.jinja",
  "chat_template_path": "/opt/app-root/template/tool_chat_template_hermes.jinja",
  "tool_call_parser": "hermes"
}
```

**Expected Results**:
- New model ingestion succeeds post-upgrade without errors
- BFF API returns complete tool-calling metadata for the new model
- Metadata updates to existing models are applied correctly
- UI displays the new model with tool-calling fields in the modelcard
- 'Tool Calling' filter includes the newly ingested model

**Notes**: To be filled later in the process.
