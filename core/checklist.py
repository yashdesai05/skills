"""Pre-flight UX & Spacing Checklists for UI/UX Pro MCP.
Provides fast validation lists before shipping frontend code.
"""

from typing import Dict, Any, List

CHECKLISTS: Dict[str, List[str]] = {
    "spacing_and_layout": [
        "Strict 8pt rhythm applied to all container margins, card paddings, and section heights (8, 16, 24, 32, 48, 64px).",
        "4pt used only for micro elements (badges, icon offsets, compact buttons).",
        "Section vertical padding has sufficient breathing room (py-16 md:py-24).",
        "Body prose has maximum reading width constraint (max-w-prose / 65ch).",
        "Flexbox and Grid items have explicit gaps (no colliding siblings on narrow screens)."
    ],
    "accessibility_wcag": [
        "Contrast ratio >= 4.5:1 for body copy and >= 3:1 for large text/headings against backgrounds.",
        "Interactive buttons and touch targets meet minimum 44x44px dimensions.",
        "Focus states are visibly clear with ring / outline (e.g. focus-visible:ring-2 focus-visible:ring-primary).",
        "Color is not used as the sole indicator of state (pair with icons or text labels).",
        "Image tags have meaningful alt attributes or aria-hidden='true' for decorative icons."
    ],
    "responsive_mobile": [
        "Containers have horizontal safety padding on mobile (e.g., px-4 sm:px-6).",
        "Multi-column grids gracefully collapse to single column on mobile (grid-cols-1 md:grid-cols-3).",
        "No horizontal layout overflow (no fixed widths exceeding 100vw).",
        "Sticky headers account for viewport height and don't occlude anchor target scroll.",
        "Interactive modals/drawers are thumb-friendly with easily reachable close triggers."
    ],
    "pre_ship": [
        "Spacing: Strict 4px/8px spatial hierarchy checked across cards and sections.",
        "Contrast: Text readable in both light/dark variants.",
        "Tap targets: All buttons >= 44px min height.",
        "Transitions: Micro-interactions have subtle ease-out durations (150ms-250ms).",
        "Empty/Loading states: Skeleton screens or fallbacks present for async data."
    ]
}

def get_checklist(category: str = "pre_ship") -> Dict[str, Any]:
    """
    Returns a concise 5-point checklist for verifying UI quality.
    """
    cat = category.lower().replace("-", "_")
    matched_key = next((k for k in CHECKLISTS if k in cat or cat in k), "pre_ship")
    return {
        "category": matched_key,
        "items": CHECKLISTS[matched_key]
    }
