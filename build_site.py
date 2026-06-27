#!/usr/bin/env python3
"""Build the Venezuela Earthquake Response static site.

Reads data.json, renders Jinja2 templates, and outputs everything to dist/.
Generates both English (root) and Spanish (es/) versions.
"""

import json
import os
from datetime import datetime, timezone

from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "data.json")
TEMPLATES_DIR = os.path.join(ROOT, "templates")
TEMPLATES_ES_DIR = os.path.join(ROOT, "templates_es")
DIST_DIR = os.path.join(ROOT, "dist")
os.makedirs(DIST_DIR, exist_ok=True)


def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)


def compute_staleness(last_updated_str):
    last = datetime.fromisoformat(last_updated_str.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    hours = (now - last).total_seconds() / 3600
    return int(hours)


def build_lang(templates_dir, output_dir, lang_suffix, data, template_vars_base, pages):
    """Build all pages for one language into output_dir/lang_suffix/."""
    env = Environment(loader=FileSystemLoader(templates_dir))
    out_base = os.path.join(output_dir, lang_suffix)
    os.makedirs(out_base, exist_ok=True)

    for page in pages:
        template = env.get_template(f"{page}.html")
        vars_copy = template_vars_base.copy()
        vars_copy["page"] = page.replace("zone_", "")
        html = template.render(**vars_copy)

        out_path = os.path.join(out_base, f"{page}.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"  Wrote {out_path}")


def build_site():
    data = load_data()
    staleness_hours = compute_staleness(data["last_updated"])

    # Format timestamp for humans
    last_dt = datetime.fromisoformat(data["last_updated"].replace("Z", "+00:00"))
    last_updated_formatted = last_dt.strftime("%d %B %Y, %I:%M %p Caracas time (UTC−4)")

    config = data.get("config", {})

    template_vars_base = {
        "page": "",
        "last_updated": data["last_updated"],
        "last_updated_formatted": last_updated_formatted,
        "staleness_hours": staleness_hours,
        "stats": data["stats"],
        "zones": data["zones"],
        "tracks": data["tracks"],
        "gaps": data["gaps"],
        "resources": data["resources"],
        "death_toll_note": data.get("death_toll_note", ""),
        "show_zone_pages": config.get("show_zone_pages", True),
    }

    pages = ["index", "intel", "handbook", "help", "contributing", "gaps", "sources", "statistics", "aid"]

    # Build English (root)
    print("Building English (root)...")
    build_lang(TEMPLATES_DIR, DIST_DIR, "", data, template_vars_base, pages)

    # Build Spanish (es/)
    print("Building Spanish (es/)...")
    build_lang(TEMPLATES_ES_DIR, DIST_DIR, "es", data, template_vars_base, pages)

    total = len(pages) * 2
    print(f"\nSite built in {DIST_DIR}/")
    print(f"  {total} pages ({len(pages)} English + {len(pages)} Spanish)")


if __name__ == "__main__":
    build_site()
