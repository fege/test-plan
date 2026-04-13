---
test_case_id: TC-AUDIT-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-AUDIT-002: Model without validated entry cannot display "Tool Calling Enabled" tag

**Objective**: Verify that a model without a validated tool-calling entry in the catalog cannot display the "Tool Calling Enabled" tag, ensuring the catalog is the single source of truth.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A model in the catalog without tool-calling metadata

**Test Steps**:
1. Identify a model in the catalog that does not have `tool_calling_supported: true` in its metadata
2. Navigate to the model in the RHOAI Catalog UI
3. Verify the model does NOT display a "Tool Calling Enabled" tag in the catalog listing
4. View the modelcard and verify no tool-calling indicators are present
5. Attempt to manually add a "Tool Calling" tag to the model (if the UI allows manual tagging)
6. Verify the system prevents tagging a model as tool-calling-enabled without validated catalog metadata, OR verify that the audit process would flag this inconsistency

**Expected Results**:
- Models without validated tool-calling metadata cannot display the "Tool Calling Enabled" tag
- The UI enforces consistency between catalog metadata and displayed tags
- No false positives where non-validated models appear as tool-calling capable

**Notes**: To be filled later in the process.
