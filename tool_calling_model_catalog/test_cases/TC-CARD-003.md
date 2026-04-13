---
test_case_id: TC-CARD-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-CARD-003: Modelcard shows --enable-auto-tool-choice and --tool-call-parser flags

**Objective**: Verify that the modelcard renders the `--enable-auto-tool-choice` flag and `--tool-call-parser` argument prominently so users know these are required for tool-calling deployments.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A tool-calling model ingested with tool_call_parser metadata

**Test Steps**:
1. Navigate to the modelcard for granite-3.1-8b-instruct
2. Verify the modelcard displays `--enable-auto-tool-choice` as a required flag for tool-calling
3. Verify the modelcard displays `--tool-call-parser hermes` (or the model-specific parser)
4. Verify these flags are visually distinct or grouped together as tool-calling requirements
5. Navigate to the modelcard for llama-3.3-70b-instruct
6. Verify the modelcard displays `--tool-call-parser llama3_json` (different parser for this model)

**Expected Results**:
- Both `--enable-auto-tool-choice` and `--tool-call-parser <parser>` are visible on the modelcard
- The parser value is model-specific and matches the ingested metadata
- The flags are clearly labeled as tool-calling deployment requirements

**Notes**: To be filled later in the process.
