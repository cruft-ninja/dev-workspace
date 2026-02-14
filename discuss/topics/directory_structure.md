# Discussion: Directory Structure Refactor
**Status:** In Progress
**Goal:** Define rules for folder hierarchy to improve navigation and limit depth.

## Active Topics
| Status | Topic | Context / Notes |
| :--- | :--- | :--- |
| [ ] | **Max Children Rule** | Guideline: Max 10 children. Up to 15 ok if strictly necessary. |
| [x] | **Unique Initials** | Implemented for `projects/`. |
| [x] | **Registry Location** | Decided: `registry` stays in root as global knowledge base. |
| [ ] | **Gemini Files** | How to handle `gemini.md` presence in root vs subfolders regarding clutter. |

## Current Focus: [Documentation Centralization]
*   **Decision:** Project-specific docs stay in project. General/Learning docs move to `registry/`.
*   **Action:** Cleanup of `projects/d_docs_gemini_internals`, `learning_mentorship_logs` complete.

---
## Decision Log (Archived)
*   [x] **Semantic Naming:** Projects renamed for clarity (e.g., `projects/n_gnarly_workflow_encabulator`, `projects/t_task_runner_gui`).
*   [x] **Project Structure:** "Inverted" `projects/n_gnarly_workflow_encabulator` to standard Python/Shell layout (`src`, `scripts`, `lib` in root).
*   [x] **Extensions:** Added `.sh` to scripts in `projects/t_task_runner_gui`.
*   [x] **Create Template:** Created `_template.md` in `topics/`.
*   [x] **Update README:** Populated `discuss/README.md`.
*   [x] **Move Projects:** Created `projects/` and moved `projects/n_gnarly_workflow_encabulator` (gnarly), `projects/t_task_runner_gui` (script_runner), `projects/d_docs_gemini_internals` (gemini_guru), `projects/l_llm_prompt_engineering` (prompt_engineering).
*   [x] **Projects Rule:** "Project" folders should live in `projects/`, not root.