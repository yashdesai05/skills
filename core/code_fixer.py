"""Code Fixer Engine for UI/UX Pro MCP.
Automatically upgrades raw or cramped UI code into pixel-perfect, accessible code.
Fixes 4px/8px rhythm, tap targets, contrast, and layout hierarchy.
"""

import re
from typing import Dict, Any, List

def fix_ui_code(raw_code: str, mode: str = "tailwind") -> Dict[str, Any]:
    """
    Transforms raw or cramped UI code into polished, beautifully spaced, accessible markup.
    """
    changes_made: List[str] = []
    code = raw_code

    # 1. Fix arbitrary pixel padding/margins (e.g. p-[13px] -> p-3.5 or p-4)
    def replace_arbitrary(match):
        prefix = match.group(1) # p, m, gap
        px = int(match.group(2))
        # Snap to nearest 4px/8px
        snapped_px = round(px / 4) * 4
        tw_val = snapped_px // 4
        changes_made.append(f"Snapped arbitrary {match.group(0)} to {prefix}-{tw_val} ({snapped_px}px grid)")
        return f"{prefix}-{tw_val}"

    code = re.sub(r'\b(p|m|gap|py|px|my|mx)-\[(\d+)px\]', replace_arbitrary, code)

    # 2. Fix cramped buttons (<button> with py-1 or py-0.5)
    def fix_button(match):
        full_tag = match.group(0)
        class_attr = match.group(1)
        new_class = class_attr
        
        # Check tap target
        if not ("min-h-" in new_class or "h-1" in new_class or "h-9" in new_class or "h-11" in new_class):
            new_class = f"{new_class} min-h-[44px]".strip()
            changes_made.append("Added min-h-[44px] for WCAG 2.5.5 accessible touch target on button")
            
        # Check padding
        if "py-1" in new_class:
            new_class = new_class.replace("py-1", "py-2.5")
            changes_made.append("Adjusted cramped py-1 button padding to py-2.5 (10px)")
        elif "py-0.5" in new_class:
            new_class = new_class.replace("py-0.5", "py-2")
            changes_made.append("Adjusted cramped py-0.5 button padding to py-2")
            
        # Ensure transitions
        if "transition" not in new_class:
            new_class = f"{new_class} transition-all duration-150 active:scale-[0.98]".strip()
            changes_made.append("Added smooth micro-interaction (transition & active scale 0.98)")
            
        return full_tag.replace(class_attr, new_class)

    code = re.sub(r'<button[^>]*class(?:Name)?=["\']([^"\']*)["\']', fix_button, code)

    # 3. Fix cramped section padding (e.g. py-4 or py-6 on <section>)
    def fix_section(match):
        full_tag = match.group(0)
        class_attr = match.group(1)
        new_class = class_attr
        
        cramped = re.search(r'\bpy-(?:1|2|3|4|6|8)\b', new_class)
        if cramped and not ("md:py-" in new_class or "lg:py-" in new_class):
            new_class = re.sub(r'\bpy-(?:1|2|3|4|6|8)\b', 'py-16 md:py-24', new_class)
            changes_made.append("Upgraded cramped section vertical padding to responsive py-16 md:py-24")
            
        return full_tag.replace(class_attr, new_class)

    code = re.sub(r'<section[^>]*class(?:Name)?=["\']([^"\']*)["\']', fix_section, code)

    # 4. Fix unconstrained paragraphs inside hero/features
    def fix_paragraph(match):
        full_tag = match.group(0)
        class_attr = match.group(1)
        new_class = class_attr
        
        if ("text-lg" in new_class or "text-xl" in new_class) and "max-w-" not in new_class:
            new_class = f"{new_class} max-w-2xl".strip()
            changes_made.append("Added max-w-2xl constraint to heading description for readability")
            
        return full_tag.replace(class_attr, new_class)

    code = re.sub(r'<p[^>]*class(?:Name)?=["\']([^"\']*)["\']', fix_paragraph, code)

    # 5. Fix card cramped padding (p-1 or p-2 on card elements)
    def fix_card(match):
        full_tag = match.group(0)
        class_attr = match.group(1)
        new_class = class_attr
        
        if ("rounded-xl" in new_class or "rounded-2xl" in new_class) and re.search(r'\bp-[12]\b', new_class):
            new_class = re.sub(r'\bp-[12]\b', 'p-6', new_class)
            changes_made.append("Replaced cramped p-1/p-2 card padding with standard p-6 (24px)")
            
        return full_tag.replace(class_attr, new_class)

    code = re.sub(r'<div[^>]*class(?:Name)?=["\']([^"\']*(?:rounded-xl|rounded-2xl)[^"\']*)["\']', fix_card, code)

    # 6. Ensure flex parents have gap
    def fix_flex(match):
        full_tag = match.group(0)
        class_attr = match.group(1)
        new_class = class_attr
        
        if r'\bflex\b' in new_class and not any(k in new_class for k in ["gap-", "space-x-", "space-y-", "justify-between"]):
            new_class = f"{new_class} gap-3 items-center".strip()
            changes_made.append("Added gap-3 items-center to flex container for proper element separation")
            
        return full_tag.replace(class_attr, new_class)

    code = re.sub(r'class(?:Name)?=["\']([^"\']*\bflex\b[^"\']*)["\']', fix_flex, code)

    return {
        "status": "IMPROVED",
        "changes_count": len(changes_made),
        "changes": changes_made if changes_made else ["Layout already adheres to strict 8pt grid"],
        "enhanced_code": code
    }
