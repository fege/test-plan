---
test_case_id: TC-PIPE-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-PIPE-004: Reject ingestion of model data with missing required fields

**Objective**: Verify the ingestion pipeline rejects model data submissions that are missing required tool-calling metadata fields when tool_calling_supported is true.

**Test Steps**:
1. Submit model data with `tool_calling_supported: true` but missing the `tool_call_parser` field
2. Verify the ingestion pipeline rejects the submission with an appropriate error
3. Verify no partial entry is created in the catalog

**Test Data**:
```json
{
  "model_name": "incomplete-model-v1",
  "model_version": "1.0",
  "category": "Other model",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192"],
  "chat_template_file_name": "tool_chat_template.jinja",
  "chat_template_path": "/opt/app-root/template/tool_chat_template.jinja"
}
```

**Expected Results**:
- Ingestion pipeline returns an error indicating missing required field `tool_call_parser`
- No catalog entry is created for `incomplete-model-v1`
- Error message clearly identifies which field is missing

**Notes**: To be filled later in the process.
