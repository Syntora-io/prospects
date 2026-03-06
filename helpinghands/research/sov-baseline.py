"""
Share of Voice Baseline -- Helping Hands Cleaning Services
Runs cleaning-industry queries across available AI engines and checks
whether Helping Hands is mentioned or cited.

Usage:
    py sov-baseline.py
    py sov-baseline.py --engines gemini,chatgpt
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime

# Force unbuffered output so background runs show progress
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# Add Syntora scripts to path so we can import the engine modules
SCRIPTS_DIR = os.path.join(
    os.environ.get("USERPROFILE", ""),
    "Desktop", "Syntora", "Internal", "Syntora.io", "scripts",
)
sys.path.insert(0, SCRIPTS_DIR)

# Load env from Syntora.io/.env.local
ENV_FILE = os.path.join(SCRIPTS_DIR, "..", ".env.local")
if os.path.exists(ENV_FILE):
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())


# =========================================================================
# TARGET COMPANY
# =========================================================================

COMPANY_NAME = "Helping Hands"
COMPANY_DOMAIN = "helpinghandscleaningservices.com"
COMPANY_ALIASES = [
    "helping hands cleaning",
    "helping hands maid",
    "helping hands cleaning services",
    "helpinghandscleaningservices",
]

# Competitors in the Chicago suburban cleaning market
COMPETITORS = [
    "Merry Maids",
    "Molly Maid",
    "The Maids",
    "MaidPro",
    "Two Maids",
    "Castle Keepers",
    "Maid Brigade",
    "Home Clean Heroes",
    "Tidy Casa",
    "Sparkle Freshness",
    "Scrub Squad",
    "COIT",
    "Stanley Steemer",
    "ServiceMaster",
    "Jan-Pro",
]


# =========================================================================
# QUERIES -- Residential cleaning, Chicago western suburbs
# =========================================================================

QUERIES = [
    # --- Brand queries ---
    {"query": "Helping Hands Cleaning Services Elmhurst IL", "category": "brand"},
    {"query": "Helping Hands Cleaning Services reviews", "category": "brand"},
    {"query": "Is Helping Hands Cleaning Services good?", "category": "brand"},

    # --- Local service queries (top cities) ---
    {"query": "best house cleaning service in Elmhurst IL", "category": "local"},
    {"query": "best cleaning service in Naperville IL", "category": "local"},
    {"query": "best house cleaning service in Glen Ellyn IL", "category": "local"},
    {"query": "best maid service in Wheaton IL", "category": "local"},
    {"query": "best cleaning company in Lombard IL", "category": "local"},
    {"query": "residential cleaning service Hinsdale IL", "category": "local"},
    {"query": "house cleaning near Downers Grove IL", "category": "local"},
    {"query": "top rated cleaning service Oak Park IL", "category": "local"},
    {"query": "best cleaning service western suburbs Chicago", "category": "local"},
    {"query": "house cleaning service DuPage County IL", "category": "local"},

    # --- Service-specific queries ---
    {"query": "deep cleaning service Elmhurst Illinois", "category": "service"},
    {"query": "move out cleaning service Naperville IL", "category": "service"},
    {"query": "recurring house cleaning Wheaton IL", "category": "service"},
    {"query": "eco-friendly house cleaning service Chicago suburbs", "category": "service"},
    {"query": "post construction cleaning DuPage County", "category": "service"},
    {"query": "carpet cleaning service Elmhurst IL", "category": "service"},

    # --- Decision / comparison queries ---
    {"query": "house cleaning vs maid service what is the difference", "category": "decision"},
    {"query": "how to choose a house cleaning company in Illinois", "category": "decision"},
    {"query": "what to look for in a residential cleaning service", "category": "decision"},
    {"query": "is it worth hiring a professional cleaning service", "category": "decision"},

    # --- Pricing queries ---
    {"query": "how much does house cleaning cost in Elmhurst IL", "category": "pricing"},
    {"query": "average cost of deep cleaning a house in Chicago suburbs", "category": "pricing"},
    {"query": "house cleaning prices per square foot Illinois", "category": "pricing"},
    {"query": "how much does a maid service cost in DuPage County", "category": "pricing"},

    # --- Trust / reputation queries ---
    {"query": "most trusted cleaning company in Elmhurst Illinois", "category": "trust"},
    {"query": "cleaning service with best reviews Chicago western suburbs", "category": "trust"},
    {"query": "eco friendly cleaning company near Elmhurst IL", "category": "trust"},
    {"query": "cleaning company that uses green products Chicago area", "category": "trust"},

    # --- Question queries (AI-style) ---
    {"query": "what is the best cleaning service near me in Elmhurst", "category": "question"},
    {"query": "can you recommend a cleaning service in Naperville Illinois", "category": "question"},
    {"query": "I need a house cleaner in the Chicago western suburbs who do you recommend", "category": "question"},
    {"query": "find me a reliable maid service in DuPage County Illinois", "category": "question"},
]


# =========================================================================
# ENGINE LOADING (reuse Syntora engine modules)
# =========================================================================

ENGINE_MAP = {
    "gemini": "engines.gemini_engine:GeminiEngine",
    "perplexity": "engines.perplexity_engine:PerplexityEngine",
    "brave": "engines.brave_engine:BraveEngine",
    "claude": "engines.claude_engine:ClaudeEngine",
    "chatgpt": "engines.chatgpt_engine:ChatGPTEngine",
    "grok": "engines.grok_engine:GrokEngine",
    "deepseek": "engines.deepseek_engine:DeepSeekEngine",
    "kimi": "engines.kimi_engine:KimiEngine",
    "llama": "engines.llama_engine:LlamaEngine",
}


def load_engine(name):
    """Load an engine by name. Returns instance or None if API key missing."""
    if name not in ENGINE_MAP:
        print(f"  [skip] Unknown engine: {name}")
        return None
    module_path, class_name = ENGINE_MAP[name].rsplit(":", 1)
    try:
        mod = __import__(module_path, fromlist=[class_name])
        cls = getattr(mod, class_name)
        return cls()
    except (ValueError, ImportError, Exception) as e:
        print(f"  [skip] {name}: {e}")
        return None


# =========================================================================
# RESPONSE PARSING
# =========================================================================

def parse_response(text, urls_cited=None):
    """Parse an AI response for Helping Hands mentions, URLs, competitors."""
    text_lower = text.lower()
    urls_cited = urls_cited or []

    # Mention detection
    mentioned = any(alias in text_lower for alias in COMPANY_ALIASES)
    if not mentioned:
        mentioned = "helping hands" in text_lower

    # URL detection
    domain_pattern = re.compile(
        r'(?:https?://)?(?:www\.)?(' + re.escape(COMPANY_DOMAIN) + r'(?:/[^\s)\]"\'>,;]*)?)',
        re.IGNORECASE,
    )
    found_urls = domain_pattern.findall(text)
    hh_urls = [u.rstrip(".,;:") for u in found_urls]
    hh_urls += [u for u in urls_cited if COMPANY_DOMAIN in u.lower()]
    hh_urls = list(dict.fromkeys(hh_urls))  # dedup preserving order

    # Competitor detection
    competitors_found = []
    for comp in COMPETITORS:
        if comp.lower() in text_lower:
            competitors_found.append(comp)

    # Citation context
    context = ""
    if mentioned:
        for sentence in re.split(r'[.!?\n]', text):
            if "helping hands" in sentence.lower():
                context = sentence.strip()[:500]
                break

    # Response quality
    if not mentioned:
        quality = "absent"
    elif hh_urls:
        quality = "featured"
    else:
        quality = "mentioned"

    return {
        "mentioned": mentioned,
        "urls": hh_urls,
        "competitors": competitors_found,
        "context": context,
        "quality": quality,
    }


# =========================================================================
# MAIN
# =========================================================================

def main():
    parser = argparse.ArgumentParser(description="Helping Hands SoV Baseline")
    parser.add_argument("--engines", default="all", help="Comma-separated engine names or 'all'")
    args = parser.parse_args()

    # Determine which engines to load
    if args.engines == "all":
        engine_names = list(ENGINE_MAP.keys())
    else:
        engine_names = [e.strip() for e in args.engines.split(",")]

    print("=" * 60)
    print("HELPING HANDS CLEANING -- SHARE OF VOICE BASELINE")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M CT')}")
    print(f"Queries: {len(QUERIES)}")
    print(f"Target: {COMPANY_NAME} ({COMPANY_DOMAIN})")
    print("=" * 60)
    print()

    # Load engines
    print("Loading engines...")
    engines = []
    for name in engine_names:
        engine = load_engine(name)
        if engine:
            engines.append(engine)
            print(f"  [ok] {name}")
    print(f"\n{len(engines)} engine(s) loaded.\n")

    if not engines:
        print("No engines available. Check API keys.")
        return

    # Run queries
    results = []
    totals = {e.name: {"mentioned": 0, "featured": 0, "absent": 0, "errors": 0} for e in engines}

    for qi, q in enumerate(QUERIES, 1):
        query_text = q["query"]
        category = q["category"]
        print(f"[{qi}/{len(QUERIES)}] {query_text}")

        for engine in engines:
            time.sleep(1)  # rate limit
            result = engine.query(query_text)

            if result.error:
                print(f"  {engine.name}: ERROR - {result.error[:80]}")
                totals[engine.name]["errors"] += 1
                results.append({
                    "query": query_text,
                    "category": category,
                    "engine": engine.name,
                    "error": result.error,
                    "mentioned": False,
                    "quality": "error",
                    "urls": [],
                    "competitors": [],
                    "context": "",
                    "response": "",
                })
                continue

            parsed = parse_response(result.response_text, result.urls_cited)

            status = "MENTIONED" if parsed["mentioned"] else "absent"
            if parsed["quality"] == "featured":
                status = "FEATURED"
            comp_str = f" | competitors: {', '.join(parsed['competitors'])}" if parsed["competitors"] else ""
            print(f"  {engine.name}: {status}{comp_str}")

            totals[engine.name]["mentioned" if parsed["mentioned"] else "absent"] += 1
            if parsed["quality"] == "featured":
                totals[engine.name]["featured"] += 1

            results.append({
                "query": query_text,
                "category": category,
                "engine": engine.name,
                "error": "",
                "mentioned": parsed["mentioned"],
                "quality": parsed["quality"],
                "urls": parsed["urls"],
                "competitors": parsed["competitors"],
                "context": parsed["context"],
                "response": result.response_text[:2000],
            })

    # =====================================================================
    # SUMMARY
    # =====================================================================
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)

    total_queries = len(QUERIES)
    for engine in engines:
        t = totals[engine.name]
        m = t["mentioned"]
        pct = (m / total_queries * 100) if total_queries else 0
        print(f"\n  {engine.name}:")
        print(f"    Mentioned: {m}/{total_queries} ({pct:.1f}%)")
        print(f"    Featured (URL cited): {t['featured']}")
        print(f"    Absent: {t['absent']}")
        if t["errors"]:
            print(f"    Errors: {t['errors']}")

    # Category breakdown
    print("\n" + "-" * 60)
    print("BY CATEGORY")
    print("-" * 60)
    categories = sorted(set(q["category"] for q in QUERIES))
    for cat in categories:
        cat_results = [r for r in results if r["category"] == cat and not r["error"]]
        cat_mentioned = sum(1 for r in cat_results if r["mentioned"])
        cat_total = len(cat_results)
        pct = (cat_mentioned / cat_total * 100) if cat_total else 0
        print(f"  {cat}: {cat_mentioned}/{cat_total} ({pct:.1f}%)")

    # Competitor leaderboard
    print("\n" + "-" * 60)
    print("COMPETITOR MENTIONS")
    print("-" * 60)
    comp_counts = {}
    for r in results:
        for c in r.get("competitors", []):
            comp_counts[c] = comp_counts.get(c, 0) + 1
    for comp, count in sorted(comp_counts.items(), key=lambda x: -x[1]):
        print(f"  {comp}: {count}")

    # Where HH WAS mentioned
    print("\n" + "-" * 60)
    print("QUERIES WHERE HELPING HANDS WAS MENTIONED")
    print("-" * 60)
    mentioned_results = [r for r in results if r["mentioned"]]
    if mentioned_results:
        for r in mentioned_results:
            url_str = f" | URL: {r['urls'][0]}" if r["urls"] else ""
            print(f"  [{r['engine']}] {r['query']}{url_str}")
            if r["context"]:
                print(f"    -> {r['context'][:200]}")
    else:
        print("  None. Helping Hands was not mentioned in any AI response.")

    # Save full results to JSON
    out_dir = os.path.dirname(os.path.abspath(__file__))
    today = datetime.now().strftime("%Y-%m-%d")
    json_path = os.path.join(out_dir, f"sov-baseline-{today}.json")
    with open(json_path, "w") as f:
        json.dump({
            "company": COMPANY_NAME,
            "domain": COMPANY_DOMAIN,
            "date": today,
            "engines": [e.name for e in engines],
            "total_queries": total_queries,
            "results": results,
            "summary": {
                "per_engine": totals,
                "competitor_counts": comp_counts,
            },
        }, f, indent=2)
    print(f"\nFull results saved to: {json_path}")


if __name__ == "__main__":
    main()
