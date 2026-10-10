# UI/UX Pro MCP Server 🚀

A high-performance, **ultra-token-efficient** Model Context Protocol (MCP) server for modern UI/UX design, readable typography, domain color research, and award-winning web animations.

Compatible with **Antigravity IDE**, **Cursor**, **Claude Desktop**, **Claude Code**, and **ChatGPT**.

---

## 🌟 Key Features

### 1. 📖 Guaranteed Text Readability & Typography Perfection
- **Optimal Reading Bounds**: Strictly enforces **50–75 characters per line** (`max-w-prose` / `65ch`), ensuring long paragraphs never stretch uncomfortably across wide screens.
- **Calibrated Line-Heights**:
  - Headings: `leading-tight` (1.1–1.25) + `tracking-tight` (-0.025em) for punchy titles.
  - Body Copy: `leading-relaxed` (1.6–1.7) for fatigue-free reading.
  - Labels & Badges: `leading-none` + `tracking-wider uppercase`.
- **WCAG AAA Contrast Rating**: Mathematically calculates relative luminance to prevent washed-out text on both light and dark backgrounds.
- **Eye-Strain Halation Guard**: Eliminates harsh pure white on pure black glare using tinted surfaces (`#0B0F17`) and soft whites (`#F8FAFC`).

### 2. 🎬 Award-Winning Animation Recipes
Production-grade, zero-jank animation code across 5 industry-standard libraries:
1. **Framer Motion**: Shared layout transitions (`layoutId`), physics spring tabs, gesture drag, staggered child reveals.
2. **GSAP + ScrollTrigger**: Scroll-scrubbed text reveals, pinned sections, zero-allocation magnetic button (`quickTo`).
3. **Anime.js**: Staggered 2D grid ripple waves, SVG path morphing.
4. **Barba.js**: Smooth page-to-page curtain wipes and crossfades without hard browser page reloads.
5. **Rive Runtime**: 60fps vector state-machine animations reacting in real time to mouse hover and cursor coordinates.

### 3. 🎨 Domain-Aware Color Research (Anti-AI Clichés)
- Researches exact product domain across 192 archetypes in 60-30-10 balance.
- Filters out generic AI clichés (no fluorescent purple on pure black).

### 4. 🧠 Codebase Memory & Caching
- Scans project once, stores design DNA in `.ui-ux-memory.json`.
- Future tool calls retrieve design context in **~90 tokens** with zero file re-reading.

### 5. ⚡ Phased Task Planning & Token Economy
- **Phase-Based Execution**: Generates structured, milestone-driven plans with checkpoints and token budgets.
- **Prompt Decomposition**: Breaks complex prompts into bite-sized, sequential subtasks to eliminate hallucinations and context blowup.
- **Token Saver Engine**: Strips conversational padding, compresses instructions, and enforces surgical diffs for 65–80% token savings.

---

## 🛠️ Complete MCP Toolset

| Tool Name | Purpose | Output Tokens |
|---|---|---|
| `audit_and_fix_readability` | Audits text line-length (50-75ch), line-heights, and WCAG AAA contrast | ~160 |
| `get_readability_standards` | Returns typography scales, leading, tracking, and curated font pairings | ~130 |
| `get_award_animation` | Recipes for Framer Motion, GSAP ScrollTrigger, Anime.js, Barba.js, or Rive | ~220 |
| `remember_project_codebase` | Scans and caches project design DNA in `.ui-ux-memory.json` | ~120 |
| `get_project_memory` | Recalls cached design context instantly without re-reading files | ~90 |
| `research_color_palette` | Researches 60-30-10 human color scheme (Light/Dark/Stone) | ~180 |
| `audit_ui_spacing` | Detects 4px/8px rhythm errors, <44px buttons, and cramped cards | ~150 |
| `repair_ui_code` | Repairs raw code into 8pt grid, accessible UI with micro-interactions | ~220 |
| `get_ui_blueprint` | Navbar, Hero, Bento Grid, Pricing Card, Modal blueprints | ~280 |
| `search_design_intelligence` | Search 79 styles, 192 color palettes, and 119 UX guidelines | ~110 |
| `get_preflight_checklist` | Pre-ship 5-point quality QA checklist | ~90 |
| `plan_task_execution` | Generates phased milestone execution plan with DoD and token budget | ~140 |
| `decompose_prompt` | Splits complex prompt into bite-sized atomic subtasks executed sequentially | ~130 |
| `optimize_token_context` | Compresses prompt context and strips conversational filler (65-80% token savings) | ~90 |


---

## ⚡ Client Setup

### Antigravity IDE (Configured ✅)
Registered in `~/.gemini/config/mcp_config.json`.

### Cursor IDE
Add to `~/.cursor/mcp.json` or `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "ui-ux-pro": {
      "command": "/home/yashdesai/.local/bin/uv",
      "args": [
        "run",
        "--directory",
        "/home/yashdesai/Documents/Projects/skills",
        "server.py"
      ]
    }
  }
}
```

### Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ui-ux-pro": {
      "command": "/home/yashdesai/.local/bin/uv",
      "args": [
        "run",
        "--directory",
        "/home/yashdesai/Documents/Projects/skills",
        "server.py"
      ]
    }
  }
}
```

### Claude Code CLI
```bash
claude mcp add ui-ux-pro -- /home/yashdesai/.local/bin/uv run --directory /home/yashdesai/Documents/Projects/skills server.py
```

---

## 🧪 Run Tests
```bash
.venv/bin/python3 tests/test_server.py
```
