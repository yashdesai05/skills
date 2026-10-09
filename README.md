# UI/UX Pro MCP Server 🚀

A high-performance, **ultra-token-efficient** Model Context Protocol (MCP) server for modern UI/UX design, spatial rhythm enforcement, domain color research, and high-end physics animations.

Compatible with **Antigravity IDE**, **Cursor**, **Claude Desktop**, **Claude Code**, and **ChatGPT**.

---

## 🌟 Key Upgrades & Highlights

### 1. 🧠 Codebase Memory & Caching (Ek Baar Scan Karo, Phir Zero Re-reading!)
- **Problem**: Har turn me LLM ko 15-20 files (tailwind.config, globals.css, package.json) dobara read karni padti thi, jisse thousands of tokens waste hote the.
- **Solution**: `remember_project_codebase()` project ke typography, colors, CSS engine aur framework ko ek baar scan karke `.ui-ux-memory.json` me save kar leta hai.
- Uske baad `get_project_memory()` **<1ms** me bas **~100 tokens** me pure project ka design DNA return karta hai bina kisi file ko re-read kiye!

### 2. 🎨 Domain-Aware Color Research (No Generic "AI Dark Mode" Clichés!)
- **Problem**: AI aksar har cheez ko pure `#000000` par fluorescent pink/purple neon bana deta hai, jo cheap aur amateur AI template jaisa lagta hai.
- **Solution**: `research_color_palette()` 192 product archetypes aur psychology datasets se research karta hai:
  - **Healthcare / B2B**: Crisp, airy high-trust light mode (`#F8FAFC`, calming slate).
  - **Luxury / High-End**: Warm stone, rich bronze & obsidian (`#121110`, warm charcoal).
  - **Trading / Analytics**: Tinted deep slate navy (`#0B0F17`), never raw black.
  - **60-30-10 Rule**: 60% Canvas, 30% Structural text/borders, 10% Strategic focal accent.
  - **Anti-AI Cliché Guard**: Explicitly eliminates fluorescent purple-on-black traps.

### 3. 🎬 Apple & Linear Grade Physics Animations
- **Zero-Reflow GPU Composited**: Kabhi bhi `width`, `height`, ya `margin` animate nahi karta (jo jank karte hain). Sirf `transform` aur `opacity` use karta hai.
- **Natural Spring Deceleration**: `cubic-bezier(0.16, 1, 0.3, 1)` physics curve.
- **Presets**:
  - `tactile_button`: Instantaneous 140ms physical press feel.
  - `border_beam_card`: Subtle traveling gradient light border on card hover.
  - `sliding_tab`: Native app style sliding pill tab indicator.
  - `accordion_grid`: Zero-JS CSS grid `0fr -> 1fr` height expansion.
  - `prefers-reduced-motion`: 100% accessible fallback for motion sensitivity.

---

## 🛠️ Complete MCP Toolset

| Tool Name | Kya Kaam Karta Hai | Output Tokens |
|---|---|---|
| `remember_project_codebase` | Project ke design stack ko scan karke `.ui-ux-memory.json` me cache karta hai | ~120 |
| `get_project_memory` | Cached design DNA recall karta hai (zero file reading) | ~90 |
| `research_color_palette` | Prompt ke hisab se best 60-30-10 palette research karta hai (Light/Dark/Stone) | ~180 |
| `get_premium_motion` | Apple/Linear grade spring bezier animations aur micro-interactions deta hai | ~120 |
| `audit_ui_spacing` | 4px/8px grid errors, <44px buttons, cramped cards detect karta hai | ~150 |
| `repair_ui_code` | Raw UI code ko automatically 8pt grid aur accessible modern UI me convert karta hai | ~220 |
| `get_spacing_tokens` | Calibrated spacing scale (compact, balanced, spacious) aur container widths | ~140 |
| `create_design_system` | Full token set + Google Font pair + Tailwind config generate karta hai | ~250 |
| `get_ui_blueprint` | Navbar, Hero, Bento Grid, Pricing Card, Modal ka pixel-perfect code | ~280 |
| `search_design_intelligence` | 79 design styles, 192 color palettes, 119 UX guidelines me fast search | ~110 |
| `get_preflight_checklist` | Shipping se pehle 5-point QA checklist | ~90 |

---

## ⚡ Setup Guides

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
Add to your Claude Desktop config file:
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
