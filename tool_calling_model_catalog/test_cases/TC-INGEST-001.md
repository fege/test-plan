---
test_case_id: TC-INGEST-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-001: Ingest single validated model with complete tool-calling metadata

**Objective**: Verify that a single validated model with all tool-calling metadata fields can be successfully ingested into the Model Catalog.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- Model Validation team output available (or synthetic test data conforming to schema)

**Test Steps**:
1. Prepare a model metadata payload with all required tool-calling fields populated
2. Submit the model entry to the ingestion pipeline
3. Verify the ingestion completes without errors
4. Query the Model Catalog database to confirm the model entry exists
5. Verify all tool-calling fields are stored with correct values

**Expected Results**:
- Model entry is created in the catalog with status indicating successful ingestion
- All five tool-calling fields are populated and match the submitted values
- Model is visible in the catalog after ingestion

**Test Data**:
```yaml
model_id: granite-3.1-8b-instruct
model_name: Granite 3.1 8B Instruct
tool_calling_supported: true
required_cli_args:
  - "--max-model-len"
  - "8192"
  - "--dtype"
  - "float16"
chat_template_path: "examples/tool_chat_template_granite.jinja"
chat_template_file_name: "tool_chat_template_granite.jinja"
tool_call_parser: "hermes"
```

**Validation**:
- Database query confirms all fields match the submitted payload
- BFF API returns the model with correct metadata

**Notes**: To be filled later in the process.
