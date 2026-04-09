---
feature: Tool Calling Metadata Integration
strat_key: RHAISTRAT-1262
version: 1.0.1
status: In Review
author: RHOAI QA Team
additional_docs:
- https://docs.google.com/document/d/1XaK-rZPZEexUrrIMkyLXzjQJYY-rKATdkEPE_NRTz5I/edit?usp=sharing
last_updated: '2026-04-09'
reviewers: []
---
# Tool Calling Metadata Integration Test Plan
**RHOAI QA Team – Model Catalog & Model Serving**

**Strategy**: [RHAISTRAT-1262](https://redhat.atlassian.net/browse/RHAISTRAT-1262)

---

## 1. Executive Summary

### 1.1 Purpose
This test plan covers the integration of validated Tool Calling metadata into the Model Catalog. This feature enables the Model Catalog to serve as the single source of truth for the RHOAI Serving UI and downstream deployment automation by storing validated CLI requirements and chat template paths for tool-calling models.

The Model Validation team confirms a model's compatibility and specific CLI requirements for RHAIIS, then this data is ingested into the Catalog with proper tags under the 'Other model' category. By storing metadata centrally, the feature enables dynamic UI configuration for the RHOAI Serving Wizard, ensures consistency with validated parameters, and supports versioning as RHAIIS and ModelCar images evolve. This improves scalability (adding models without code changes), accuracy (eliminating manual entry errors), and deployment reliability for tool-calling use cases, ultimately providing a seamless "one-click" deployment experience.

### 1.2 Scope

#### In Scope (RHOAI QA Team Responsibilities)
- Schema enhancement to store tool-calling CLI arguments (--enable-auto-tool-choice, --tool-call-parser, etc.) and chat template paths
- Ingestion pipeline to receive and update model entries with validation team's output
- API exposure via Model Catalog BFF to provide tool-calling attributes in structured JSON format
- UI integration: adding 'Tool Calling' task filter to left navigation menu
- Tool-calling data display within modelcards for supported models
- Tagging models with "Tool Calling Enabled" backed by validated Catalog entries
- Metadata fields: tool_calling_supported (boolean), required_cli_args (list), chat_template_file_name (string), chat_template_path (string), tool_call_parser (string)
- Sample validated models from initiative RHAISTRAT-1165

#### Out of Scope (Other Teams)
- UI automation for model deployment wizard (deferred to RHAIRFE-1254)
- Code changes to RHOAI Serving UI itself (this feature provides the API, not the UI implementation)

### 1.3 Test Objectives
1. Verify the Model Catalog database successfully stores all required tool-calling metadata fields (tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser) for each model version
2. Confirm the ingestion pipeline correctly processes validated model data from the Model Validation team and populates the Catalog with proper tags under 'Other model' category
3. Validate the Model Catalog BFF API returns tool-calling metadata in structured JSON format consumable by the RHOAI Serving UI
4. Verify the 'Tool Calling' task appears in the UI's left navigation filter and correctly filters models tagged with tool-calling support
5. Confirm modelcards display tool-calling CLI arguments and chat template paths for models that support tool calling
6. Ensure models tagged as "Tool Calling Enabled" in the UI have corresponding validated entries in the Catalog
7. Validate versioning support: changes to template locations or parser requirements are properly managed across RHAIIS and ModelCar image updates

---

## 2. Test Strategy

### 2.1 Test Levels
- **API Integration Testing** — Verify Model Catalog BFF API returns tool-calling metadata in structured JSON format that the RHOAI Serving UI can parse
- **Data Validation Testing** — Validate metadata schema can store CLI arguments (--enable-auto-tool-choice, --tool-call-parser), chat template paths, and boolean flags correctly
- **Functional Testing** — Test ingestion pipeline workflow, metadata display in model cards, and filtering by 'Tool Calling' task in UI
- **UI Testing** — Verify tool-calling metadata renders correctly in model cards, new 'Tool Calling' filter appears in left navigation, and models tagged as "Tool Calling Enabled" are backed by validated catalog entries

### 2.2 Test Types
- **Positive Testing** — Valid metadata ingestion for validated models, successful API retrieval of tool-calling attributes, correct display of CLI arguments in model cards
- **Negative Testing** — Models without tool-calling metadata don't show TC fields, invalid metadata formats are rejected, filtering excludes non-TC models
- **Boundary Testing** — Large sets of CLI arguments, multiple model versions with different template paths, edge cases in metadata schema fields
- **Regression Testing** — Existing Model Catalog functionality remains intact, non-TC models display correctly, current API consumers are not broken by schema changes

### 2.3 Test Priorities
- **P0 (Critical)** — Metadata schema can store and retrieve tool-calling fields; API returns structured JSON for validated models; ingestion pipeline successfully updates catalog entries
- **P1 (High)** — UI displays tool-calling metadata in model cards; 'Tool Calling' filter works in left navigation; only validated models are tagged as "Tool Calling Enabled"
- **P2 (Medium)** — Copy/paste functionality from model card works correctly; error handling for missing or malformed metadata; audit mechanism for source of truth validation

---

## 3. Test Environment

### 3.1 Test Cluster Configuration
- RHOAI cluster with Model Catalog component installed (version TBD - targeting RHOAI 3.4 based on RHAIRFE-1256)
- OpenShift version: TBD
- Model Serving component enabled
- AI Hub component enabled
- RHAIIS (Red Hat AI Inference Server) version: TBD
- ModelCar container images: TBD

### 3.2 Test Data Requirements
- Sample model metadata with tool-calling fields (JSON/YAML):
  - `tool_calling_supported: boolean`
  - `required_cli_args: list`
  - `chat_template_file_name: string`
  - `chat_template_path: string`
  - `tool_call_parser: string`
  - Flag: `--enable-auto-tool-choice`
- Validated tool-calling models from RHAISTRAT-1165 initiative (specific model names TBD pending Model Validation team output)
- Sample model entries tagged with 'Other model' category
- Sample model entries tagged with 'Tool Calling' task
- Mock Model Validation team output data (validated CLI arguments and chat template paths)
- Sample modelcard YAML files with frontmatter containing tool-calling commands

### 3.3 Test Users
- Admin user with permissions to update Model Catalog schema and ingest metadata
- RHOAI UI user with access to Model Catalog browsing and filtering
- API consumer user for Model Catalog API/BFF access
- RHOAI Serving Wizard user for model deployment testing
- RBAC roles for Model Catalog write access follow the same Model Registry RBAC model

---

## 4. Endpoints/Methods Under Test

| Endpoint/Method | Type | Purpose | Priority |
|-----------------|------|---------|----------|
| Model Catalog BFF API - Get Model Metadata | REST | Retrieve tool-calling metadata (JSON) for a specific model version | P0 |
| Model Catalog Database - Store Metadata | Database | Persist tool-calling fields (tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser) | P0 |
| Ingestion Pipeline - Upload Model Entry | Pipeline/API | Accept validated model data from Model Validation team and update Catalog entries | P0 |
| Model Catalog UI - Tool Calling Filter | UI Component | Display 'Tool Calling' task in left navigation and filter models by this tag | P1 |
| Modelcard Rendering - Tool Calling Section | UI Component | Display tool-calling CLI arguments and chat template paths within modelcard YAML frontmatter | P1 |
| Model Catalog API - List Models by Task | REST | Return filtered list of models tagged with 'Tool Calling' task | P1 |
| Model Catalog API - Validate Model Tag Consistency | API/Validation | Ensure "Tool Calling Enabled" UI tag corresponds to validated Catalog entry (supports Test Objective 6) | P2 |

---

## 5. Test Cases

**28 test cases** have been generated across 5 categories. See the complete index at [test_cases/INDEX.md](test_cases/INDEX.md).

**Test Cases Directory**: [test_cases/](test_cases/)
**Complete Test Case Index**: [test_cases/INDEX.md](test_cases/INDEX.md)

### 5.1 Test Case Organization

| Category | Test Cases | Priority Distribution |
|----------|------------|----------------------|
| TC-API (BFF API Endpoints) | 8 | 2 P0, 4 P1, 2 P2 |
| TC-DB (Database Operations) | 5 | 4 P0, 1 P1, 0 P2 |
| TC-PIPE (Ingestion Pipeline) | 5 | 3 P0, 2 P1, 0 P2 |
| TC-UI (UI Components) | 7 | 0 P0, 6 P1, 1 P2 |
| TC-VER (Versioning) | 3 | 0 P0, 2 P1, 1 P2 |
| **Total** | **28** | **9 P0, 15 P1, 4 P2** |

### 5.2 Test Case Naming Convention

Test cases follow the naming pattern: `TC-<CATEGORY>-<NUMBER>`

- **TC-API-xxx**: Model Catalog BFF API endpoints (GET metadata, list models by task, validate tag consistency)
- **TC-DB-xxx**: Database operations (store metadata, retrieve tool-calling fields, schema validation)
- **TC-PIPE-xxx**: Ingestion pipeline operations (upload model entry, update catalog with validated data)
- **TC-UI-xxx**: UI components (Tool Calling filter, modelcard rendering, tag display)
- **TC-VER-xxx**: Versioning and metadata evolution (template path changes, RHAIIS/ModelCar version updates)

---

## 6. Risks and Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Dependency on Model Validation team's output format and timing for validated model data (RHAISTRAT-1165) | High | High | Establish clear handoff contract and schema with Model Validation team; create sample test data for development and testing; set up automated validation of incoming metadata format |
| Schema changes to Model Catalog may break existing API consumers or downstream systems | High | Medium | Implement backwards-compatible schema extension; version the API if breaking changes are necessary; coordinate with RHOAI Serving UI team (RHAIRFE-1254) on integration testing |
| Inconsistency between UI tagging and actual validated catalog entries could mislead customers | High | Medium | Implement automated audit mechanism to verify "Tool Calling Enabled" tag is only applied to validated entries; add integration tests between catalog data and UI filtering |
| CLI argument changes in RHAIIS or ModelCar images over time may invalidate stored metadata | Medium | Medium | Implement versioning strategy for metadata tied to specific RHAIIS/ModelCar versions; establish process for Model Validation team to update metadata when images evolve |
| Temporary copy/paste solution from model card may have poor UX until automation (RHAIRFE-1254) is delivered | Medium | High | Ensure model card rendering includes clear formatting and instructions for copying CLI arguments; plan for smooth transition to automated wizard integration |

---

## 7. Test Environment Requirements

### 7.1 Infrastructure
- Model Catalog database (PostgreSQL, to be confirmed during environment setup)
- Model Catalog BFF (Backend-for-Frontend) API service
- RHOAI Serving UI component
- Model Validation team testing suite integration endpoint (external dependency)
- Storage for model artifacts and chat templates (to be specified during environment setup)

### 7.2 Configuration
- Model Catalog schema definition files (for tool-calling metadata fields)
- Model Catalog API endpoint configuration
- RHOAI UI catalog filter configuration (to add 'Tool Calling' task)
- Ingestion pipeline configuration for Model Validation team data
- TBD: Environment variables for API endpoints
- TBD: Feature flags for tool-calling metadata display

### 7.3 Test Tools
- API testing tools (curl, httpie, or Postman) for Model Catalog BFF API validation
- Database query tools (psql or appropriate DB client) for schema and data verification
- oc/kubectl for cluster and operator inspection
- Browser developer tools for UI catalog filtering and metadata display testing
- JSON/YAML validation tools for metadata format verification
- TBD: Performance testing tools for catalog query performance with new metadata

---

## 8. Appendix

### 8.1 Test Case Summary

| Category | Total | P0 | P1 | P2 |
|----------|-------|----|----|-----|
| TC-API | 8 | 2 | 4 | 2 |
| TC-DB | 5 | 4 | 1 | 0 |
| TC-PIPE | 5 | 3 | 2 | 0 |
| TC-UI | 7 | 0 | 6 | 1 |
| TC-VER | 3 | 0 | 2 | 1 |
| **Total** | **28** | **9** | **15** | **4** |

### 8.2 Endpoint Coverage

| Endpoint | Test Cases | Coverage |
|----------|------------|----------|
| Model Catalog BFF API - Get Model Metadata | TC-API-001, TC-API-002, TC-API-003, TC-API-004, TC-API-006 | |
| Model Catalog Database - Store Metadata | TC-DB-001, TC-DB-002, TC-DB-003, TC-DB-004, TC-DB-005 | |
| Ingestion Pipeline - Upload Model Entry | TC-PIPE-001, TC-PIPE-002, TC-PIPE-003, TC-PIPE-004, TC-PIPE-005 | |
| Model Catalog UI - Tool Calling Filter | TC-UI-001, TC-UI-002, TC-UI-007 | |
| Modelcard Rendering - Tool Calling Section | TC-UI-003, TC-UI-004, TC-UI-005, TC-UI-006 | |
| Model Catalog API - List Models by Task | TC-API-005 | |
| Model Catalog API - Validate Model Tag Consistency | TC-API-007, TC-API-008 | |

### 8.3 Document Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1 | 2026-04-08 | Initial test plan |
| 1 | 2026-04-08 | Generated 28 test cases across 5 categories (9 P0, 15 P1, 4 P2) |

---

**End of Test Plan**
