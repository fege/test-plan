---
test_case_id: TC-INGEST-003
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-003: Verify ingested model tagged under 'Other model' category

**Objective**: Verify that a tool-calling model ingested into the catalog is correctly categorized under 'Other model' and tagged with the appropriate tool-calling tag.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- At least one model successfully ingested with `tool_calling_supported: true`

**Test Steps**:
1. Ingest a validated tool-calling model into the Model Catalog
2. Query the catalog for the model's category assignment
3. Verify the model is categorized under 'Other model'
4. Verify the model has a "Tool Calling" tag or equivalent label applied
5. Access the RHOAI Catalog UI and confirm the model appears under the 'Other model' section

**Expected Results**:
- Model is categorized under 'Other model' category as specified in the strategy
- Tool-calling tag is applied to the model entry
- Model is discoverable in the UI under the correct category

**Notes**: To be filled later in the process.
