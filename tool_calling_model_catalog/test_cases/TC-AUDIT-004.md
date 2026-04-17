---
test_case_id: TC-AUDIT-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-AUDIT-004: Audit identifies inconsistencies between tags and catalog entries

**Objective**: Verify that the source of truth audit process can detect and report models that are tagged as "Tool Calling Enabled" in the UI but lack validated metadata in the catalog.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- An audit mechanism or report is available for validating tag-metadata consistency

**Test Steps**:
1. Ingest a model with complete tool-calling metadata (valid state)
2. Manually create an inconsistent state: apply the "Tool Calling Enabled" tag to a model that does NOT have validated tool-calling metadata (if possible via direct DB manipulation or admin API)
3. Run the source of truth audit process
4. Verify the audit report identifies the inconsistency (model tagged without validated metadata)
5. Verify the audit report includes the model ID and the nature of the inconsistency
6. Verify the valid model (from step 1) passes the audit without issues

**Expected Results**:
- Audit detects the tag-metadata mismatch
- Report includes actionable details: model ID, missing fields, recommendation
- Valid models pass the audit without false positives
- Audit does not modify data -- it only reports findings

**Notes**: To be filled later in the process.
