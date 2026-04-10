---
test_case_id: TC-VER-002
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-VER-002: Update tool_call_parser for ModelCar image update

**Objective**: Verify the catalog correctly handles metadata updates when a ModelCar image update changes the required tool_call_parser value for a model.

**Preconditions**:
- A model exists in the catalog with `tool_call_parser: "llama3_json"`
- A simulated ModelCar image update requires changing the parser

**Test Steps**:
1. Confirm the existing model entry has `tool_call_parser` set to `llama3_json`
2. Submit an update via the ingestion pipeline changing `tool_call_parser` to `llama3_json_v2`
3. Verify the catalog entry is updated
4. Verify the API returns the updated parser value
5. Verify the modelcard displays the updated parser value

**Test Data**:
```json
{
  "model_name": "llama-3.1-70b-instruct",
  "model_version": "1.0",
  "tool_call_parser": "llama3_json_v2"
}
```

**Expected Results**:
- The catalog entry reflects `tool_call_parser: "llama3_json_v2"`
- The BFF API returns the new parser value
- Other tool-calling metadata fields remain unchanged
- The modelcard displays the updated parser value

**Notes**: To be filled later in the process.
