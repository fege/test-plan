---
feature: tool_calling_model_catalog
strat_key: RHAISTRAT-1262
version: 1.0.0
status: In Review
author: RHOAI AI Hub
additional_docs:
- https://docs.google.com/document/d/1XaK-rZPZEexUrrIMkyLXzjQJYY-rKATdkEPE_NRTz5I/edit
- https://docs.google.com/document/d/1LYXSH8OsTy8SMwrq2Y3g5kjMqp09Moy1cAYBoZ4fD-k/edit
last_updated: '2026-04-13'
reviewers: []
---
# Tool Calling Model Catalog Test Plan
**RHOAI AI Hub -- Tool Calling Metadata Integration Testing**

**Strategy**: [RHAISTRAT-1262](https://redhat.atlassian.net/browse/RHAISTRAT-1262)

---

## 1. Executive Summary

### 1.1 Purpose

This test plan covers the integration of validated Tool Calling metadata into the RHOAI Model Catalog (Dev Preview, RHOAI 3.4). The feature extends the Model Catalog schema with tool-calling-specific fields (such as `tool_calling_supported`, `required_cli_args`, `chat_template_path`, and `tool_call_parser`), exposes this metadata via the BFF API for the RHOAI Serving Wizard, and adds UI capabilities for filtering and displaying tool-calling information on modelcards.

The goal is to establish the Model Catalog as the single source of truth for tool-calling-enabled models, replacing hardcoded UI values with dynamic, versioned metadata verified by the Model Validation team. Testing validates the full data lifecycle -- from ingestion of validated model metadata, through API exposure, to UI rendering and filtering -- ensuring customers can reliably discover and deploy tool-calling models.

### 1.2 Scope

#### In Scope (RHOAI AI Hub Responsibilities)
- Extending the Model Catalog schema to include tool-calling-specific fields (tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser)
- Ingesting validated tool-calling metadata provided by the Model Validation team into the Model Catalog
- Tagging tool-calling-enabled models under the 'Other model' category
- Rendering tool-calling commands in YAML frontmatter within modelcards for manual copy-paste (temporary workaround)
- Exposing tool-calling metadata via the Model Catalog BFF API in JSON format for consumption by the RHOAI Serving Wizard
- Auditing and ensuring models tagged as "Tool Calling Enabled" in the UI are backed by validated Catalog entries
- Adding a 'Tool Calling' task filter to the left-hand navigation menu in the RHOAI Catalog UI
- Supporting both upstream (`examples/<template_file_name>`) and downstream (`opt/app-root/template/<template_file_name>`) chat template paths
- Handling the `--enable-auto-tool-choice` flag and `--tool-call-parser` argument requirements

#### Out of Scope (Other Teams)
- Direct integration with the RHOAI Serving Wizard to auto-populate deployment parameters (covered by RHAIRFE-1254)
- Model validation testing itself (performed by Model Validation team under RHAISTRAT-1165)
- Changes to RHAIIS or ModelCar image internals
- Manual configuration workflows beyond the temporary copy-paste solution

### 1.3 Test Objectives

1. Verify that the Model Catalog schema accepts and correctly stores all required tool-calling metadata fields (tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser) for a model entry
2. Confirm successful ingestion of a sample set of validated tool-calling models from RHAISTRAT-1165 with correct metadata, proper tags, and categorization under 'Other model'
3. Validate that the Model Catalog BFF API returns tool-calling metadata in a structured JSON format that includes all required fields for a given model
4. Ensure that the 'Tool Calling' task filter appears in the left-hand navigation menu and correctly filters models tagged with tool-calling support
5. Verify that modelcards display tool-calling commands in YAML frontmatter in a user-readable, copy-paste-friendly format
6. Confirm that only models with validated tool-calling entries in the Catalog can be tagged as "Tool Calling Enabled" in the UI (source of truth audit)
7. Test that both upstream and downstream chat template path formats are correctly stored and retrievable via the API

---

## 2. Test Strategy

### 2.1 Test Levels
- **API Integration Testing** -- Validate that the Model Catalog BFF API correctly exposes tool-calling metadata fields in structured JSON format
- **Data Validation Testing** -- Verify correct ingestion, storage, and retrieval of tool-calling metadata (CLI arguments, chat template paths, parser settings) in the Model Catalog database
- **Functional Testing** -- Test catalog filtering by Tool Calling task, metadata rendering in modelcards, and tagging logic for tool-calling enabled models
- **UI Testing** -- Verify Tool Calling filter appears in left navigation, models display correct metadata in cards, and copy-paste functionality works for CLI arguments

### 2.2 Test Types
- **Positive Testing** -- Validate successful ingestion of validated models with complete tool-calling metadata, correct API responses, UI filtering, and modelcard rendering
- **Negative Testing** -- Test handling of incomplete metadata, invalid CLI arguments, missing chat template paths, and models incorrectly tagged as tool-calling enabled
- **Boundary Testing** -- Validate behavior with maximum number of tool-calling models in catalog, long CLI argument strings, and edge cases in chat template path formats (upstream vs downstream)
- **Regression Testing** -- Ensure existing Model Catalog functionality (search, filtering by other tasks, modelcard display) remains intact after schema updates

### 2.3 Test Priorities
- **P0 (Critical)** -- Core metadata schema functionality (BFF API returns tool-calling fields), successful ingestion of validated models from RHAISTRAT-1165, and Tool Calling filter operational in UI
- **P1 (High)** -- Accurate rendering of CLI arguments in modelcards, correct tagging audit (only validated models tagged), and API data structure matches UI parsing requirements
- **P2 (Medium)** -- UI refinements for copy-paste experience, comprehensive error handling for invalid metadata, and edge case handling for template path variations

---

## 3. Test Environment

### 3.1 Test Cluster Configuration
- OpenShift cluster with RHOAI 3.4 installed (Dev Preview release)
- RHOAI AI Hub component enabled
- RHOAI Model Serving component enabled
- ModelCar operator/images (version confirmed to support both upstream and downstream chat template paths; specific version to be pinned once RHAIIS compatibility matrix is finalized)
- Model Catalog BFF API deployed and accessible
- RHOAI Serving UI deployed and accessible

### 3.2 Test Data Requirements
- Sample model metadata YAML files with tool-calling specific frontmatter fields (tool_calling_supported, required_cli_args, chat_template_file_name, chat_template_path, tool_call_parser)
- Validated tool-calling models from RHAISTRAT-1165 initiative: minimum test data set of 3 validated models with complete tool-calling metadata, provided by Model Validation team or substituted with synthetic test entries conforming to the schema
- Sample JSON payloads for Model Catalog API with tool-calling metadata structure
- Chat template files for testing both upstream and downstream paths:
  - Upstream format: `examples/<template_file_name>`
  - Downstream format: `opt/app-root/template/<template_file_name>`
- Sample CLI argument configurations including:
  - `--enable-auto-tool-choice`
  - `--tool-call-parser` variations
  - Required CLI args to run models without tool calling (baseline)
- Mock Model Validation team outputs (validated model entries with tool-calling parameters)

### 3.3 Test Users
- RHOAI admin user (for Model Catalog management and ingestion pipeline operations)
- RHOAI data scientist user (for accessing Model Catalog UI and Serving Wizard)
- Service account with permissions to query Model Catalog BFF API
- Anonymous/unauthenticated user (to verify catalog browsing and filtering without deployment permissions)

---

## 4. API Endpoints / Methods Under Test

| Endpoint/Method | Type | Purpose | Priority |
|-----------------|------|---------|----------|
| Model Catalog BFF API (model metadata endpoint) | REST | Return tool-calling metadata in JSON format for a specific model | P0 |
| Model Catalog schema (database fields) | Config | Store tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser | P0 |
| Model ingestion pipeline (validation team handoff) | Method/Process | Ingest validated tool-calling metadata into the Catalog | P0 |
| Model tagging logic (UI audit) | Method | Ensure "Tool Calling Enabled" tag is backed by validated Catalog entry | P0 |
| RHOAI Catalog UI -- 'Tool Calling' task filter | UI | Filter models by tool-calling support in left-hand navigation | P1 |
| Modelcard rendering (YAML frontmatter) | UI | Display tool-calling commands for copy-paste | P1 |
| Chat template path resolution logic | Method/Process | Validate correct template path returned based on upstream vs downstream format | P1 |

---

## 5. Test Cases

> **42 test cases generated** across 8 categories. See the full index for details.

**Test Cases Directory**: [test_cases/](test_cases/)
**Complete Test Case Index**: [test_cases/INDEX.md](test_cases/INDEX.md)

### 5.1 Test Case Organization

| Category | Test Cases | Priority Distribution |
|----------|------------|----------------------|
| TC-SCHEMA | 7 | P0: 5, P1: 1, P2: 1 |
| TC-INGEST | 6 | P0: 3, P1: 2, P2: 1 |
| TC-API | 7 | P0: 3, P1: 3, P2: 1 |
| TC-FILTER | 5 | P0: 2, P1: 2, P2: 1 |
| TC-CARD | 5 | P0: 0, P1: 4, P2: 1 |
| TC-AUDIT | 4 | P0: 2, P1: 2, P2: 0 |
| TC-REG | 4 | P0: 0, P1: 4, P2: 0 |
| TC-E2E | 4 | P0: 4, P1: 0, P2: 0 |
| **Total** | **42** | **P0: 19, P1: 18, P2: 5** |

### 5.2 Test Case Naming Convention

Test cases follow the naming pattern: `TC-<CATEGORY>-<NUMBER>`

- **TC-SCHEMA** -- Model Catalog schema enhancement and metadata field validation
- **TC-INGEST** -- Ingestion pipeline and data import from Model Validation team
- **TC-API** -- BFF API endpoint responses and JSON structure
- **TC-FILTER** -- UI catalog filtering by Tool Calling task
- **TC-CARD** -- Modelcard rendering and YAML frontmatter display
- **TC-AUDIT** -- Source of truth audit and tag validation
- **TC-REG** -- Regression testing for existing catalog functionality
- **TC-E2E** -- End-to-end scenarios across ingestion, API, and UI

---

## 6. E2E Test Scenarios

End-to-end scenarios that validate the user journeys defined in the strategy. Each scenario maps to one or more TC-E2E-*.md test cases generated by `/test-plan.create-cases`.

> **Requirement**: At least one E2E scenario MUST be generated for each P0 endpoint in Section 4.
> E2E scenarios will be filled by `/test-plan.create-cases`.

### 6.1 Scenario Summary

| ID | Scenario | Endpoints Covered | Priority |
|----|----------|-------------------|----------|
| TC-E2E-001 | Full model ingestion to API retrieval lifecycle | BFF API, Schema, Ingestion pipeline | P0 |
| TC-E2E-002 | Model tagging audit and validation flow | Tagging logic, Ingestion pipeline | P0 |
| TC-E2E-003 | Catalog discovery and modelcard viewing flow | Tool Calling filter, Modelcard rendering, BFF API | P0 |
| TC-E2E-004 | Schema backwards compatibility with existing models | Schema, BFF API | P0 |

### 6.2 E2E Coverage Matrix

| Endpoint (from Section 4) | E2E Scenarios |
|----------------------------|---------------|
| Model Catalog BFF API (model metadata endpoint) | TC-E2E-001, TC-E2E-003, TC-E2E-004 |
| Model Catalog schema (database fields) | TC-E2E-001, TC-E2E-004 |
| Model ingestion pipeline (validation team handoff) | TC-E2E-001, TC-E2E-002 |
| Model tagging logic (UI audit) | TC-E2E-002 |
| RHOAI Catalog UI -- 'Tool Calling' task filter | TC-E2E-003 |
| Modelcard rendering (YAML frontmatter) | TC-E2E-003 |
| Chat template path resolution logic | TC-E2E-001 |

---

## 7. Non-Functional Requirements

Each category below must be explicitly addressed. If a category does not apply to this feature, state **Not Applicable** with a brief justification.

### 7.1 Disconnected/Air-Gapped

**Not Applicable** -- This feature focuses on metadata storage and retrieval within the Model Catalog. While the models themselves may be deployed in disconnected environments, the catalog metadata integration does not introduce new external registry dependencies or runtime image pulls. The chat template paths reference locations within RHAIIS/ModelCar images already deployed.

### 7.2 Upgrade/Migration

Testing must validate:
- **Schema evolution compatibility** -- Existing modelcards without tool-calling metadata must continue to function after schema enhancement
- **Backwards compatibility** -- Models added before tool-calling metadata fields existed should not break catalog API responses or UI rendering
- **Version-specific template paths** -- Ensure chat_template_path correctly distinguishes between upstream (`examples/<template_file_name>`) and downstream (`opt/app-root/template/<template_file_name>`) locations as RHAIIS and ModelCar image versions evolve
- **Metadata update workflow** -- Test ability to update tool-calling metadata for existing models when validation team provides new CLI requirements

### 7.3 Performance/Scalability

Testing must validate:
- **API response time** -- BFF API returns tool-calling metadata within acceptable latency when Serving UI queries model details (target: <500ms for single model lookup)
- **Catalog UI rendering** -- Filtering by Tool Calling task and rendering modelcards with embedded CLI arguments should not degrade UI responsiveness with large model portfolios (test with 50+ models)
- **Database query efficiency** -- Metadata retrieval should scale as the number of tool-calling enabled models grows over multiple releases

### 7.4 RBAC/Authorization

**Not Applicable** -- The strategy does not indicate new authorization boundaries for accessing tool-calling metadata. The Model Catalog BFF already enforces RBAC for model metadata access; those existing controls apply to the new tool-calling fields without additional testing scope.

---

## 8. Risks and Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Dependency on Model Validation team handoff timing and format of CLI arguments | High | Medium | Establish clear schema contract early, request sample data from validation team during test planning phase, automate validation of ingestion format |
| Chat template path differences between upstream and downstream images may cause deployment failures if metadata is incorrect | High | Medium | Test both upstream and downstream path formats explicitly, validate against actual RHAIIS/ModelCar image contents, document path resolution logic |
| UI parsing of BFF API JSON structure may fail if schema is not aligned between backend and frontend teams | High | Medium | Define API contract early with both Model Catalog and Serving UI teams, include API response validation in integration tests, perform end-to-end UI wizard testing |
| Manual copy-paste from modelcard (temporary solution) introduces user error risk until RHAIRFE-1254 automation is delivered | Medium | High | Provide clear modelcard formatting, add validation examples in test data, document known limitations of Dev Preview implementation |
| Inconsistent tagging of models as "Tool Calling Enabled" could mislead customers if validation process is incomplete | High | Medium | Implement automated audit process to verify all tagged models have complete validated metadata, include negative test cases for incorrectly tagged models |
| Schema changes to Model Catalog database could break existing integrations or queries | Medium | Low | Test backwards compatibility with existing modelcards, validate that non-tool-calling models still render correctly, perform regression testing on all catalog API endpoints |
| Model Catalog BFF API contract not yet finalized between backend and frontend teams | High | Medium | Track API specification progress as a dependency, use mock API responses for initial test development, validate contract alignment before E2E testing |

---

## 9. Test Environment Requirements

### 9.1 Infrastructure
- Single OpenShift cluster (sufficient for Dev Preview testing)
- Model Catalog database (PostgreSQL or equivalent -- storage for enhanced metadata schema)
- Model Catalog BFF API service endpoint
- RHOAI Serving Wizard UI endpoint
- Container registry access (for ModelCar images and validated models)
- Model Validation team's testing suite output (external dependency -- handoff mechanism TBD)

### 9.2 Configuration
- Model Catalog schema migration/update scripts (to support new tool-calling fields)
- Environment variables for Model Catalog BFF API endpoint
- RHOAI Serving Wizard configuration pointing to Model Catalog API
- Catalog source configuration for RHOAI 3.4 operators
- Feature flags for Dev Preview functionality (if applicable)
- Model Catalog UI left navigation configuration (to add 'Tool Calling' task filter)

### 9.3 Test Tools
- API testing tools: `curl`, `httpie`, or Postman (for Model Catalog BFF API validation)
- Kubernetes CLI: `kubectl` or `oc` (for operator inspection, pod logs, resource verification)
- JSON/YAML validation tools: `jq`, `yq` (for parsing API responses and metadata files)
- Database query tools: `psql` or equivalent (for direct schema and data validation)
- Browser developer tools (for UI inspection of Catalog filters and Serving Wizard behavior)
- Git/version control (for tracking metadata schema changes and model entry updates)
- Log viewing tools: `oc logs`, `stern` (for debugging ingestion pipeline and API errors)

---

## 10. Appendix

### 10.1 Test Case Summary

| Category | Total | P0 | P1 | P2 |
|----------|-------|----|----|-----|
| TC-SCHEMA | 7 | 5 | 1 | 1 |
| TC-INGEST | 6 | 3 | 2 | 1 |
| TC-API | 7 | 3 | 3 | 1 |
| TC-FILTER | 5 | 2 | 2 | 1 |
| TC-CARD | 5 | 0 | 4 | 1 |
| TC-AUDIT | 4 | 2 | 2 | 0 |
| TC-REG | 4 | 0 | 4 | 0 |
| TC-E2E | 4 | 4 | 0 | 0 |
| **Total** | **42** | **19** | **18** | **5** |

### 10.2 Endpoint/Method Coverage

| Endpoint | Test Cases | Coverage |
|----------|------------|----------|
| Model Catalog BFF API (model metadata endpoint) | TC-API-001, TC-API-002, TC-API-003, TC-API-004, TC-API-005, TC-API-006, TC-API-007, TC-E2E-001, TC-E2E-003, TC-E2E-004 | |
| Model Catalog schema (database fields) | TC-SCHEMA-001, TC-SCHEMA-002, TC-SCHEMA-003, TC-SCHEMA-004, TC-SCHEMA-005, TC-SCHEMA-006, TC-SCHEMA-007, TC-E2E-001, TC-E2E-004 | |
| Model ingestion pipeline (validation team handoff) | TC-INGEST-001, TC-INGEST-002, TC-INGEST-003, TC-INGEST-004, TC-INGEST-005, TC-INGEST-006, TC-E2E-001, TC-E2E-002 | |
| Model tagging logic (UI audit) | TC-AUDIT-001, TC-AUDIT-002, TC-AUDIT-003, TC-AUDIT-004, TC-E2E-002 | |
| RHOAI Catalog UI -- 'Tool Calling' task filter | TC-FILTER-001, TC-FILTER-002, TC-FILTER-003, TC-FILTER-004, TC-FILTER-005, TC-E2E-003 | |
| Modelcard rendering (YAML frontmatter) | TC-CARD-001, TC-CARD-002, TC-CARD-003, TC-CARD-004, TC-CARD-005, TC-E2E-003 | |
| Chat template path resolution logic | TC-API-005, TC-API-006, TC-SCHEMA-003, TC-CARD-005, TC-E2E-001 | |

### 10.3 Document Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-04-13 | Initial test plan |
| 1.1.0 | 2026-04-13 | Added 42 test cases across 8 categories, E2E scenarios, coverage matrix |

---

**End of Test Plan**
