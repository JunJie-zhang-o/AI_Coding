---
name: todo-plus-todo
description: Enforce strict Todo+ conventions for reading, generating, and updating the project root TODO file. Use when requests mention TODO planning, TODO parsing, TODO updates, Todo+ syntax, task tracking, or requirement breakdowns in TODO. Apply only to the repository root `TODO` file, preserve user intent, normalize formatting, and produce structured summaries of pending/completed/high-priority/risk items.
---

# Todo+ Root TODO Specification

## Scope
- Operate only on the repository root `TODO` file.
- Create `TODO` if it does not exist.
- Refuse write requests targeting `TODO.md`, nested TODO files, or other filenames.
- Preserve semantics of existing content; do not invent status changes.

## Canonical Format
- Use `☐` for incomplete tasks.
- Use `✔` for completed tasks.
- Add completion date as `@done(YYYY-MM-DD)` on completed tasks.
- Use priority tags from `@high`, `@medium`, `@low` for new prioritized tasks.
- Keep section headers as plain lines ending with `:` when used as groups.
- Use two-space indentation for child tasks.
- Keep tags after task text, in this order: priority tags first, then `@done(...)` when completed.

## Read Workflow
1. Parse file by sections and task lines.
2. Classify tasks into pending/completed/high-priority/risk-blocked views.
3. Return a structured summary with:
- Counts: pending, completed, high-priority, blocked/risky.
- Pending requirements list.
- Risk notes (blocked, ambiguous, malformed, or conflicting lines).
4. For non-canonical lines, keep original text in summary and mark as `needs-normalization`.

## Write Workflow
1. Add new tasks as `☐ <task text>` by default.
2. When marking complete, convert task to `✔ <task text> @done(YYYY-MM-DD)`.
3. Keep original section order whenever possible.
4. If no section exists, place items under `General:`.
5. Keep one logical task per line.

## Normalization Rules
- Normalize spacing around colons and task markers.
- Normalize full-width punctuation to ASCII when safe.
- Deduplicate exact duplicate task lines in the same section.
- Do not merge semantically different tasks.
- Retain unknown tags; keep standard priority tags for newly added items.

## Safety Rules
- Do not delete content explicitly marked by user as retained.
- Do not auto-complete ambiguous tasks.
- Before large reorder or rewrite, provide a concise change summary.
- If a request conflicts with scope, refuse and explain the allowed scope.

## Output Contract
After read or write operations, report these four buckets:
- `新增`: newly added tasks.
- `修改`: normalized or edited tasks.
- `完成`: tasks marked done with `@done(...)`.
- `风险`: malformed lines, ambiguous intent, blocked items, or refused operations.

## Examples
### Example 1: Read summary
User intent: summarize root TODO status.
Output shape:
- pending: N
- completed: N
- high-priority: N
- blocked/risk: N
- pending requirements: [...]
- needs-normalization: [...]

### Example 2: Add requirements
Input intent: add two requirements.
Write style:
- `☐ Add ROS2 e2e smoke test @high`
- `☐ Add TODO schema check in CI @medium`

### Example 3: Mark task completed
Input intent: complete a task.
Transform:
- from: `☐ Add TODO schema check in CI @medium`
- to: `✔ Add TODO schema check in CI @medium @done(2026-02-22)`
