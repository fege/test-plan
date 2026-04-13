---
test_case_id: TC-REG-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-REG-003: Existing modelcard display unaffected by schema changes

**Objective**: Verify that modelcards for pre-existing models (without tool-calling metadata) continue to render correctly after the schema update.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Pre-existing models in the catalog that were ingested before the tool-calling schema update

**Test Steps**:
1. Navigate to the modelcard for a pre-existing model (e.g., flan-t5-small)
2. Verify all existing sections render correctly (description, tags, model details)
3. Verify no empty or broken tool-calling sections appear
4. Verify no "undefined", "null", or error indicators for tool-calling fields
5. Compare the modelcard layout with the expected layout from before the schema update
6. Check the browser console for any JavaScript errors during rendering

**Expected Results**:
- Pre-existing modelcards render identically to before the schema update
- No visual artifacts from missing tool-calling fields
- No JavaScript errors in the browser console
- Model metadata is intact and correctly displayed

**Notes**: To be filled later in the process.
