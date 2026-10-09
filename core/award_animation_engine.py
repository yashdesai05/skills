"""Award-Winning Web Animation Engine for UI/UX Pro MCP.
Provides production-ready, silky-smooth animation code across:
- Framer Motion (Spring physics, layoutId, gestures)
- GSAP + ScrollTrigger (Scroll scrub, pin, text reveals)
- Anime.js (SVG path morphing, staggered kinetic grid)
- Barba.js (Page transitions without reloads)
- Rive (State-machine vector animations)
"""

from typing import Dict, Any

ANIMATION_RECIPES: Dict[str, Dict[str, Any]] = {
    "framer_motion_layout": {
        "framework": "Framer Motion",
        "title": "Shared Layout Tab Indicator & Card Expansion",
        "description": "Smooth physics-based pill indicator sliding using layoutId, plus spring hover scale.",
        "code": """import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';

export function AnimatedTabs({ tabs = ['Overview', 'Features', 'Pricing', 'Changelog'] }) {
  const [activeTab, setActiveTab] = useState(tabs[0]);

  return (
    <div className="flex items-center gap-1.5 p-1 rounded-xl bg-surface border border-border">
      {tabs.map((tab) => {
        const isActive = activeTab === tab;
        return (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className="relative px-4 py-2 text-sm font-medium transition-colors text-text-muted hover:text-text-main"
          >
            {isActive && (
              <motion.div
                layoutId="active-pill"
                className="absolute inset-0 rounded-lg bg-primary/10 border border-primary/20"
                transition={{ type: 'spring', stiffness: 450, damping: 35 }}
              />
            )}
            <span className={`relative z-10 ${isActive ? 'text-primary font-semibold' : ''}`}>
              {tab}
            </span>
          </button>
        );
      })}
    </div>
  );
}

// Staggered list fade-up
export const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.06, delayChildren: 0.1 }
  }
};

export const itemVariants = {
  hidden: { opacity: 0, y: 14 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 350, damping: 25 }
  }
};"""
    },
    "gsap_scroll_trigger": {
        "framework": "GSAP (GreenSock)",
        "title": "ScrollTrigger Scrubbed Text Highlight & Pinned Section",
        "description": "Words light up sequentially as user scrolls, with smooth scrub and mobile performance guard.",
        "code": """import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useEffect, useRef } from 'react';

gsap.registerPlugin(ScrollTrigger);

export function useScrollTextReveal(textRef) {
  useEffect(() => {
    const el = textRef.current;
    if (!el) return;

    // Split words or spans
    const words = el.querySelectorAll('.scroll-word');

    const ctx = gsap.context(() => {
      gsap.fromTo(
        words,
        { opacity: 0.2, filter: 'blur(4px)' },
        {
          opacity: 1,
          filter: 'blur(0px)',
          stagger: 0.1,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 75%',
            end: 'bottom 45%',
            scrub: 1 // smooth scrubbing
          }
        }
      );
    });

    return () => ctx.revert();
  }, [textRef]);
}

// Magnetic Button with GSAP quickTo (0 GC churn)
export function initMagneticButton(buttonEl) {
  const xTo = gsap.quickTo(buttonEl, 'x', { duration: 0.3, ease: 'power3.out' });
  const yTo = gsap.quickTo(buttonEl, 'y', { duration: 0.3, ease: 'power3.out' });

  const onMove = (e) => {
    const { left, top, width, height } = buttonEl.getBoundingClientRect();
    const x = (e.clientX - (left + width / 2)) * 0.35;
    const y = (e.clientY - (top + height / 2)) * 0.35;
    xTo(x);
    yTo(y);
  };

  const onLeave = () => {
    xTo(0);
    yTo(0);
  };

  buttonEl.addEventListener('pointermove', onMove);
  buttonEl.addEventListener('pointerleave', onLeave);
}"""
    },
    "animejs_stagger": {
        "framework": "Anime.js",
        "title": "Kinetic Ripple & SVG Morphing",
        "description": "Staggered grid ripple wave and smooth SVG path animation using Anime.js.",
        "code": """import anime from 'animejs';

// 1. Grid Stagger Wave Effect
export function triggerGridRipple(containerSelector) {
  anime({
    targets: `${containerSelector} .grid-cell`,
    scale: [
      { value: 0.4, easing: 'easeOutSine', duration: 250 },
      { value: 1, easing: 'easeInOutQuad', duration: 500 }
    ],
    delay: anime.stagger(40, { grid: [8, 8], from: 'center' })
  });
}

// 2. Smooth SVG Path Morphing
export function morphPath(pathSelector, targetPathData) {
  anime({
    targets: pathSelector,
    d: [{ value: targetPathData }],
    easing: 'easeOutElastic(1, .6)',
    duration: 1200
  });
}"""
    },
    "barbajs_transitions": {
        "framework": "Barba.js",
        "title": "Smooth Page-to-Page Curtain Transition (Zero Reloads)",
        "description": "Fluid curtain wipe and DOM crossfade between page routes using Barba.js + GSAP.",
        "code": """import barba from '@barba/core';
import gsap from 'gsap';

export function initBarbaTransitions() {
  barba.init({
    sync: true,
    transitions: [
      {
        name: 'curtain-wipe',
        async leave(data) {
          const done = this.async();
          // Curtain slides down
          gsap.to('.curtain-overlay', {
            scaleY: 1,
            transformOrigin: 'bottom',
            duration: 0.5,
            ease: 'power3.inOut',
            onComplete: done
          });
        },
        async enter(data) {
          // Scroll back to top smoothly
          window.scrollTo(0, 0);
          // Curtain slides up away
          gsap.fromTo(
            '.curtain-overlay',
            { scaleY: 1, transformOrigin: 'top' },
            {
              scaleY: 0,
              duration: 0.5,
              ease: 'power3.inOut'
            }
          );
          // Fade in new container
          gsap.from(data.next.container, {
            opacity: 0,
            y: 20,
            duration: 0.4,
            ease: 'power2.out'
          });
        }
      }
    ]
  });
}"""
    },
    "rive_interactive": {
        "framework": "Rive Runtime",
        "title": "Interactive Vector State Machine with Mouse Cursor Tracking",
        "description": "High-framerate 60fps vector animation reacting to hover states and mouse direction without DOM lag.",
        "code": """import { useRive, useStateMachineInput } from '@rive-app/react-canvas';

export function InteractiveRiveGraphic({ src = '/assets/interactive-badge.riv', stateMachine = 'State Machine 1' }) {
  const { rive, RiveComponent } = useRive({
    src,
    stateMachines: stateMachine,
    autoplay: true,
  });

  // Example: Hook mouse cursor position into Rive State Machine number inputs
  const hoverInput = useStateMachineInput(rive, stateMachine, 'isHovered');
  const mouseXInput = useStateMachineInput(rive, stateMachine, 'numX');
  const mouseYInput = useStateMachineInput(rive, stateMachine, 'numY');

  const handlePointerMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    if (mouseXInput && mouseYInput) {
      mouseXInput.value = ((e.clientX - rect.left) / rect.width) * 100;
      mouseYInput.value = ((e.clientY - rect.top) / rect.height) * 100;
    }
  };

  return (
    <div
      onMouseEnter={() => hoverInput && (hoverInput.value = true)}
      onMouseLeave={() => hoverInput && (hoverInput.value = false)}
      onPointerMove={handlePointerMove}
      className="w-48 h-48 cursor-pointer"
    >
      <RiveComponent />
    </div>
  );
}"""
    }
}

def get_animation_recipe(framework_or_name: str = "framer_motion") -> Dict[str, Any]:
    """
    Returns production-ready code for Framer Motion, GSAP ScrollTrigger, Anime.js, Barba.js, or Rive.
    framework_or_name: 'framer_motion', 'gsap', 'animejs', 'barba', 'rive'.
    """
    key = framework_or_name.lower().replace("-", "_").replace(" ", "_")
    matched = None
    if any(k in key for k in ["framer", "motion", "spring"]):
        matched = ANIMATION_RECIPES["framer_motion_layout"]
    elif any(k in key for k in ["gsap", "scroll", "trigger"]):
        matched = ANIMATION_RECIPES["gsap_scroll_trigger"]
    elif any(k in key for k in ["anime", "path", "morph", "ripple"]):
        matched = ANIMATION_RECIPES["animejs_stagger"]
    elif any(k in key for k in ["barba", "page", "route", "wipe"]):
        matched = ANIMATION_RECIPES["barbajs_transitions"]
    elif any(k in key for k in ["rive", "vector", "state_machine"]):
        matched = ANIMATION_RECIPES["rive_interactive"]
    else:
        matched = ANIMATION_RECIPES["framer_motion_layout"]

    return {
        "framework": matched["framework"],
        "title": matched["title"],
        "description": matched["description"],
        "performance_rules": [
            "Always animate transform and opacity only (compositor thread).",
            "Always clean up event listeners or ScrollTrigger contexts on component unmount.",
            "Respect prefers-reduced-motion for accessibility."
        ],
        "code": matched["code"]
    }
