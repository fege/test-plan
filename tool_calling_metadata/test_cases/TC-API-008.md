---
test_case_id: TC-API-008
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-008: Detect inconsistency when model has UI tag but no validated catalog entry

**Objective**: Verify the system identifies inconsistency when a model is tagged as "Tool Calling Enabled" in the UI but lacks a validated catalog entry.

**Preconditions**:
- A model exists in the catalog without validated tool-calling metadata (tool_calling_supported is false or missing)
- The model has been manually or erroneously tagged as "Tool Calling Enabled" in the UI

**Test Steps**:
1. Identify a model that is displayed as "Tool Calling Enabled" in the UI
2. Query the Model Catalog API for the same model's catalog entry
3. Verify the catalog entry does NOT have `tool_calling_supported: true`
4. Verify the audit mechanism flags this inconsistency

**Expected Results**:
- The catalog entry shows `tool_calling_supported` as `false` or absent
- The audit or validation mechanism identifies and flags the mismatch
- The inconsistency is detectable either through an API validation endpoint or a reconciliation process

**Notes**: To be filled later in the process.
