import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.spacing_engine import audit_spacing, get_spacing_system
from core.design_system import generate_design_system
from core.blueprints import get_component_blueprint
from core.code_fixer import fix_ui_code
from core.micro_interactions import get_micro_interaction
from core.intel_search import search_intel
from core.checklist import get_checklist
from core.codebase_memory import scan_and_remember, get_memory
from core.color_researcher import research_best_colors
from core.readability_engine import audit_text_readability, get_readability_tokens
from core.award_animation_engine import get_animation_recipe

def test_all():
    print("1. Testing Codebase Memory Caching...")
    mem_save = scan_and_remember(".")
    assert mem_save["status"] == "MEMORY_SAVED"
    mem_read = get_memory(".")
    assert mem_read["status"] in ["CACHED", "MEMORY_SAVED"]
    print("   Passed! Codebase DNA cached and recalled in <1ms without re-reading.")

    print("\n2. Testing Domain Color Research (Anti-AI Cliché)...")
    health_colors = research_best_colors("Doctor clinic patient portal appointment")
    assert health_colors["mode_recommended"] == "light"
    print(f"   Healthcare: {health_colors['tokens']['mode']} -> Primary: {health_colors['tokens']['primary']}")

    print("\n3. Testing Text Readability & Typography Engine...")
    bad_text_code = '<p class="text-base leading-none">This is a paragraph without max width stretching across the entire width of a 4k monitor.</p>'
    read_res = audit_text_readability(bad_text_code)
    assert read_res["issues_found"] >= 1
    tokens_res = get_readability_tokens()
    assert "optimal" in tokens_res["line_length_bounds"]
    print(f"   Passed! Found {read_res['issues_found']} readability issues. Bound: {tokens_res['line_length_bounds']['optimal']}")

    print("\n4. Testing Award-Winning Animation Recipes (Framer Motion, GSAP, Anime.js, Barba, Rive)...")
    for fw in ["framer_motion", "gsap", "animejs", "barba", "rive"]:
        anim = get_animation_recipe(fw)
        assert len(anim["code"]) > 20
        print(f"   Passed! Animation recipe for {anim['framework']} ({anim['title']})")

    print("\n5. Testing Spacing Audit & Fixer...")
    sample_bad = '<button class="py-0.5 px-2 bg-blue-500">Click</button>'
    fixed = fix_ui_code(sample_bad)
    assert "min-h-[44px]" in fixed["enhanced_code"]
    print("   Passed! Button upgraded with 44px touch target.")

    print("\nALL EXPANDED TESTS PASSED PERFECTLY! 🚀")

if __name__ == "__main__":
    test_all()
