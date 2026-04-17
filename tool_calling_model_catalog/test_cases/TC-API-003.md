---
test_case_id: TC-API-003
strat_key: RHAISTRAT-1262
priority: P0
status: Automated
automation_status: Complete
last_updated: '2026-04-17'
---
# TC-API-003: Verify --enable-auto-tool-choice flag data in API response

**Objective**: Verify that the BFF API response includes the `--enable-auto-tool-choice` flag information so the Serving UI knows this flag is required for tool-calling deployment.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- A validated tool-calling model ingested with auto-tool-choice requirement

**Test Steps**:
1. Ingest a model with metadata indicating `--enable-auto-tool-choice` is required (either as part of `required_cli_args` or as a separate field)
2. Send a GET request to the BFF API for the model
3. Verify the response includes information about the `--enable-auto-tool-choice` flag
4. Verify the flag information is in a format consumable by the Serving UI
5. Verify a model without tool-calling support does NOT include this flag in its response

**Expected Results**:
- The `--enable-auto-tool-choice` flag is included in the tool-calling metadata
- The flag is distinguishable from model-specific CLI args (baseline args vs tool-calling-specific args)
- The Serving UI can programmatically determine when to include this flag in deployment commands

**Test Data**:
```json
{
  "model_id": "granite-3.1-8b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192"],
  "chat_template_path": "examples/tool_chat_template_granite.jinja",
  "tool_call_parser": "hermes"
}
```

**Notes**: To be filled later in the process.
