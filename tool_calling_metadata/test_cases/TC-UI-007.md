---
test_case_id: TC-UI-007
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-007: Existing catalog functionality remains intact after schema changes

**Objective**: Verify that existing Model Catalog UI features (search, non-TC filters, model listing, pagination) continue to function correctly after the tool-calling metadata schema extension.

**Preconditions**:
- RHOAI UI is accessible with updated Model Catalog containing tool-calling metadata
- Catalog contains a mix of tool-calling and non-tool-calling models

**Test Steps**:
1. Navigate to the Model Catalog page
2. Verify the default model listing loads without errors
3. Test existing filters (non-TC filters) and verify they still work
4. Search for a non-tool-calling model and verify results are correct
5. Open a non-tool-calling model's modelcard and verify it renders correctly
6. Verify pagination (if applicable) works with the updated catalog

**Expected Results**:
- Default catalog listing loads normally with no errors
- Existing filters continue to function as before
- Search functionality returns correct results for non-TC models
- Non-TC modelcards render correctly without any layout issues caused by the TC schema extension
- No regression in catalog performance or UI responsiveness

**Notes**: To be filled later in the process.
