"""Design Intelligence Search for UI/UX Pro MCP.
Performs fast keyword matching across curated design styles, palettes, and UX guidelines.
Outputs compact, token-optimized recommendations.
"""

import os
import csv
from typing import Dict, Any, List

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def search_intel(query: str, domain: str = "all") -> Dict[str, Any]:
    """
    Searches UI/UX dataset for styles, palettes, typography, or UX guidelines.
    Returns maximum 2-3 most relevant results in minimal tokens.
    """
    query_terms = [t.lower() for t in query.split() if len(t) > 2]
    results: List[Dict[str, Any]] = []

    # 1. Search UX guidelines
    if domain in ["all", "ux", "guidelines"] and os.path.exists(os.path.join(DATA_DIR, "ux-guidelines.csv")):
        try:
            with open(os.path.join(DATA_DIR, "ux-guidelines.csv"), mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    text_blob = f"{row.get('Category', '')} {row.get('Issue', '')} {row.get('Description', '')} {row.get('Do', '')}".lower()
                    if any(term in text_blob for term in query_terms):
                        results.append({
                            "type": "UX Guideline",
                            "topic": f"{row.get('Category')}: {row.get('Issue')}",
                            "rule": row.get('Description'),
                            "do": row.get('Do'),
                            "dont": row.get('Don\'t')
                        })
                        if len(results) >= 2:
                            break
        except Exception:
            pass

    # 2. Search Styles
    if (len(results) < 2 and domain in ["all", "style"]) and os.path.exists(os.path.join(DATA_DIR, "styles.csv")):
        try:
            with open(os.path.join(DATA_DIR, "styles.csv"), mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Column 1 or Style name
                    style_name = row.get("Style Name") or list(row.values())[1] if len(row) > 1 else ""
                    keywords = row.get("Keywords", "")
                    text_blob = f"{style_name} {keywords}".lower()
                    if any(term in text_blob for term in query_terms):
                        results.append({
                            "type": "Aesthetic Style",
                            "style": style_name,
                            "keywords": keywords[:120],
                            "recommendation": row.get("Best For", "")[:100]
                        })
                        if len(results) >= 3:
                            break
        except Exception:
            pass

    # 3. Search Colors / Palettes
    if (len(results) < 2 and domain in ["all", "color", "palette"]) and os.path.exists(os.path.join(DATA_DIR, "colors.csv")):
        try:
            with open(os.path.join(DATA_DIR, "colors.csv"), mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = row.get("Product Type", "")
                    if any(term in product.lower() for term in query_terms):
                        results.append({
                            "type": "Color Palette",
                            "product_type": product,
                            "primary": row.get("Primary"),
                            "background": row.get("Background"),
                            "accent": row.get("Accent"),
                            "note": row.get("Notes", "")
                        })
                        if len(results) >= 3:
                            break
        except Exception:
            pass

    if not results:
        # Fallback helpful tip
        results.append({
            "type": "General Rule",
            "rule": "Prioritize 8pt spatial grid, minimum 4.5:1 text contrast ratio, and 44x44px mobile touch targets."
        })

    return {
        "query": query,
        "results_count": len(results),
        "guidance": results[:3]
    }
