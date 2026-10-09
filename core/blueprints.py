"""Component Blueprints for UI/UX Pro MCP.
Provides battle-tested, pixel-perfect, beautifully spaced UI recipes.
Optimized for high aesthetics, responsive layouts, and minimal token usage.
"""

from typing import Dict, Any

BLUEPRINTS: Dict[str, Dict[str, Any]] = {
    "navbar": {
        "title": "Modern Sticky Glass Navbar",
        "key_spacings": "h-16 px-4 sm:px-6 lg:px-8, gap-6 nav items, min-h-[44px] cta",
        "description": "Sticky top bar with backdrop blur, 1px subtle border, accessible tap targets.",
        "tailwind_code": """<header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md">
  <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
    <div className="flex items-center gap-8">
      <a href="/" className="flex items-center gap-2.5 font-semibold tracking-tight text-text-main text-lg">
        <div className="h-8 w-8 rounded-lg bg-primary flex items-center justify-center text-white font-bold">A</div>
        <span>Brand</span>
      </a>
      <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-text-muted">
        <a href="#features" className="hover:text-text-main transition-colors py-2">Features</a>
        <a href="#pricing" className="hover:text-text-main transition-colors py-2">Pricing</a>
        <a href="#docs" className="hover:text-text-main transition-colors py-2">Documentation</a>
      </nav>
    </div>
    <div className="flex items-center gap-3">
      <a href="/login" className="hidden sm:inline-flex text-sm font-medium text-text-muted hover:text-text-main px-3 py-2">Sign in</a>
      <a href="/signup" className="inline-flex min-h-[40px] items-center justify-center rounded-lg bg-primary px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-primary/90 transition-all active:scale-[0.98]">
        Get Started
      </a>
    </div>
  </div>
</header>"""
    },
    "hero": {
        "title": "High-Conversion SaaS Hero Section",
        "key_spacings": "py-20 md:py-28 section, max-w-3xl headline, gap-4 cta row, gap-8 trust bar",
        "description": "Hero with announcement pill, tight heading rhythm, constrained paragraph, and dual CTAs.",
        "tailwind_code": """<section className="relative overflow-hidden py-20 md:py-28 lg:py-32">
  <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
    <!-- Announcement Pill -->
    <div className="inline-flex items-center gap-2 rounded-full border border-border bg-surface px-3.5 py-1.5 text-xs font-medium text-text-muted mb-8 shadow-xs hover:border-primary/50 transition-colors">
      <span className="flex h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span>
      <span>v2.0 is now live</span>
      <span className="text-text-main font-semibold">Explore changelog &rarr;</span>
    </div>
    
    <!-- Headline & Copy -->
    <h1 className="mx-auto max-w-4xl text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-text-main leading-[1.12]">
      Build beautiful products <br className="hidden sm:inline" />
      <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">without wasting tokens</span>
    </h1>
    <p className="mx-auto mt-6 max-w-2xl text-lg sm:text-xl text-text-muted leading-relaxed">
      Engineered for developer speed, pixel-perfect spacing, and instant WCAG AA compliance across every viewport.
    </p>

    <!-- CTA Group -->
    <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
      <button className="min-h-[48px] px-6 py-3 rounded-xl bg-primary text-white font-medium shadow-md hover:bg-primary/90 transition-all active:scale-[0.98]">
        Start Free Trial
      </button>
      <button className="min-h-[48px] px-6 py-3 rounded-xl border border-border bg-surface text-text-main font-medium hover:bg-surface-hover transition-all">
        Book a Demo
      </button>
    </div>

    <!-- Proof / Trust row -->
    <div className="mt-16 pt-8 border-t border-border/40">
      <p className="text-xs uppercase tracking-wider font-semibold text-text-muted">Trusted by fast-moving engineering teams</p>
    </div>
  </div>
</section>"""
    },
    "feature_grid": {
        "title": "Bento Feature Grid (3-Column)",
        "key_spacings": "gap-6 lg:gap-8 grid, p-6 sm:p-8 card padding, gap-4 card inner rhythm",
        "description": "Balanced bento grid with elevated cards, subtle hover lift, and icon badges.",
        "tailwind_code": """<section className="py-16 md:py-24 bg-surface/50">
  <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div className="max-w-2xl mb-12 sm:mb-16">
      <h2 className="text-xs font-bold uppercase tracking-wider text-primary">Capabilities</h2>
      <p className="mt-2 text-3xl font-bold tracking-tight text-text-main sm:text-4xl">Everything you need, calibrated</p>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
      {/* Feature Card */}
      <div className="group rounded-2xl border border-border bg-surface p-6 sm:p-8 transition-all duration-200 hover:-translate-y-1 hover:border-primary/40 hover:shadow-lg">
        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10 text-primary mb-6">
          <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
        </div>
        <h3 className="text-xl font-semibold text-text-main mb-2">Automated Spacing</h3>
        <p className="text-sm text-text-muted leading-relaxed">
          Enforce strict 4px/8px mathematical spatial rhythm without manual calculations.
        </p>
      </div>
    </div>
  </div>
</section>"""
    },
    "pricing_card": {
        "title": "Spotlight Pricing Card",
        "key_spacings": "p-8 card padding, gap-6 vertical stack, gap-3 feature checklist",
        "description": "High-converting pricing card with highlight ring, badge, and full-width CTA.",
        "tailwind_code": """<div className="relative rounded-2xl border-2 border-primary bg-surface p-8 shadow-xl flex flex-col justify-between">
  <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-primary px-3.5 py-1 text-xs font-semibold text-white uppercase tracking-wide">
    Most Popular
  </div>
  <div>
    <h3 className="text-xl font-bold text-text-main">Pro Team</h3>
    <p className="mt-2 text-sm text-text-muted">For growing startups demanding flawless UI.</p>
    <div className="mt-6 flex items-baseline gap-1">
      <span className="text-4xl font-extrabold tracking-tight text-text-main">$49</span>
      <span className="text-sm font-medium text-text-muted">/month</span>
    </div>
    
    <ul className="mt-8 space-y-3.5 border-t border-border pt-6 text-sm text-text-main">
      <li className="flex items-center gap-3">
        <span className="text-emerald-500 font-bold">&#10003;</span>
        <span>Unlimited layout audits</span>
      </li>
      <li className="flex items-center gap-3">
        <span className="text-emerald-500 font-bold">&#10003;</span>
        <span>WCAG AA automated fixes</span>
      </li>
      <li className="flex items-center gap-3">
        <span className="text-emerald-500 font-bold">&#10003;</span>
        <span>Full token generation</span>
      </li>
    </ul>
  </div>
  
  <button className="mt-8 w-full min-h-[44px] rounded-xl bg-primary py-3 px-4 text-sm font-semibold text-white shadow-sm hover:bg-primary/90 transition-all active:scale-[0.98]">
    Get Started with Pro
  </button>
</div>"""
    },
    "dashboard_card": {
        "title": "Clean Metric / KPI Card",
        "key_spacings": "p-5 sm:p-6 card, gap-3 header row, gap-1 stat to label",
        "description": "Essential dashboard stat card with trend indicator and sparkline container.",
        "tailwind_code": """<div className="rounded-xl border border-border bg-surface p-5 sm:p-6 shadow-xs">
  <div className="flex items-center justify-between">
    <span className="text-xs font-medium uppercase tracking-wider text-text-muted">Total Revenue</span>
    <span className="inline-flex items-center gap-1 rounded-full bg-emerald-500/10 px-2 py-0.5 text-xs font-semibold text-emerald-500">
      &uarr; 12.5%
    </span>
  </div>
  <div className="mt-4 flex items-baseline gap-2">
    <span className="text-3xl font-bold tracking-tight text-text-main">$128,430</span>
    <span className="text-xs text-text-muted">vs last month</span>
  </div>
</div>"""
    },
    "modal_dialog": {
        "title": "Accessible Modal Dialog",
        "key_spacings": "p-6 header/body/footer, max-w-lg container, gap-4 action buttons",
        "description": "Modal with backdrop-blur, smooth border, scrollable body, and sticky actions.",
        "tailwind_code": """<div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-background/60 backdrop-blur-sm animate-fade-in">
  <div className="w-full max-w-lg rounded-2xl border border-border bg-surface p-6 shadow-2xl animate-scale-up">
    <div className="flex items-center justify-between border-b border-border pb-4">
      <h3 className="text-lg font-semibold text-text-main">Edit Component</h3>
      <button className="h-8 w-8 rounded-lg flex items-center justify-center text-text-muted hover:text-text-main hover:bg-surface-hover">
        &times;
      </button>
    </div>
    <div className="py-6 space-y-4 text-sm text-text-muted">
      <p>Configure layout properties and spatial tokens.</p>
    </div>
    <div className="flex items-center justify-end gap-3 border-t border-border pt-4">
      <button className="min-h-[40px] px-4 py-2 rounded-lg border border-border text-sm font-medium hover:bg-surface-hover">
        Cancel
      </button>
      <button className="min-h-[40px] px-4 py-2 rounded-lg bg-primary text-white text-sm font-medium hover:bg-primary/90">
        Save Changes
      </button>
    </div>
  </div>
</div>"""
    }
}

def get_component_blueprint(component_type: str = "hero") -> Dict[str, Any]:
    """
    Returns a production-ready, beautifully spaced component blueprint.
    """
    key = component_type.lower().replace("-", "_").replace(" ", "_")
    if key not in BLUEPRINTS:
        # Fallback to closest match
        match = next((k for k in BLUEPRINTS if k in key or key in k), "hero")
        blueprint = BLUEPRINTS[match]
    else:
        blueprint = BLUEPRINTS[key]
        
    return {
        "component": component_type,
        "blueprint_title": blueprint["title"],
        "description": blueprint["description"],
        "key_spacings": blueprint["key_spacings"],
        "code": blueprint["tailwind_code"]
    }
