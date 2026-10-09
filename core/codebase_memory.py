"""Codebase Memory Engine for UI/UX Pro MCP.
Scans and remembers project design tokens, Tailwind config, fonts, and frameworks.
Persists context to `.ui-ux-memory.json` so the LLM never has to re-scan files across turns.
Ultra token-efficient: retrieves full project design DNA in ~100 tokens.
"""

import os
import json
import re
from typing import Dict, Any, Optional

MEMORY_FILENAME = ".ui-ux-memory.json"

def scan_and_remember(project_path: str = ".") -> Dict[str, Any]:
    """
    Scans project directory for design tokens, typography, CSS frameworks, and saves to memory file.
    """
    abs_path = os.path.abspath(project_path)
    if not os.path.isdir(abs_path):
        return {"error": f"Directory not found: {abs_path}"}

    memory_file = os.path.join(abs_path, MEMORY_FILENAME)
    
    detected: Dict[str, Any] = {
        "project_root": abs_path,
        "framework": "unknown",
        "css_engine": "css",
        "has_tailwind": False,
        "ui_libraries": [],
        "fonts_detected": [],
        "primary_colors": [],
        "dark_mode_strategy": "class",
        "spacing_convention": "8pt_grid"
    }

    # 1. Inspect package.json if present
    pkg_path = os.path.join(abs_path, "package.json")
    if os.path.exists(pkg_path):
        try:
            with open(pkg_path, "r", encoding="utf-8") as f:
                pkg_data = json.load(f)
                deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
                
                # Framework detection
                if "next" in deps:
                    detected["framework"] = "nextjs"
                elif "react" in deps:
                    detected["framework"] = "react"
                elif "vue" in deps or "nuxt" in deps:
                    detected["framework"] = "vue"
                elif "svelte" in deps:
                    detected["framework"] = "svelte"
                elif "astro" in deps:
                    detected["framework"] = "astro"
                
                # CSS & UI libs
                if "tailwindcss" in deps:
                    detected["has_tailwind"] = True
                    detected["css_engine"] = "tailwind"
                if "gsap" in deps:
                    detected["ui_libraries"].append("gsap")
                if "framer-motion" in deps:
                    detected["ui_libraries"].append("framer-motion")
                if "@radix-ui/react-slot" in deps or "lucide-react" in deps:
                    detected["ui_libraries"].append("shadcn-ui")
                if "@mui/material" in deps:
                    detected["ui_libraries"].append("mui")
        except Exception:
            pass

    # 2. Inspect tailwind.config.* if present
    for tw_name in ["tailwind.config.js", "tailwind.config.ts", "tailwind.config.mjs"]:
        tw_path = os.path.join(abs_path, tw_name)
        if os.path.exists(tw_path):
            detected["has_tailwind"] = True
            detected["css_engine"] = "tailwind"
            try:
                with open(tw_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Check dark mode
                    if "darkMode:" in content:
                        dm_match = re.search(r"darkMode:\s*['\"]([^'\"]+)['\"]", content)
                        if dm_match:
                            detected["dark_mode_strategy"] = dm_match.group(1)
                    # Extract hex colors if defined
                    hex_matches = re.findall(r"#[0-9a-fA-F]{6}", content)
                    if hex_matches:
                        detected["primary_colors"] = list(set(hex_matches))[:4]
                    # Extract font families
                    font_matches = re.findall(r"['\"]font-[a-zA-Z0-9_-]+['\"]|fontFamily:\s*\{([^}]+)\}", content)
                    if font_matches:
                        detected["fonts_detected"].append("Custom Tailwind Font Config")
            except Exception:
                pass
            break

    # 3. Check for globals.css / index.css
    for css_subpath in ["src/app/globals.css", "src/globals.css", "src/index.css", "styles/globals.css", "index.css"]:
        full_css = os.path.join(abs_path, css_subpath)
        if os.path.exists(full_css):
            try:
                with open(full_css, "r", encoding="utf-8") as f:
                    css_content = f.read()
                    # Look for Google Fonts or font-family
                    font_imports = re.findall(r"family=([a-zA-Z+]+)", css_content)
                    if font_imports:
                        detected["fonts_detected"].extend([f.replace("+", " ") for f in font_imports])
                    # Look for root CSS variables
                    css_vars = re.findall(r"--([a-zA-Z0-9_-]+):\s*([^;]+);", css_content)
                    if css_vars:
                        detected["primary_colors"].extend([v[1].strip() for v in css_vars if "#" in v[1] or "hsl" in v[1]][:4])
            except Exception:
                pass
            break

    # Save to memory file
    try:
        with open(memory_file, "w", encoding="utf-8") as f:
            json.dump(detected, f, indent=2)
    except Exception as e:
        return {"error": f"Failed to persist memory: {str(e)}"}

    return {
        "status": "MEMORY_SAVED",
        "file": memory_file,
        "summary": {
            "framework": detected["framework"],
            "css_engine": detected["css_engine"],
            "ui_libraries": detected["ui_libraries"],
            "fonts": detected["fonts_detected"] if detected["fonts_detected"] else ["System UI / Inter"],
            "saved_colors": detected["primary_colors"],
            "spacing_rule": "Strict 8pt spatial grid"
        },
        "note": "Codebase DNA cached successfully. Future tool calls will use this memory with zero re-scanning."
    }

def get_memory(project_path: str = ".") -> Dict[str, Any]:
    """
    Instantly returns the cached codebase design memory without re-reading files.
    """
    abs_path = os.path.abspath(project_path)
    memory_file = os.path.join(abs_path, MEMORY_FILENAME)
    
    if os.path.exists(memory_file):
        try:
            with open(memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {
                    "status": "CACHED",
                    "framework": data.get("framework", "react"),
                    "css_engine": data.get("css_engine", "tailwind"),
                    "ui_libraries": data.get("ui_libraries", []),
                    "fonts": data.get("fonts_detected", ["Inter"]),
                    "colors": data.get("primary_colors", []),
                    "spacing": data.get("spacing_convention", "8pt_grid")
                }
        except Exception:
            pass

    # If no memory exists yet, trigger a lightweight scan
    return scan_and_remember(project_path)
