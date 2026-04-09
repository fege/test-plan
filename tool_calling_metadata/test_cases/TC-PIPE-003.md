---
test_case_id: TC-PIPE-003
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-PIPE-003: Update existing model entry with new tool-calling metadata

**Objective**: Verify the ingestion pipeline can update an existing catalog entry with new or modified tool-calling metadata.

**Preconditions**:
- A model entry already exists in the catalog (e.g., granite-3.1-8b-instruct)
- The existing entry may or may not have tool-calling metadata

**Test Steps**:
1. Submit updated tool-calling metadata for an existing model to the ingestion pipeline
2. Verify the ingestion completes successfully
3. Query the catalog for the model
4. Verify the tool-calling metadata has been updated to the new values
5. Verify other existing metadata fields were not overwritten or lost

**Test Data**:
```json
{
  "model_name": "granite-3.1-8b-instruct",
  "model_version": "1.0",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "16384"],
  "chat_template_file_name": "tool_chat_template_granite_v2.jinja",
  "chat_template_path": "/opt/app-root/template/tool_chat_template_granite_v2.jinja",
  "tool_call_parser": "granite"
}
```

**Expected Results**:
- The catalog entry reflects the updated metadata values
- `required_cli_args` changed from `["--max-model-len", "8192"]` to `["--max-model-len", "16384"]`
- `chat_template_file_name` updated to `tool_chat_template_granite_v2.jinja`
- Existing non-tool-calling metadata fields remain unchanged

**Notes**: To be filled later in the process.
