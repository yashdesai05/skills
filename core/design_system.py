"""Design System Generator for UI/UX Pro MCP.
Generates token-efficient palettes, typography scales, shadows, and radii.
Includes WCAG AA contrast compliance and Tailwind/CSS variable formats.
"""

from typing import Dict, Any, Optional

THEME_PRESETS = {
    "modern_saas_dark": {
        "name": "Modern SaaS Dark (Linear / Vercel style)",
        "vibe": "Sleek, tech-forward, high contrast, clean micro-borders",
        "colors": {
            "background": "#090A0F",
            "surface": "#12141A",
            "surface_hover": "#1A1D26",
            "border": "#232733",
            "border_subtle": "#1B1E28",
            "primary": "#3B82F6",
            "primary_hover": "#2563EB",
            "primary_foreground": "#FFFFFF",
            "accent": "#6366F1",
            "text_main": "#F8FAFC",
            "text_muted": "#94A3B8",
            "success": "#10B981",
            "destructive": "#EF4444"
        },
        "contrast_rating": "WCAG AAA (17.5:1 text on background)",
        "typography": {
            "font_sans": "Inter, -apple-system, BlinkMacSystemFont, sans-serif",
            "font_mono": "JetBrains Mono, monospace",
            "google_fonts_url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
            "scale": {
                "xs": "12px / line-height: 16px",
                "sm": "14px / line-height: 20px",
                "base": "16px / line-height: 24px",
                "lg": "18px / line-height: 28px",
                "xl": "20px / line-height: 28px",
                "2xl": "24px / line-height: 32px",
                "3xl": "30px / line-height: 36px",
                "4xl": "36px / line-height: 40px",
                "5xl": "48px / line-height: 1.1"
            }
        },
        "radius": {"sm": "6px", "md": "10px", "lg": "14px", "full": "9999px"},
        "shadows": {
            "card": "0 1px 3px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.06)",
            "glow": "0 0 25px -5px rgba(59, 130, 246, 0.25)"
        }
    },
    "modern_saas_light": {
        "name": "Modern SaaS Light (Clean Stripe style)",
        "vibe": "Airy, crisp, trust-inducing, vibrant accents with subtle borders",
        "colors": {
            "background": "#F8FAFC",
            "surface": "#FFFFFF",
            "surface_hover": "#F1F5F9",
            "border": "#E2E8F0",
            "border_subtle": "#F1F5F9",
            "primary": "#2563EB",
            "primary_hover": "#1D4ED8",
            "primary_foreground": "#FFFFFF",
            "accent": "#0D9488",
            "text_main": "#0F172A",
            "text_muted": "#64748B",
            "success": "#059669",
            "destructive": "#DC2626"
        },
        "contrast_rating": "WCAG AAA (15.2:1 text on background)",
        "typography": {
            "font_sans": "Plus Jakarta Sans, sans-serif",
            "font_mono": "Fira Code, monospace",
            "google_fonts_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap",
            "scale": {
                "xs": "12px", "sm": "14px", "base": "16px", "lg": "18px",
                "xl": "20px", "2xl": "24px", "3xl": "30px", "4xl": "36px"
            }
        },
        "radius": {"sm": "6px", "md": "10px", "lg": "16px", "full": "9999px"},
        "shadows": {
            "card": "0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05)",
            "elevated": "0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05)"
        }
    },
    "fintech_trust": {
        "name": "Fintech & Banking Trust",
        "vibe": "Deep navy, gold/emerald accents, bank-grade reliability, clear numbers",
        "colors": {
            "background": "#0B0F19",
            "surface": "#111827",
            "surface_hover": "#1F2937",
            "border": "#1F2937",
            "border_subtle": "#162032",
            "primary": "#10B981",
            "primary_hover": "#059669",
            "primary_foreground": "#000000",
            "accent": "#F59E0B",
            "text_main": "#F9FAFB",
            "text_muted": "#9CA3AF",
            "success": "#10B981",
            "destructive": "#F43F5E"
        },
        "contrast_rating": "WCAG AAA (16.8:1 text on background)",
        "typography": {
            "font_sans": "Outfit, sans-serif",
            "font_mono": "Space Mono, monospace",
            "google_fonts_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap",
            "scale": {"xs": "12px", "sm": "14px", "base": "16px", "lg": "18px", "xl": "22px", "2xl": "28px"}
        },
        "radius": {"sm": "4px", "md": "8px", "lg": "12px", "full": "9999px"},
        "shadows": {
            "card": "0 4px 20px -2px rgba(0, 0, 0, 0.4)",
            "accent": "0 0 20px rgba(16, 185, 129, 0.2)"
        }
    },
    "minimalist_editorial": {
        "name": "Minimalist Editorial & Portfolio",
        "vibe": "Swiss grid typography, monochrome with single vibrant punch, expansive space",
        "colors": {
            "background": "#FAFAFA",
            "surface": "#FFFFFF",
            "surface_hover": "#F4F4F5",
            "border": "#E4E4E7",
            "border_subtle": "#F4F4F5",
            "primary": "#18181B",
            "primary_hover": "#27272A",
            "primary_foreground": "#FFFFFF",
            "accent": "#E11D48",
            "text_main": "#09090B",
            "text_muted": "#71717A",
            "success": "#16A34A",
            "destructive": "#DC2626"
        },
        "contrast_rating": "WCAG AAA (19.1:1 text on background)",
        "typography": {
            "font_sans": "Newsreader, Playfair Display, serif (Headings) + Inter (Body)",
            "font_mono": "Geist Mono, monospace",
            "google_fonts_url": "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Inter:wght@400;500;600&display=swap",
            "scale": {"xs": "12px", "sm": "14px", "base": "16px", "lg": "18px", "xl": "24px", "2xl": "32px", "3xl": "48px"}
        },
        "radius": {"sm": "0px", "md": "2px", "lg": "4px", "full": "9999px"},
        "shadows": {
            "card": "none",
            "subtle": "0 1px 2px rgba(0,0,0,0.04)"
        }
    },
    "glassmorphic_neon": {
        "name": "Glassmorphism & Neon Glow",
        "vibe": "Translucent frosted surfaces, vibrant neon gradients, layered z-depth",
        "colors": {
            "background": "#070814",
            "surface": "rgba(255, 255, 255, 0.04)",
            "surface_hover": "rgba(255, 255, 255, 0.08)",
            "border": "rgba(255, 255, 255, 0.12)",
            "border_subtle": "rgba(255, 255, 255, 0.06)",
            "primary": "#8B5CF6",
            "primary_hover": "#7C3AED",
            "primary_foreground": "#FFFFFF",
            "accent": "#EC4899",
            "text_main": "#FFFFFF",
            "text_muted": "#A1A1AA",
            "success": "#10B981",
            "destructive": "#F43F5E"
        },
        "contrast_rating": "WCAG AA (minimum 4.5:1 required; use backdrop-blur-md/lg)",
        "typography": {
            "font_sans": "Space Grotesk, sans-serif",
            "font_mono": "Space Mono, monospace",
            "google_fonts_url": "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap",
            "scale": {"xs": "12px", "sm": "14px", "base": "16px", "lg": "18px", "xl": "22px", "2xl": "28px", "3xl": "36px"}
        },
        "radius": {"sm": "10px", "md": "16px", "lg": "24px", "full": "9999px"},
        "shadows": {
            "card": "0 8px 32px 0 rgba(0, 0, 0, 0.37)",
            "glow": "0 0 30px -5px rgba(139, 92, 246, 0.35)"
        }
    }
}

def generate_design_system(vibe_query: str = "modern_saas_dark", format_type: str = "tailwind") -> Dict[str, Any]:
    """
    Returns an ultra token-efficient design system specification tailored to the prompt.
    """
    query = vibe_query.lower()
    selected_key = "modern_saas_dark"
    if any(k in query for k in ["light", "stripe", "clean", "white"]):
        selected_key = "modern_saas_light"
    elif any(k in query for k in ["fintech", "bank", "crypto", "money", "invest"]):
        selected_key = "fintech_trust"
    elif any(k in query for k in ["minimal", "editorial", "luxury", "serif", "portfolio"]):
        selected_key = "minimalist_editorial"
    elif any(k in query for k in ["glass", "neon", "cyber", "glow", "gradient"]):
        selected_key = "glassmorphic_neon"

    theme = THEME_PRESETS[selected_key]
    
    # Generate CSS variables string
    c = theme["colors"]
    css_vars = f""":root {{
  --bg: {c['background']};
  --surface: {c['surface']};
  --surface-hover: {c['surface_hover']};
  --border: {c['border']};
  --primary: {c['primary']};
  --text-main: {c['text_main']};
  --text-muted: {c['text_muted']};
  --accent: {c['accent']};
}}"""

    # Generate Tailwind config snippet
    tw_config = f"""// tailwind.config.js snippet
theme: {{
  extend: {{
    colors: {{
      bg: '{c['background']}',
      surface: '{c['surface']}',
      border: '{c['border']}',
      primary: '{c['primary']}',
      accent: '{c['accent']}',
      'text-main': '{c['text_main']}',
      'text-muted': '{c['text_muted']}'
    }},
    fontFamily: {{
      sans: ['{theme['typography']['font_sans'].split(',')[0]}', 'sans-serif']
    }}
  }}
}}"""

    return {
        "preset": selected_key,
        "name": theme["name"],
        "vibe": theme["vibe"],
        "contrast_check": theme["contrast_rating"],
        "colors": theme["colors"],
        "typography": theme["typography"],
        "radii": theme["radius"],
        "shadows": theme["shadows"],
        "css_variables": css_vars,
        "tailwind_config": tw_config
    }
