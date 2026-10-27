# NSK DevPreneur-Hub & Sovereign TPRM Engine — Agent Guidelines (`AGENTS.md`)

This project follows the **Google Antigravity Spec-Driven Product Lifecycle** (*Beyond Vibe Coding*):
**PRD ("What") $\rightarrow$ In-Browser Design ("Look") $\rightarrow$ Technical Spec ("How") $\rightarrow$ Multi-Agent Reviewed Build $\rightarrow$ Production Deployment.**

## Core Rules for Coding Agents

1. **Interactive Requirements Clarification (`ask_question`)**:
   - When I ask you to ask me questions or clarify requirements, you are **REQUIRED** to use your `ask_question` tool to do so.
2. **Product Requirements Documents (PRDs) & Technical Specs**:
   - PRDs and architectural specifications should always be written to the project's root in `docs/plans/{{YYYY-MM-DD}}-{{description}}.md` format.
   - Keep functional scope (**PRD**) cleanly separated from technical architecture (**Spec** with Mermaid state diagrams).
3. **Sovereign Security & Repository Boundary**:
   - Never expose private `devpreneur-hub` proprietary platform source code to public repositories.
   - Only push sanitized public evaluation artifacts and TPRM engine benchmarks to the public showcase repository (`nsk-tprm-security-engine`).
   - Enforce POPIA Section 19 PII sanitization before any external LLM calls (`Gemini 2.5 Flash`).
4. **Progressive Enhancement & Graceful Fallbacks**:
   - All AI-powered workflows must include deterministic local fallbacks (e.g., Python AST static verification + `Graceful429Plugin` retry handling) to guarantee resilience in low-connectivity environments.
