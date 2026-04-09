# Test Cases Index — Tool Calling Metadata Integration

**Test Plan**: [../TestPlan.md](../TestPlan.md)
**Strategy**: [RHAISTRAT-1262](https://redhat.atlassian.net/browse/RHAISTRAT-1262)

## Quick Stats

| Metric | Count |
|--------|-------|
| Total Test Cases | 28 |
| P0 (Critical) | 9 |
| P1 (High) | 15 |
| P2 (Medium) | 4 |

---

## API — Model Catalog BFF API Endpoints

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-API-001](TC-API-001.md) | Retrieve tool-calling metadata for a validated model | P0 |
| [TC-API-002](TC-API-002.md) | API response includes enable-auto-tool-choice flag context | P0 |
| [TC-API-003](TC-API-003.md) | Retrieve metadata for a model without tool-calling support | P1 |
| [TC-API-004](TC-API-004.md) | Retrieve metadata for a non-existent model returns appropriate error | P1 |
| [TC-API-005](TC-API-005.md) | List models filtered by Tool Calling task | P1 |
| [TC-API-006](TC-API-006.md) | API response is structured JSON consumable by Serving UI | P1 |
| [TC-API-007](TC-API-007.md) | Validate tag consistency for correctly tagged model | P2 |
| [TC-API-008](TC-API-008.md) | Detect inconsistency when model has UI tag but no validated catalog entry | P2 |

## DB — Database Operations

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-DB-001](TC-DB-001.md) | Store all tool-calling metadata fields for a model | P0 |
| [TC-DB-002](TC-DB-002.md) | Retrieve stored tool-calling metadata fields | P0 |
| [TC-DB-003](TC-DB-003.md) | Store metadata with multiple CLI arguments | P0 |
| [TC-DB-004](TC-DB-004.md) | Store metadata preserves downstream chat template path format | P0 |
| [TC-DB-005](TC-DB-005.md) | Store metadata with tool_calling_supported set to false | P1 |

## PIPE — Ingestion Pipeline Operations

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-PIPE-001](TC-PIPE-001.md) | Ingest validated model data with complete tool-calling metadata | P0 |
| [TC-PIPE-002](TC-PIPE-002.md) | Ingested model receives proper tags including Tool Calling task | P0 |
| [TC-PIPE-003](TC-PIPE-003.md) | Update existing model entry with new tool-calling metadata | P0 |
| [TC-PIPE-004](TC-PIPE-004.md) | Reject ingestion of model data with missing required fields | P1 |
| [TC-PIPE-005](TC-PIPE-005.md) | Ingest multiple validated models from a batch submission | P1 |

## UI — UI Components

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-UI-001](TC-UI-001.md) | Tool Calling filter appears in left navigation menu | P1 |
| [TC-UI-002](TC-UI-002.md) | Filter by Tool Calling task shows only TC-enabled models | P1 |
| [TC-UI-003](TC-UI-003.md) | Modelcard displays tool-calling CLI arguments and template path | P1 |
| [TC-UI-004](TC-UI-004.md) | Modelcard does not display TC fields for non-tool-calling models | P1 |
| [TC-UI-005](TC-UI-005.md) | Tool Calling Enabled tag is visible on catalog model cards | P1 |
| [TC-UI-006](TC-UI-006.md) | Copy tool-calling commands from modelcard | P2 |
| [TC-UI-007](TC-UI-007.md) | Existing catalog functionality remains intact after schema changes | P1 |

## VER — Versioning and Metadata Evolution

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-VER-001](TC-VER-001.md) | Update chat template path for new RHAIIS version | P1 |
| [TC-VER-002](TC-VER-002.md) | Update tool_call_parser for ModelCar image update | P1 |
| [TC-VER-003](TC-VER-003.md) | Multiple model versions with different template paths coexist | P2 |
