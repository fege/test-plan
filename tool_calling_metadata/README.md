# Tool Calling Metadata Integration

Integration of validated Tool Calling metadata into the Model Catalog to enable automated model deployment configuration in the RHOAI Serving UI.

## References

- **Strategy**: [RHAISTRAT-1262](https://redhat.atlassian.net/browse/RHAISTRAT-1262)
- **Feature Refinement**: [Google Doc](https://docs.google.com/document/d/1XaK-rZPZEexUrrIMkyLXzjQJYY-rKATdkEPE_NRTz5I/edit?usp=sharing)
- **Test Plan**: [TestPlan.md](TestPlan.md)

## Overview

This feature ensures the Model Catalog serves as the single source of truth for tool-calling models by storing validated CLI requirements and chat template paths. The Model Validation team confirms model compatibility, then this data is ingested into the Catalog with proper tags, enabling dynamic UI configuration and consistent deployments.

## Test Cases

**28 test cases** across 5 categories — see [test_cases/INDEX.md](test_cases/INDEX.md)

| Priority | Count |
|----------|-------|
| P0 (Critical) | 9 |
| P1 (High) | 15 |
| P2 (Medium) | 4 |

Categories: API (8), DB (5), PIPE (5), UI (7), VER (3)

## Testing

Automated tests will be implemented to cover:
- Model Catalog BFF API endpoints for retrieving and validating tool-calling metadata
- Database schema and data persistence for tool-calling fields
- Ingestion pipeline integration with Model Validation team output
- UI components (Tool Calling filter, modelcard rendering)
- Versioning support for metadata evolution across RHAIIS/ModelCar updates

See [TestPlan.md](TestPlan.md) for complete test strategy and coverage details.
