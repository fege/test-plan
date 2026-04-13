---
test_case_id: TC-CARD-002
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-CARD-002: CLI arguments on modelcard are copy-paste friendly

**Objective**: Verify that the tool-calling CLI arguments displayed on the modelcard can be easily copied and pasted by users for manual deployment configuration.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A tool-calling model ingested with CLI arguments and chat template path

**Test Steps**:
1. Navigate to the modelcard for granite-3.1-8b-instruct
2. Locate the YAML frontmatter section displaying tool-calling commands
3. Select and copy the CLI arguments text from the modelcard
4. Paste the copied text into a text editor
5. Verify the pasted text is clean (no extra whitespace, HTML tags, or formatting artifacts)
6. Verify the pasted CLI arguments can be used directly in a vLLM deployment command:
   ```
   --chat-template examples/tool_chat_template_granite.jinja --tool-call-parser hermes --enable-auto-tool-choice
   ```

**Expected Results**:
- Copied text is clean and directly usable in CLI commands
- No hidden characters or formatting artifacts in the copied text
- Line breaks and indentation are preserved appropriately

**Notes**: To be filled later in the process.
