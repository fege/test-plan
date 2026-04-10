---
test_case_id: TC-PIPE-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-PIPE-005: Ingest multiple validated models from a batch submission

**Objective**: Verify the ingestion pipeline can handle a batch of validated tool-calling models from the Model Validation team's testing suite output.

**Preconditions**:
- Ingestion pipeline is running
- Multiple validated model entries are prepared

**Test Steps**:
1. Submit a batch of three validated tool-calling models to the ingestion pipeline
2. Verify all three models are ingested successfully
3. Query the catalog to confirm all three entries were created
4. Verify each model has its unique tool-calling metadata correctly stored

**Test Data**:
```json
[
  {
    "model_name": "granite-3.1-8b-instruct",
    "tool_calling_supported": true,
    "required_cli_args": ["--max-model-len", "8192"],
    "chat_template_file_name": "tool_chat_template_granite.jinja",
    "chat_template_path": "/opt/app-root/template/tool_chat_template_granite.jinja",
    "tool_call_parser": "granite"
  },
  {
    "model_name": "llama-3.1-70b-instruct",
    "tool_calling_supported": true,
    "required_cli_args": ["--max-model-len", "32768", "--tensor-parallel-size", "4"],
    "chat_template_file_name": "tool_chat_template_llama3.1_json.jinja",
    "chat_template_path": "/opt/app-root/template/tool_chat_template_llama3.1_json.jinja",
    "tool_call_parser": "llama3_json"
  },
  {
    "model_name": "mistral-7b-instruct-v0.3",
    "tool_calling_supported": true,
    "required_cli_args": ["--max-model-len", "8192"],
    "chat_template_file_name": "tool_chat_template_mistral.jinja",
    "chat_template_path": "/opt/app-root/template/tool_chat_template_mistral.jinja",
    "tool_call_parser": "mistral"
  }
]
```

**Expected Results**:
- All three models are successfully ingested
- Each model has unique, correct tool-calling metadata
- Each model is tagged with 'Tool Calling' task
- No data mixing between model entries

**Notes**: To be filled later in the process.
