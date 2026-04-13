---
test_case_id: TC-INGEST-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-002: Ingest batch of validated tool-calling models from RHAISTRAT-1165

**Objective**: Verify that a batch of validated tool-calling models (minimum 3) from the RHAISTRAT-1165 initiative can be ingested together with correct metadata and proper tags.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- Batch of at least 3 validated model entries ready for ingestion

**Test Steps**:
1. Prepare a batch payload containing 3 validated models with different tool_call_parser values
2. Submit the batch to the ingestion pipeline
3. Verify all 3 models are successfully ingested without errors
4. Query the catalog and verify each model has correct tool-calling metadata
5. Verify each model has the appropriate tags applied (including "Tool Calling" tag)

**Expected Results**:
- All 3 models are ingested in a single batch operation
- Each model retains its distinct tool_call_parser, chat_template_path, and required_cli_args
- No cross-contamination of metadata between models
- All models are tagged correctly for UI filtering

**Test Data**:
```json
[
  {
    "model_id": "granite-3.1-8b-instruct",
    "tool_calling_supported": true,
    "tool_call_parser": "hermes",
    "chat_template_file_name": "tool_chat_template_granite.jinja",
    "chat_template_path": "examples/tool_chat_template_granite.jinja",
    "required_cli_args": ["--max-model-len", "8192"]
  },
  {
    "model_id": "llama-3.3-70b-instruct",
    "tool_calling_supported": true,
    "tool_call_parser": "llama3_json",
    "chat_template_file_name": "tool_chat_template_llama3.3_json.jinja",
    "chat_template_path": "examples/tool_chat_template_llama3.3_json.jinja",
    "required_cli_args": ["--max-model-len", "16384", "--dtype", "bfloat16"]
  },
  {
    "model_id": "mistral-7b-instruct-v0.3",
    "tool_calling_supported": true,
    "tool_call_parser": "mistral",
    "chat_template_file_name": "tool_chat_template_mistral.jinja",
    "chat_template_path": "examples/tool_chat_template_mistral.jinja",
    "required_cli_args": ["--max-model-len", "32768"]
  }
]
```

**Notes**: To be filled later in the process.
