---
test_case_id: TC-AUDIT-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-AUDIT-001: Model with validated catalog entry shows "Tool Calling Enabled" tag

**Objective**: Verify that a model with a validated tool-calling entry in the catalog correctly displays the "Tool Calling Enabled" tag in the UI.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A model ingested with complete, validated tool-calling metadata via the ingestion pipeline

**Test Steps**:
1. Ingest a model (granite-3.1-8b-instruct) with complete tool-calling metadata through the validated ingestion pipeline
2. Navigate to the RHOAI Model Catalog UI
3. Locate the granite-3.1-8b-instruct model in the catalog listing
4. Verify the model displays a "Tool Calling Enabled" tag or equivalent indicator
5. Click on the model to view the modelcard
6. Verify the modelcard also shows the "Tool Calling Enabled" status
7. Query the BFF API and confirm `tool_calling_supported: true` matches the UI display

**Expected Results**:
- "Tool Calling Enabled" tag is visible in both catalog listing and modelcard views
- Tag presence is backed by validated metadata in the catalog database
- Tag and API data are consistent

**Notes**: To be filled later in the process.
