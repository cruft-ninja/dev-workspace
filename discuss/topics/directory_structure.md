# Discussion: Directory Structure Refactor
**Status:** In Progress
**Goal:** Define rules for folder hierarchy to improve navigation and limit depth.

## Active Topics
| Status | Topic | Context / Notes |
| :--- | :--- | :--- |
| [ ] | **Max Children Rule** | Guideline: Max 10 children. Up to 15 ok if strictly necessary. |
| [ ] | **Unique Initials** | Goal: First char of each *directory* should be unique for fast navigation. |
| [ ] | **Registry Location** | Question: Should `registry` move to `projects/` or stay in root? |
| [ ] | **Gemini Files** | How to handle `gemini.md` presence in root vs subfolders regarding clutter. |

## Current Focus: [Unique Initials Rule]
*   **User:** The rule should only apply to *directories* for now.
*   **Gemini:** Does `registry/` collide with `readme.md`? (Currently: `r` collision).
*   **Action:** Need to decide if `registry` should move or if we accept file/folder collision.

---
## Decision Log (Archived)
*   [x] **Create Template:** Created `_template.md` in `topics/`.
*   [x] **Update README:** Populated `discuss/README.md`.
*   [x] **Move Projects:** Created `projects/` and moved `gnarly`, `script_runner`, `gemini_guru`, `prompt_mentor`, `prompt_engineering`.
*   [x] **Projects Rule:** "Project" folders should live in `projects/`, not root.
