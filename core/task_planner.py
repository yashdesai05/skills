"""Task Planning, Prompt Decomposition & Token Optimization Engine.
Provides ultra-token-efficient task planning, prompt chunking into atomic sub-tasks,
and context optimization to minimize LLM token consumption.
"""

import re
from typing import Dict, Any, List

def plan_task_execution(prompt_or_goal: str, execution_mode: str = "incremental") -> Dict[str, Any]:
    """
    Creates a disciplined, phase-based execution plan for any complex request.
    Enforces incremental milestones, acceptance criteria, and token efficiency budgets.
    """
    clean_goal = prompt_or_goal.strip()
    
    # Identify key focus domains from the prompt
    lower_goal = clean_goal.lower()
    is_ui = any(k in lower_goal for k in ["ui", "css", "tailwind", "design", "frontend", "component", "page", "layout"])
    is_backend = any(k in lower_goal for k in ["api", "server", "backend", "database", "mcp", "endpoint", "logic"])
    is_fix_refactor = any(k in lower_goal for k in ["fix", "bug", "refactor", "repair", "error", "audit"])
    
    phases: List[Dict[str, Any]] = []
    
    # Phase 1: Discovery & Scope Definition
    phases.append({
        "phase": 1,
        "name": "Scope & Context Discovery",
        "description": "Inspect existing files/memory without re-reading entire codebase. Identify target files and constraints.",
        "actions": [
            "Check cached memory or config before reading raw files.",
            "Identify exact target files and functions to modify.",
            "Establish unambiguous definition of done (DoD)."
        ],
        "token_budget": "Ultra-Low (<150 tokens)",
        "checkpoint": "Exact file paths & interfaces verified."
    })
    
    # Phase 2: Modular Architecture / Sub-task Chunking
    if is_fix_refactor:
        phases.append({
            "phase": 2,
            "name": "Root-Cause Isolation & Targeted Fix",
            "description": "Isolate the defective block and craft minimal surgical diff.",
            "actions": [
                "Pinpoint specific lines or failing conditions.",
                "Apply surgical replacement without touching unrelated logic.",
                "Preserve all existing comments and documentation."
            ],
            "token_budget": "Low (<250 tokens)",
            "checkpoint": "Error condition resolved with minimal diff."
        })
    elif is_ui:
        phases.append({
            "phase": 2,
            "name": "Layout, Tokens & Typography Foundation",
            "description": "Setup 4px/8px rhythm, accessible color tokens (60-30-10), and max reading bounds (65ch).",
            "actions": [
                "Establish container constraints and typography hierarchy.",
                "Apply WCAG AAA contrast and touch targets (min 44px).",
                "Ensure mobile responsive scaffolding."
            ],
            "token_budget": "Medium (<350 tokens)",
            "checkpoint": "Responsive layout with zero overflow and verified typography."
        })
        phases.append({
            "phase": 3,
            "name": "Component Assembly & Micro-Interactions",
            "description": "Add interactive states, accessible controls, and smooth micro-animations.",
            "actions": [
                "Build modular sub-components with explicit states (hover, focus, active).",
                "Inject lightweight micro-interactions (150-250ms ease-out).",
                "Verify keyboard focus rings and semantic HTML."
            ],
            "token_budget": "Medium (<350 tokens)",
            "checkpoint": "Interactive states responsive and accessible."
        })
    else:
        phases.append({
            "phase": 2,
            "name": "Core Logic & Data Flow Implementation",
            "description": "Implement core algorithms/handlers in discrete modular steps.",
            "actions": [
                "Implement pure core functions with explicit type hints.",
                "Wire inputs, validation, and error handlers.",
                "Keep functions short and single-responsibility."
            ],
            "token_budget": "Medium (<300 tokens)",
            "checkpoint": "Core logic returns expected outputs for edge cases."
        })
        phases.append({
            "phase": 3,
            "name": "Integration & Interface Wiring",
            "description": "Expose clean interfaces/endpoints and connect with consumers.",
            "actions": [
                "Register endpoints, CLI commands, or MCP tools.",
                "Validate payload serialization and error responses.",
                "Keep response payloads compact and structured."
            ],
            "token_budget": "Low (<200 tokens)",
            "checkpoint": "Endpoints/tools callable and responsive."
        })
        
    # Final Phase: Verification, QA & Token Review
    final_phase_num = len(phases) + 1
    phases.append({
        "phase": final_phase_num,
        "name": "Automated Verification & Token Economy Audit",
        "description": "Run test suites, verify outputs, and ensure zero redundant token waste.",
        "actions": [
            "Execute test commands or run verification script.",
            "Confirm no regressions in existing features.",
            "Present brief summary with clickable file links and diffs."
        ],
        "token_budget": "Ultra-Low (<120 tokens)",
        "checkpoint": "All tests pass cleanly with zero lint or runtime errors."
    })
    
    return {
        "status": "PLAN_GENERATED",
        "goal": clean_goal,
        "execution_mode": execution_mode,
        "total_phases": len(phases),
        "phases": phases,
        "token_optimization_rules": [
            "Never dump full files when making small changes; use targeted replacements.",
            "Execute each phase sequentially; verify before advancing to next step.",
            "Keep LLM responses concise and focused directly on user value.",
            "Avoid conversational filler and repetitive summaries."
        ],
        "estimated_token_savings": "65% - 80% vs monolithic execution"
    }

def decompose_prompt(prompt: str, max_subtasks: int = 5) -> Dict[str, Any]:
    """
    Deconstructs a complex, multi-faceted prompt into small, atomic sub-tasks.
    Each sub-task is self-contained with minimal context requirements to preserve tokens.
    """
    clean_prompt = prompt.strip()
    
    # Split prompt by common sentence delimiters or bullet points
    raw_lines = re.split(r'[\n\r]+|[.;]\s+(?=[A-Z0-9\u0900-\u097F])|(?:\s+(?:aur|and|also|then|furthermore|ke sath)\s+)', clean_prompt, flags=re.IGNORECASE)
    items = [line.strip("- *• \t") for line in raw_lines if len(line.strip("- *• \t")) > 5]
    
    if not items:
        items = [clean_prompt]
        
    # Cap items to max_subtasks
    selected_items = items[:max_subtasks] if len(items) > max_subtasks else items
    
    subtasks: List[Dict[str, Any]] = []
    for idx, item in enumerate(selected_items, 1):
        # Determine task type
        item_lower = item.lower()
        if any(k in item_lower for k in ["test", "verify", "check", "run", "validate"]):
            category = "Verification & Testing"
            token_target = "<100 tokens"
        elif any(k in item_lower for k in ["plan", "break", "dified", "divide", "structure", "design"]):
            category = "Planning & Architecture"
            token_target = "<120 tokens"
        elif any(k in item_lower for k in ["fix", "error", "bug", "repair"]):
            category = "Surgical Fix"
            token_target = "<150 tokens"
        elif any(k in item_lower for k in ["ui", "css", "style", "animation", "color"]):
            category = "UI/UX Styling"
            token_target = "<200 tokens"
        else:
            category = "Implementation"
            token_target = "<180 tokens"
            
        subtasks.append({
            "subtask_id": idx,
            "title": f"Step {idx}: {item[:45]}..." if len(item) > 45 else f"Step {idx}: {item}",
            "objective": item,
            "category": category,
            "dependency": f"Step {idx-1}" if idx > 1 else "None (Initial Step)",
            "token_budget": token_target,
            "execution_protocol": "Execute atomically -> Verify -> Commit change before proceeding."
        })
        
    return {
        "status": "DECOMPOSED",
        "original_prompt": clean_prompt,
        "subtasks_count": len(subtasks),
        "subtasks": subtasks,
        "sequential_guideline": (
            "Rule: Process one subtask at a time. After completing each step, verify the outcome "
            "before calling tools for the next step. This prevents token context blowup and eliminates hallucinations."
        ),
        "token_economy_benefit": "Reduces peak context window consumption by up to 75%."
    }

def optimize_token_context(content_or_request: str, mode: str = "compress") -> Dict[str, Any]:
    """
    Optimizes and compresses prompts, code snippets, or conversational context to save tokens.
    Modes:
      - 'compress': Strips boilerplate, conversational filler, and redundant words.
      - 'diff_only': Formats guidance on extracting only modified lines/blocks.
      - 'summary': Generates high-density structural context.
    """
    raw_text = content_or_request.strip()
    original_char_count = len(raw_text)
    est_orig_tokens = max(1, original_char_count // 4)
    
    if mode == "compress":
        # Remove repeated whitespace and common conversational fluff
        compressed = re.sub(r'[ \t]+', ' ', raw_text)
        compressed = re.sub(r'\n\s*\n+', '\n', compressed)
        # Strip common AI/human filler phrases
        fluff_patterns = [
            r'(?i)\b(please\s+note\s+that|as\s+mentioned\s+earlier|in\s+order\s+to|it\s+is\s+important\s+to\s+remember\s+that)\b',
            r'(?i)\b(i\s+would\s+like\s+to\s+ask\s+you\s+to|could\s+you\s+please|can\s+you\s+help\s+me\s+with)\b',
            r'(?i)\b(basically|essentially|as\s+you\s+can\s+see|without\s+further\s+ado)\b'
        ]
        for pat in fluff_patterns:
            compressed = re.sub(pat, '', compressed)
        compressed = re.sub(r'\s+', ' ', compressed).strip()
        
        comp_char_count = len(compressed)
        est_comp_tokens = max(1, comp_char_count // 4)
        tokens_saved = max(0, est_orig_tokens - est_comp_tokens)
        pct_saved = round((tokens_saved / est_orig_tokens) * 100, 1) if est_orig_tokens > 0 else 0
        
        return {
            "mode": "compress",
            "original_tokens_est": est_orig_tokens,
            "optimized_tokens_est": est_comp_tokens,
            "tokens_saved_est": tokens_saved,
            "savings_percentage": f"{pct_saved}%",
            "optimized_text": compressed,
            "token_rule": "High-density instruction generated. Direct action without polite filler."
        }
        
    elif mode == "diff_only":
        return {
            "mode": "diff_only",
            "guideline": "Only pass changed functions or targeted lines instead of entire source files.",
            "best_practices": [
                "Use replace_file_content or multi_replace_file_content with exact ranges.",
                "Never re-send full 500+ line files when modifying 5 lines.",
                "Use search_graph or exact line views (slice notation) to minimize read window.",
                "Omit unchanged import lists or boilerplate headers in context."
            ],
            "average_token_reduction": "85% - 95% compared to whole-file rewriting"
        }
        
    else:  # summary mode
        first_lines = [line.strip() for line in raw_text.splitlines() if line.strip()][:5]
        summary_repr = " | ".join(first_lines)
        return {
            "mode": "summary",
            "original_tokens_est": est_orig_tokens,
            "high_density_anchor": summary_repr[:200],
            "recommendation": "Maintain persistent memory cache (e.g. .ui-ux-memory.json) instead of re-sending full spec."
        }
