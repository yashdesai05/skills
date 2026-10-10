# Task Planning, Prompt Decomposition & Token Minimization Rules

## 1. Disciplined Phased Planning
- **Plan First**: Before modifying code or executing complex workflows, establish a clear, concise execution plan with numbered phases.
- **Milestone Checkpoints**: Each phase must have an explicit verification checkpoint before moving to the next phase.
- **Single Source of Truth**: Identify exact files, functions, and symbols to touch before running edits.

## 2. Prompt Decomposition (Divide & Conquer)
- **Sub-task Chunking**: Whenever a prompt contains multiple requirements or features, break it down into atomic, bite-sized sub-tasks (Subtask 1, Subtask 2, Subtask 3...).
- **Sequential Execution**: Execute sub-tasks one by one. Validate and test each sub-task immediately after implementation.
- **Zero Monolithic Bloat**: Avoid doing everything in a single unvalidated step, which leads to hallucinations, truncations, and debugging overhead.

## 3. Token Minimization Protocol (Ultra-Low Token Footprint)
- **High-Density Communication**: Communicate with direct, actionable statements. Cut polite filler ("Sure, I can help you with that", "As you know", "Please note").
- **Surgical Code Modifications**: 
  - ALWAYS prefer targeted block edits (`replace_file_content` / `multi_replace_file_content`) over rewriting entire files.
  - Never dump 500+ lines of unchanged code when changing 5 lines.
- **Targeted Context Reading**:
  - Read specific line ranges with `view_file` (using `StartLine` and `EndLine`) rather than entire large files.
  - Use MCP memory tools or `.ui-ux-memory.json` to recall design systems and stack configs in ~90 tokens instead of re-reading configs.
- **Concise Summaries**:
  - Give compact, high-value status reports.
  - Use markdown diffs and clickable file links (`file:///...`).
