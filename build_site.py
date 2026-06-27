#!/usr/bin/env python3
"""Build the Venezuela Earthquake Response static site.

Reads data.json, renders 8 Jinja2 templates, and outputs everything to dist/.
"""

import json
import os
from datetime import datetime, timezone

from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "data.json")
TEMPLATES_DIR = os.path.join(ROOT, "templates")
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


def build_site():
    data = load_data()
    staleness_hours = compute_staleness(data["last_updated"])

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    pages = ["index", "intel", "handbook", "help", "contributing", "gaps", "sources", "statistics", "aid"]

    # Format timestamp for humans
    last_dt = datetime.fromisoformat(data["last_updated"].replace("Z", "+00:00"))
    last_updated_formatted = last_dt.strftime("%d %B %Y, %I:%M %p Caracas time (UTC−4)")

    config = data.get("config", {})

    template_vars = {
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

    for page in pages:
        template = env.get_template(f"{page}.html")
        vars_copy = template_vars.copy()
        vars_copy["page"] = page.replace("zone_", "")
        html = template.render(**vars_copy)

        out_path = os.path.join(DIST_DIR, f"{page}.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"  Wrote {out_path}")

    print(f"\nSite built in {DIST_DIR}/")
    print(f"  {len(pages)} pages")


if __name__ == "__main__":
    build_site()
