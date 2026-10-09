"""Intelligent Domain Color Research Engine for UI/UX Pro MCP.
Researches the exact niche, product type, and psychological color harmony across 192 product profiles.
Prevents generic "AI dark mode" clichés (no fluorescent purple on pure black).
Provides sophisticated human-designed palettes in 60-30-10 balance for both Light & Dark modes.
"""

import os
import csv
import re
from typing import Dict, Any, List, Optional

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def research_best_colors(prompt: str, mode_preference: str = "auto") -> Dict[str, Any]:
    """
    Researches the prompt and returns a domain-specific, human-crafted color palette with zero AI clichés.
    """
    clean_prompt = prompt.lower()
    terms = [w for w in re.split(r'[\s,._-]+', clean_prompt) if len(w) > 2]
    
    best_product = None
    best_color_row = None
    best_reasoning_row = None
    highest_score = -1

    # 1. Match against products.csv & colors.csv
    products_csv_path = os.path.join(DATA_DIR, "products.csv")
    colors_csv_path = os.path.join(DATA_DIR, "colors.csv")
    reasoning_csv_path = os.path.join(DATA_DIR, "ui-reasoning.csv")

    products_data: List[Dict[str, str]] = []
    if os.path.exists(products_csv_path):
        with open(products_csv_path, mode="r", encoding="utf-8") as f:
            products_data = list(csv.DictReader(f))

    colors_data: Dict[str, Dict[str, str]] = {}
    if os.path.exists(colors_csv_path):
        with open(colors_csv_path, mode="r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                p_type = row.get("Product Type", "").strip().lower()
                colors_data[p_type] = row

    reasoning_data: Dict[str, Dict[str, str]] = {}
    if os.path.exists(reasoning_csv_path):
        with open(reasoning_csv_path, mode="r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cat = row.get("UI_Category", "").strip().lower()
                reasoning_data[cat] = row

    # Score matches
    for prod in products_data:
        p_name = prod.get("Product Type", "")
        keywords = prod.get("Keywords", "").lower()
        full_text = f"{p_name.lower()} {keywords}"
        score = sum(3 for t in terms if t in p_name.lower()) + sum(1 for t in terms if t in keywords)
        
        if score > highest_score:
            highest_score = score
            best_product = prod
            best_color_row = colors_data.get(p_name.strip().lower())
            best_reasoning_row = reasoning_data.get(p_name.strip().lower())

    # Fallback to SaaS (General) if score is low
    if highest_score <= 0 or not best_color_row:
        # Check domain heuristics
        if any(w in clean_prompt for w in ["doctor", "health", "clinic", "patient", "medical"]):
            target_key = "healthcare app"
        elif any(w in clean_prompt for w in ["luxury", "watch", "jewelry", "fashion", "high-end"]):
            target_key = "e-commerce luxury"
        elif any(w in clean_prompt for w in ["fintech", "crypto", "trading", "bank", "invest", "finance"]):
            target_key = "financial dashboard"
        elif any(w in clean_prompt for w in ["dev", "code", "terminal", "cli", "api", "infra"]):
            target_key = "b2b service"
        else:
            target_key = "saas (general)"

        best_color_row = colors_data.get(target_key, list(colors_data.values())[0] if colors_data else {})
        best_product = next((p for p in products_data if p.get("Product Type", "").lower() == target_key), {})
        best_reasoning_row = reasoning_data.get(target_key, {})

    product_name = best_product.get("Product Type", "Modern Product")
    color_focus = best_product.get("Color Palette Focus", "Balanced professional contrast")
    anti_patterns = best_reasoning_row.get("Anti_Patterns", "Avoid AI purple/pink gradients & generic default dark mode") if best_reasoning_row else "Avoid AI purple/pink gradients"

    # Determine recommended mode based on psychology and user preference
    rec_mode = "light"
    if mode_preference.lower() in ["dark", "light"]:
        rec_mode = mode_preference.lower()
    else:
        # Domain based recommendation
        if any(w in clean_prompt for w in ["trading", "crypto", "dashboard", "developer", "ide", "gaming"]):
            rec_mode = "dark"
        elif any(w in clean_prompt for w in ["luxury", "high-end"]):
            rec_mode = "warm_stone"
        elif any(w in clean_prompt for w in ["health", "medical", "clinic", "education", "b2b", "service", "gov"]):
            rec_mode = "light"
        else:
            rec_mode = "light"  # Human SaaS prefers crisp clean light with dark toggle

    # Palette Extraction
    primary = best_color_row.get("Primary", "#2563EB")
    secondary = best_color_row.get("Secondary", "#3B82F6")
    accent = best_color_row.get("Accent", "#EA580C")
    base_bg = best_color_row.get("Background", "#F8FAFC")
    base_fg = best_color_row.get("Foreground", "#0F172A")
    base_card = best_color_row.get("Card", "#FFFFFF")
    base_border = best_color_row.get("Border", "#E2E8F0")

    # Generate Cohesive Dark & Light Pairings (Not cheap pure #000000)
    if rec_mode == "dark":
        palette = {
            "mode": "Sophisticated Dark (Tinted Slate / Obsidian)",
            "background": "#0B0F17",  # Deep navy slate, never raw 000
            "surface": "#121824",
            "surface_elevated": "#1A2234",
            "border": "#222D42",
            "border_subtle": "#161F30",
            "text_primary": "#F8FAFC",
            "text_muted": "#94A3B8",
            "primary": primary if primary != "#000000" else "#3B82F6",
            "accent": accent,
            "success": "#10B981"
        }
    elif rec_mode == "warm_stone":
        palette = {
            "mode": "Warm Stone & Obsidian (Editorial Luxury)",
            "background": "#121110",
            "surface": "#1A1816",
            "surface_elevated": "#262320",
            "border": "#36322D",
            "border_subtle": "#22201D",
            "text_primary": "#F5F3EF",
            "text_muted": "#A8A29E",
            "primary": "#D97706" if "#" in primary else primary,
            "accent": "#F59E0B",
            "success": "#10B981"
        }
    else:  # Clean Light
        palette = {
            "mode": "Crisp Editorial Light (Airy & High Trust)",
            "background": base_bg if base_bg else "#F8FAFC",
            "surface": base_card if base_card else "#FFFFFF",
            "surface_elevated": "#F1F5F9",
            "border": base_border if base_border else "#E2E8F0",
            "border_subtle": "#F8FAFC",
            "text_primary": base_fg if base_fg else "#0F172A",
            "text_muted": "#64748B",
            "primary": primary,
            "accent": accent,
            "success": "#059669"
        }

    return {
        "domain_identified": product_name,
        "design_reasoning": color_focus,
        "mode_recommended": rec_mode,
        "ai_cliche_guard": f"Avoided: {anti_patterns}",
        "color_distribution": {
            "60_percent_canvas": f"Background ({palette['background']}) + Surface ({palette['surface']})",
            "30_percent_structural": f"Text ({palette['text_primary']}) + Borders ({palette['border']})",
            "10_percent_focal_accent": f"Primary CTA ({palette['primary']}) + Accent ({palette['accent']})"
        },
        "tokens": palette,
        "tailwind_vars": f"""colors: {{
  bg: '{palette['background']}',
  surface: '{palette['surface']}',
  'surface-elevated': '{palette['surface_elevated']}',
  border: '{palette['border']}',
  primary: '{palette['primary']}',
  accent: '{palette['accent']}',
  'text-main': '{palette['text_primary']}',
  'text-muted': '{palette['text_muted']}'
}}"""
    }
