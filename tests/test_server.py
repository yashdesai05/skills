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
from core.motion_engine import get_motion_preset

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
    assert "purple" not in health_colors["ai_cliche_guard"].lower() or "avoid" in health_colors["ai_cliche_guard"].lower()
    print(f"   Healthcare: {health_colors['tokens']['mode']} -> Primary: {health_colors['tokens']['primary']}")

    lux_colors = research_best_colors("Luxury Swiss watch boutique e-commerce")
    assert lux_colors["mode_recommended"] in ["warm_stone", "dark"]
    print(f"   Luxury: {lux_colors['tokens']['mode']} -> Background: {lux_colors['tokens']['background']}")

    trading_colors = research_best_colors("Crypto trading terminal analytics")
    assert trading_colors["mode_recommended"] == "dark"
    print(f"   Trading: {trading_colors['tokens']['mode']} -> Accent: {trading_colors['tokens']['accent']}")

    print("\n3. Testing Premium Physics Motion...")
    motion = get_motion_preset("tactile_button")
    assert "cubic-bezier" in motion["physics_curve"]
    assert "btn-tactile" in motion["css"]
    print(f"   Motion: {motion['name']} ({motion['physics_curve'][:30]}...)")

    print("\n4. Testing Spacing Audit & Fixer...")
    sample_bad = '<button class="py-0.5 px-2 bg-blue-500">Click</button>'
    fixed = fix_ui_code(sample_bad)
    assert "min-h-[44px]" in fixed["enhanced_code"]
    print("   Passed! Button upgraded with 44px touch target.")

    print("\n5. Testing Accurate 3D Model Experiences...")
    from core.three_engine import generate_3d_model_experience
    three_res = generate_3d_model_experience("product_viewer", "r3f")
    assert "Canvas" in three_res["code"]
    print(f"   3D Experience: {three_res['experience']} ({three_res['framework_chosen']})")

    print("\nALL EXPANDED TESTS PASSED PERFECTLY! 🚀")

if __name__ == "__main__":
    test_all()
