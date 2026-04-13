---
test_case_id: TC-CARD-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-CARD-004: Modelcard without tool-calling metadata renders without errors

**Objective**: Verify that a modelcard for a model without tool-calling support renders correctly without any errors or broken UI elements related to missing tool-calling fields.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A model ingested without tool-calling metadata (e.g., a text-generation-only model)

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Locate and click on a model without tool-calling support
3. Open the modelcard detail view
4. Verify the modelcard renders without JavaScript errors (check browser console)
5. Verify no empty or broken tool-calling sections appear on the card
6. Verify the modelcard's existing content (description, tags, other metadata) is displayed correctly

**Expected Results**:
- Modelcard renders cleanly without tool-calling section
- No placeholder text like "N/A" or "undefined" for tool-calling fields
- No console errors related to missing tool-calling metadata
- Model's existing metadata is unaffected

**Notes**: To be filled later in the process.
