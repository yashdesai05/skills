"""Spacing & Layout Engine for UI/UX Pro MCP.
Provides 4px/8px grid auditing, spacing scale generation, and layout rhythm verification.
Optimized for minimal token output with high actionable value.
"""

import re
from typing import Dict, List, Any, Optional

STANDARD_8PT_PX = [0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 128]
TAILWIND_SPACING_MAP = {
    0: "0", 1: "0.5", 2: "1", 4: "1", 6: "1.5", 8: "2", 10: "2.5", 12: "3",
    14: "3.5", 16: "4", 20: "5", 24: "6", 28: "7", 32: "8", 36: "9", 40: "10",
    44: "11", 48: "12", 56: "14", 64: "16", 72: "18", 80: "20", 96: "24"
}

def closest_8pt(px: int) -> int:
    """Find the nearest 4px/8px grid value."""
    return min(STANDARD_8PT_PX, key=lambda x: abs(x - px))

def get_spacing_system(density: str = "balanced") -> Dict[str, Any]:
    """
    Returns calibrated spacing tokens for compact, balanced, or spacious UI.
    """
    density_profiles = {
        "compact": {  # Dashboards, data-dense tools, data grids
            "base_grid": "4px / 8px",
            "component_padding": {
                "button": "px-3 py-1.5 text-xs sm:text-sm min-h-[36px]",
                "input": "px-2.5 py-1.5 text-sm",
                "card": "p-3 sm:p-4",
                "dialog": "p-4 sm:p-6 max-w-lg",
                "section": "py-6 sm:py-8",
                "table_cell": "px-3 py-2 text-xs",
            },
            "gaps": {
                "inline_items": "gap-1.5",
                "form_fields": "gap-3",
                "card_grid": "gap-3 sm:gap-4",
                "section_stack": "space-y-6",
            },
            "containers": {
                "readable_prose": "max-w-prose",
                "content_container": "max-w-6xl mx-auto px-4 sm:px-6",
                "wide_container": "max-w-7xl mx-auto px-4 sm:px-6",
            }
        },
        "balanced": {  # Modern SaaS, apps, portfolios, general web
            "base_grid": "8px primary, 4px micro-adjustments",
            "component_padding": {
                "button": "px-4 py-2.5 text-sm font-medium min-h-[44px]",
                "input": "px-3.5 py-2.5 text-sm",
                "card": "p-5 sm:p-6",
                "dialog": "p-6 sm:p-8 max-w-lg",
                "section": "py-16 md:py-24",
                "table_cell": "px-4 py-3 text-sm",
            },
            "gaps": {
                "inline_items": "gap-2 sm:gap-3",
                "form_fields": "gap-4",
                "card_grid": "gap-6 lg:gap-8",
                "section_stack": "space-y-16 md:space-y-24",
            },
            "containers": {
                "readable_prose": "max-w-prose (65ch)",
                "content_container": "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8",
                "wide_container": "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            }
        },
        "spacious": {  # Luxury, editorial, marketing landing pages
            "base_grid": "8px / 16px rhythm",
            "component_padding": {
                "button": "px-6 py-3.5 text-base font-medium min-h-[48px]",
                "input": "px-4 py-3 text-base",
                "card": "p-8 sm:p-10",
                "dialog": "p-8 sm:p-12 max-w-xl",
                "section": "py-24 md:py-32",
                "table_cell": "px-6 py-4 text-sm",
            },
            "gaps": {
                "inline_items": "gap-4",
                "form_fields": "gap-6",
                "card_grid": "gap-8 lg:gap-10",
                "section_stack": "space-y-24 md:space-y-32",
            },
            "containers": {
                "readable_prose": "max-w-2xl mx-auto",
                "content_container": "max-w-5xl mx-auto px-6 lg:px-12",
                "wide_container": "max-w-7xl mx-auto px-6 lg:px-12",
            }
        }
    }
    profile = density_profiles.get(density.lower(), density_profiles["balanced"])
    return {
        "density": density,
        "grid_rules": "Strict 8pt grid for layouts/cards, 4pt for micro spacing (tags, icons, buttons)",
        "scale_tokens": {
            "2xs": "4px (0.25rem / tw: 1)",
            "xs": "8px (0.5rem / tw: 2)",
            "sm": "12px (0.75rem / tw: 3)",
            "md": "16px (1rem / tw: 4)",
            "lg": "24px (1.5rem / tw: 6)",
            "xl": "32px (2rem / tw: 8)",
            "2xl": "48px (3rem / tw: 12)",
            "3xl": "64px (4rem / tw: 16)",
            "4xl": "96px (6rem / tw: 24)"
        },
        "specifications": profile
    }

def audit_spacing(code_snippet: str) -> Dict[str, Any]:
    """
    Audits UI code (HTML/Tailwind/CSS/JSX) for spacing, rhythm, and layout defects.
    """
    violations = []
    
    # 1. Check for non-standard arbitrary pixel values in Tailwind e.g. p-[13px], m-[17px], gap-[23px]
    arbitrary_spacing_matches = re.finditer(r'(?:p|m|gap|top|bottom|left|right|space-[xy])(?:-[tblrxy])?-\[(\d+)px\]', code_snippet)
    for m in arbitrary_spacing_matches:
        px = int(m.group(1))
        if px not in STANDARD_8PT_PX:
            target_px = closest_8pt(px)
            tw_equiv = TAILWIND_SPACING_MAP.get(target_px, str(target_px // 4))
            violations.append({
                "severity": "WARNING",
                "type": "non_standard_spacing",
                "found": m.group(0),
                "issue": f"{px}px breaks the 4px/8px spatial rhythm.",
                "fix": f"Replace with standard {target_px}px class (e.g. standard Tailwind scale: -{tw_equiv})"
            })

    # 2. Check for button tap target size in HTML/JSX (<button> or role="button")
    button_matches = re.finditer(r'<button[^>]*class(?:Name)?=["\']([^"\']*)["\']', code_snippet, re.IGNORECASE)
    for m in button_matches:
        classes = m.group(1).split()
        has_min_height = any("min-h-" in c or "h-" in c for c in classes)
        has_py = any(c.startswith("py-") for c in classes)
        # Check if py is too small, e.g. py-0.5, py-1, py-1.5 without explicit height >= 44px
        if not has_min_height:
            cramped_py = any(c in ["py-0", "py-0.5", "py-1"] for c in classes)
            if cramped_py or not has_py:
                violations.append({
                    "severity": "CRITICAL",
                    "type": "inaccessible_touch_target",
                    "found": f"<button class='{m.group(1)}'>",
                    "issue": "Touch target likely < 44px (fails WCAG 2.5.5 accessibility).",
                    "fix": "Add `min-h-[44px]` or ensure `py-2.5 px-4 inline-flex items-center justify-center`"
                })

    # 3. Check for unconstrained prose/paragraphs (text without max-width)
    p_matches = re.finditer(r'<p[^>]*class(?:Name)?=["\']([^"\']*)["\']', code_snippet, re.IGNORECASE)
    for m in p_matches:
        classes = m.group(1)
        if len(classes) > 0 and not any(w in classes for w in ["max-w-", "truncate", "line-clamp"]):
            # If paragraph has font styling but no max-width in wide containers
            if "text-base" in classes or "text-lg" in classes or "text-sm" in classes:
                violations.append({
                    "severity": "SUGGESTION",
                    "type": "unconstrained_reading_length",
                    "found": f"<p class='{classes}'>",
                    "issue": "Body text line length may stretch across full width, reducing readability (optimal is 50-75 chars).",
                    "fix": "Add `max-w-prose` or `max-w-xl` / `max-w-2xl`."
                })

    # 4. Check for section padding in landing pages/sites
    section_matches = re.finditer(r'<section[^>]*class(?:Name)?=["\']([^"\']*)["\']', code_snippet, re.IGNORECASE)
    for m in section_matches:
        classes = m.group(1)
        # If py is very small on section
        cramped_section = re.search(r'\bpy-(?:1|2|3|4|6|8)\b', classes)
        if cramped_section and not ("md:py-" in classes or "lg:py-" in classes):
            violations.append({
                "severity": "WARNING",
                "type": "cramped_section_padding",
                "found": f"<section class='{classes}'>",
                "issue": f"{cramped_section.group(0)} on <section> makes the page feel suffocated.",
                "fix": "Use responsive section breathing room: `py-16 md:py-24` or `py-12 lg:py-20`."
            })

    # 5. Check flex containers with multiple children lacking gap
    flex_matches = re.finditer(r'class(?:Name)?=["\']([^"\']*\bflex\b[^"\']*)["\']', code_snippet)
    for m in flex_matches:
        classes = m.group(1)
        if "gap-" not in classes and "space-x-" not in classes and "space-y-" not in classes and "justify-between" not in classes:
            violations.append({
                "severity": "SUGGESTION",
                "type": "missing_flex_gap",
                "found": f"class='{classes}'",
                "issue": "Flex container without explicit `gap-*` may cause sibling items to collide.",
                "fix": "Add `gap-2` (micro items), `gap-4` (standard), or `gap-6` (cards/sections)."
            })

    # 6. Check Card internal padding consistency
    card_matches = re.finditer(r'class(?:Name)?=["\']([^"\']*(?:rounded-|border|shadow)[^"\']*)["\']', code_snippet)
    for m in card_matches:
        classes = m.group(1)
        if ("rounded-xl" in classes or "rounded-2xl" in classes) and ("p-1" in classes or "p-2" in classes):
            violations.append({
                "severity": "WARNING",
                "type": "cramped_card_padding",
                "found": f"class='{classes}'",
                "issue": "Card container has cramped padding (p-1/p-2) which suffocates contents.",
                "fix": "Use `p-5 sm:p-6` for standard cards or `p-4` for compact list items."
            })

    # Calculate overall health score
    critical_cnt = sum(1 for v in violations if v["severity"] == "CRITICAL")
    warning_cnt = sum(1 for v in violations if v["severity"] == "WARNING")
    suggestion_cnt = sum(1 for v in violations if v["severity"] == "SUGGESTION")
    
    score = max(0, 100 - (critical_cnt * 25 + warning_cnt * 10 + suggestion_cnt * 5))
    status = "EXCELLENT" if score >= 90 else "GOOD" if score >= 75 else "NEEDS_IMPROVEMENT" if score >= 50 else "POOR"

    return {
        "status": status,
        "score": score,
        "violation_count": len(violations),
        "violations": violations[:6],  # Keep token count tight
        "quick_rules": [
            "Use 8pt grid (8, 16, 24, 32, 48, 64px) for layouts and cards.",
            "Use 4pt (4, 12, 20px) only for micro alignments (tags, buttons, icons).",
            "Buttons must have min 44x44px clickable target.",
            "Sections need py-16 md:py-24 for breathing room.",
            "Body copy requires max-w-prose (65ch) constraint."
        ]
    }
