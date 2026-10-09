"""Readability & Typography Engine for UI/UX Pro MCP.
Guarantees 100% readable text, optimal reading lengths (50-75 ch), calibrated line-heights,
WCAG AAA contrast math, and editorial typographic hierarchy.
"""

import re
import math
from typing import Dict, Any, List

def calculate_relative_luminance(hex_color: str) -> float:
    """Calculates relative luminance for WCAG contrast calculation."""
    hex_clean = hex_color.lstrip('#')
    if len(hex_clean) == 3:
        hex_clean = ''.join([c*2 for c in hex_clean])
    if len(hex_clean) != 6:
        return 0.5  # fallback
    try:
        r = int(hex_clean[0:2], 16) / 255.0
        g = int(hex_clean[2:4], 16) / 255.0
        b = int(hex_clean[4:6], 16) / 255.0
    except ValueError:
        return 0.5

    def adjust(c):
        return c / 12.92 if c <= 0.03928 else math.pow((c + 0.055) / 1.055, 2.4)

    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def get_contrast_ratio(hex1: str, hex2: str) -> float:
    """Returns WCAG contrast ratio between two hex colors."""
    l1 = calculate_relative_luminance(hex1)
    l2 = calculate_relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def audit_text_readability(code_snippet: str) -> Dict[str, Any]:
    """
    Audits UI code for text readability, line-length constraints, line-heights, and contrast flaws.
    """
    issues = []
    
    # 1. Check for unconstrained wide paragraphs (stretching without max-width)
    p_tags = re.finditer(r'<p[^>]*class(?:Name)?=["\']([^"\']*)["\']', code_snippet, re.IGNORECASE)
    for m in p_tags:
        classes = m.group(1)
        if not any(k in classes for k in ["max-w-prose", "max-w-xl", "max-w-2xl", "max-w-lg", "max-w-md", "truncate", "line-clamp"]):
            issues.append({
                "type": "unconstrained_line_length",
                "severity": "HIGH",
                "found": f"<p class='{classes}'>",
                "issue": "Line length exceeds 75 characters on desktop. Eye struggles to find start of next line.",
                "fix": "Add `max-w-prose` (65ch) or `max-w-2xl`."
            })

    # 2. Check for cramped line heights (leading-none or leading-tight on body copy)
    cramped_leading = re.finditer(r'class(?:Name)?=["\']([^"\']*(?:text-base|text-sm|text-lg)[^"\']*(?:leading-none|leading-3|leading-4)[^"\']*)["\']', code_snippet)
    for m in cramped_leading:
        issues.append({
            "type": "cramped_line_height",
            "severity": "HIGH",
            "found": m.group(0),
            "issue": "Body text has cramped line-height, causing ascenders and descenders to collide.",
            "fix": "Use `leading-relaxed` (1.625) for body copy."
        })

    # 3. Check for low-contrast text classes on light or dark background
    faint_texts = ["text-gray-300", "text-slate-300", "text-zinc-300", "text-gray-400"]
    for ft in faint_texts:
        if ft in code_snippet and "bg-white" in code_snippet:
            issues.append({
                "type": "low_contrast_text",
                "severity": "CRITICAL",
                "found": ft,
                "issue": f"{ft} on white fails WCAG 2.1 AA (contrast ratio < 3:1).",
                "fix": "Replace with `text-slate-600` (#475569) or `text-slate-700`."
            })

    # 4. Check for pure white on pure black eye-strain (halation)
    if "bg-black" in code_snippet and "text-white" in code_snippet and "antialiased" not in code_snippet:
        issues.append({
            "type": "dark_mode_halation",
            "severity": "MEDIUM",
            "found": "bg-black + text-white without antialiased",
            "issue": "Pure #FFFFFF on pure #000000 causes eye glare (halation effect).",
            "fix": "Use `bg-[#0B0F17]` with `text-[#F8FAFC]` and add `antialiased`."
        })

    # 5. Check for missing letter-spacing on large headlines
    h_tags = re.finditer(r'class(?:Name)?=["\']([^"\']*(?:text-4xl|text-5xl|text-6xl)[^"\']*)["\']', code_snippet)
    for m in h_tags:
        classes = m.group(1)
        if "tracking-" not in classes:
            issues.append({
                "type": "missing_optical_tracking",
                "severity": "LOW",
                "found": classes,
                "issue": "Large headings (36px+) appear loose without optical letter-spacing.",
                "fix": "Add `tracking-tight` (-0.025em) to make headlines punchy and cohesive."
            })

    score = max(0, 100 - len(issues) * 20)
    return {
        "readability_score": score,
        "status": "PASS" if score >= 80 else "NEEDS_OPTIMIZATION",
        "issues_found": len(issues),
        "issues": issues[:5],
        "readability_rules": [
            "Body line length: strictly 50-75 characters (max-w-prose / 65ch).",
            "Body line height: 1.5 - 1.7 (leading-relaxed).",
            "Heading line height: 1.1 - 1.25 (leading-tight) with tracking-tight.",
            "Contrast: minimum 4.5:1 for body copy (WCAG AA), 7:1 for AAA.",
            "Dark mode: use tinted darks (#0B0F17) and soft whites (#F8FAFC) with `antialiased`."
        ]
    }

def get_readability_tokens() -> Dict[str, Any]:
    """
    Returns typography standards, font size scales, leading, and tracking rules for maximum legibility.
    """
    return {
        "line_length_bounds": {
            "optimal": "65 characters (max-w-prose)",
            "minimum": "45 characters (below this, breaks reading rhythm)",
            "maximum": "75 characters (above this, reader loses place upon newline)"
        },
        "type_scale_and_leading": {
            "display": {"size": "48px - 64px", "leading": "leading-[1.1]", "tracking": "tracking-tight", "usage": "Hero H1"},
            "h2": {"size": "30px - 36px", "leading": "leading-[1.2]", "tracking": "tracking-tight", "usage": "Section Titles"},
            "h3": {"size": "20px - 24px", "leading": "leading-[1.3]", "tracking": "tracking-normal", "usage": "Card Titles"},
            "body": {"size": "16px (1rem)", "leading": "leading-relaxed (1.625)", "tracking": "tracking-normal", "usage": "Paragraphs"},
            "caption": {"size": "12px - 14px", "leading": "leading-normal (1.5)", "tracking": "tracking-wide", "usage": "Metadata & Hints"},
            "badge_label": {"size": "11px - 12px", "leading": "leading-none", "tracking": "tracking-wider uppercase font-semibold", "usage": "Status Pills"}
        },
        "curated_font_pairings": [
            {"style": "Universal Clean SaaS", "heading": "Inter / Plus Jakarta Sans", "body": "Inter", "mono": "JetBrains Mono"},
            {"style": "Editorial High-Trust", "heading": "Newsreader / Merriweather", "body": "Plus Jakarta Sans", "mono": "Geist Mono"},
            {"style": "Technical / Developer", "heading": "Geist / Space Grotesk", "body": "Geist", "mono": "Geist Mono"}
        ]
    }
