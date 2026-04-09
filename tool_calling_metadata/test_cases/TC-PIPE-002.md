---
test_case_id: TC-PIPE-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-PIPE-002: Ingested model receives proper tags including Tool Calling task

**Objective**: Verify that when a tool-calling model is ingested, it receives proper tags including the 'Other model' category and 'Tool Calling' task tag.

**Preconditions**:
- Ingestion pipeline is running
- A model with `tool_calling_supported: true` is submitted for ingestion

**Test Steps**:
1. Submit a validated tool-calling model to the ingestion pipeline
2. Query the catalog for the ingested model
3. Verify the model is tagged with 'Other model' category
4. Verify the model is tagged with 'Tool Calling' task
5. Verify the model appears when filtering by the 'Tool Calling' task

**Expected Results**:
- The model entry has the 'Other model' category tag
- The model entry has the 'Tool Calling' task tag
- The model appears in filtered results when querying by 'Tool Calling' task
- Both tags are applied automatically during ingestion without manual intervention

**Notes**: To be filled later in the process.
