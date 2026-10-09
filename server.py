"""UI/UX Pro MCP Server - Fast, Token-Optimized UI Design Engine.
Features:
- Domain Color Research across 192 product profiles (No generic AI dark mode clichés)
- Codebase Memory & Caching (.ui-ux-memory.json - scans once, never re-reads)
- Apple/Linear Grade Physics Animations & Micro-interactions
- 4px/8px Spatial Rhythm & Spacing Audits
- Universal compatibility: Antigravity IDE, Cursor, Claude Desktop, Claude Code, ChatGPT
"""

import sys
import json
from mcp.server.fastmcp import FastMCP

from core.spacing_engine import audit_spacing, get_spacing_system
from core.design_system import generate_design_system
from core.blueprints import get_component_blueprint
from core.code_fixer import fix_ui_code
from core.micro_interactions import get_micro_interaction
from core.intel_search import search_intel
from core.checklist import get_checklist
from core.codebase_memory import scan_and_remember, get_memory
from core.color_researcher import research_best_colors
from core.motion_engine import get_motion_preset
from core.three_engine import generate_3d_model_experience

# Initialize FastMCP Server
mcp = FastMCP("ui-ux-pro")

# 0. 3D MODEL & WEBGL EXPERIENCES
@mcp.tool()
def get_3d_experience(experience_type: str = "product_viewer", framework: str = "r3f") -> str:
    """
    Generate accurate, production-ready 3D model viewers and procedural 3D web experiences.
    experience_type: 'product_viewer' (accurate GLTF/GLB model viewer with studio lighting & auto-centering),
                     'glass_orb' (organic liquid sphere with chromatic aberration & mouse follow),
                     'interactive_globe' (3D cyber globe with atmosphere glow & coordinates),
                     'interactive_3d_card' (pure 60fps CSS 3D perspective tilt without heavy WebGL).
    framework: 'r3f' (React Three Fiber) or 'threejs' (Vanilla Three.js).
    """
    result = generate_3d_model_experience(experience_type, framework)
    return json.dumps(result, indent=2)

# 1. CODEBASE MEMORY & CACHING TOOLS (Scan once, never re-read!)
@mcp.tool()
def remember_project_codebase(project_path: str = ".") -> str:
    """
    Scans project once (Tailwind config, globals.css, fonts, dependencies) and saves
    design memory to `.ui-ux-memory.json`. Future requests recall this with zero token overhead.
    """
    result = scan_and_remember(project_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_project_memory(project_path: str = ".") -> str:
    """
    Instantly returns cached project design context (fonts, colors, framework, spacing rules)
    in ~100 tokens. Eliminates the need to re-read codebase files.
    """
    result = get_memory(project_path)
    return json.dumps(result, indent=2)

# 2. COLOR RESEARCH & ANTI-AI-CLICHE TOOLS
@mcp.tool()
def research_color_palette(prompt_or_niche: str, mode_preference: str = "auto") -> str:
    """
    Researches the exact product domain across 192 archetypes and returns a human-crafted
    color palette in 60-30-10 balance. Avoids amateur AI dark mode clichés (no generic purple on black).
    mode_preference: 'auto', 'light', 'dark', 'warm_stone'.
    """
    result = research_best_colors(prompt_or_niche, mode_preference)
    return json.dumps(result, indent=2)

# 3. PREMIUM MOTION & PHYSICS
@mcp.tool()
def get_premium_motion(motion_name: str = "tactile_button") -> str:
    """
    Get Apple / Linear / Stripe grade GPU-accelerated micro-interactions.
    motion_name options: 'tactile_button', 'border_beam_card', 'sliding_tab', 'accordion_grid', 'stagger_reveal'.
    Uses cubic-bezier spring curves and zero-reflow transforms.
    """
    result = get_motion_preset(motion_name)
    return json.dumps(result, indent=2)

# 4. SPACING, AUDITING & FIXING
@mcp.tool()
def audit_ui_spacing(code_snippet: str) -> str:
    """
    Audit HTML, Tailwind, JSX, or CSS code for spacing & layout issues.
    Checks 4px/8px rhythm, accessible button heights (min 44px), line length constraints, and card padding.
    """
    result = audit_spacing(code_snippet)
    return json.dumps(result, indent=2)

@mcp.tool()
def repair_ui_code(code: str) -> str:
    """
    Automatically repair and enhance messy/cramped UI code.
    Snaps arbitrary margins/paddings to 4px/8px grid, adds min 44px touch targets, fixes cramped section spacing, and adds micro-interactions.
    """
    result = fix_ui_code(code)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_spacing_tokens(density: str = "balanced") -> str:
    """
    Get calibrated 4px/8px spacing system, container constraints, and component padding rules.
    density options: 'compact' (dashboards), 'balanced' (modern SaaS/web), 'spacious' (luxury/editorial).
    """
    result = get_spacing_system(density)
    return json.dumps(result, indent=2)

@mcp.tool()
def create_design_system(vibe_query: str = "modern_saas_dark") -> str:
    """
    Generate a full token-efficient design system tailored to a vibe/industry.
    Includes WCAG AA contrast check, Google Font pair, semantic colors, radii, shadows, and Tailwind config.
    """
    result = generate_design_system(vibe_query)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_ui_blueprint(component_type: str = "hero") -> str:
    """
    Get a production-ready, beautifully spaced component blueprint with Tailwind classes.
    component_type options: 'navbar', 'hero', 'feature_grid', 'pricing_card', 'dashboard_card', 'modal_dialog'.
    """
    result = get_component_blueprint(component_type)
    return json.dumps(result, indent=2)

@mcp.tool()
def search_design_intelligence(query: str, domain: str = "all") -> str:
    """
    Search curated catalog of 79 design styles, 192 color palettes, and 119 UX guidelines.
    Returns 2-3 laser-focused, token-compact recommendations.
    """
    result = search_intel(query, domain)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_preflight_checklist(category: str = "pre_ship") -> str:
    """
    Get a rapid 5-point quality checklist before shipping frontend code.
    category options: 'spacing_and_layout', 'accessibility_wcag', 'responsive_mobile', 'pre_ship'.
    """
    result = get_checklist(category)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
