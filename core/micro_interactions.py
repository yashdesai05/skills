"""Micro-Interactions and Animation Engine for UI/UX Pro MCP.
Provides CSS, Tailwind, and GSAP micro-interaction recipes for high-end UI feel.
"""

from typing import Dict, Any

INTERACTIONS: Dict[str, Dict[str, Any]] = {
    "button_press": {
        "name": "Tactile Button Press",
        "tailwind": "transition-all duration-150 ease-out active:scale-[0.97] hover:brightness-105 active:brightness-95",
        "css": """.btn-tactile {
  transition: transform 120ms cubic-bezier(0.16, 1, 0.3, 1), filter 120ms ease;
}
.btn-tactile:hover {
  transform: translateY(-1px);
}
.btn-tactile:active {
  transform: scale(0.97) translateY(0);
}""",
        "tip": "Gives physical responsiveness without distracting bouncy physics."
    },
    "card_hover": {
        "name": "Subtle Card Lift & Border Glow",
        "tailwind": "transition-all duration-200 ease-out hover:-translate-y-1 hover:border-primary/50 hover:shadow-xl",
        "css": """.card-hover {
  transition: transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease;
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -10px rgba(0, 0, 0, 0.15);
}""",
        "tip": "Keep vertical lift subtle (between -2px and -4px) to preserve reading flow."
    },
    "modal_dialog": {
        "name": "Smooth Dialog Entrance",
        "tailwind": "animate-in fade-in zoom-in-95 duration-200 ease-out",
        "css": """@keyframes modalEnter {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
.modal-enter {
  animation: modalEnter 200ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}""",
        "tip": "Always pair with background backdrop-blur-sm for depth separation."
    },
    "stagger_reveal": {
        "name": "Staggered List / Grid Reveal (GSAP / CSS)",
        "tailwind": "Use CSS animation delay: [&>*:nth-child(1)]:delay-75 [&>*:nth-child(2)]:delay-150 ...",
        "gsap": """gsap.from(".stagger-item", {
  y: 20,
  opacity: 0,
  duration: 0.5,
  stagger: 0.08,
  ease: "power2.out"
});""",
        "tip": "Stagger interval should be 0.05s - 0.08s. Longer intervals feel sluggish."
    },
    "skeleton_shimmer": {
        "name": "Fluid Skeleton Loading Shimmer",
        "tailwind": "animate-pulse bg-surface-hover rounded-md",
        "css": """.shimmer {
  background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0.03) 100%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
}
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}""",
        "tip": "Maintain the exact height/width of final rendered content to prevent layout shifts (CLS)."
    }
}

def get_micro_interaction(interaction_type: str = "button_press") -> Dict[str, Any]:
    """
    Returns high-performance micro-interaction snippet and parameters.
    """
    key = interaction_type.lower().replace("-", "_").replace(" ", "_")
    matched = INTERACTIONS.get(key)
    if not matched:
        match_key = next((k for k in INTERACTIONS if k in key or key in k), "button_press")
        matched = INTERACTIONS[match_key]

    return {
        "interaction": interaction_type,
        "name": matched["name"],
        "tailwind": matched.get("tailwind"),
        "css": matched.get("css"),
        "gsap": matched.get("gsap"),
        "best_practice": matched["tip"]
    }
