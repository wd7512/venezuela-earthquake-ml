#!/usr/bin/env python3
"""Build the Venezuela Earthquake Response static site.

Reads data.json, generates 4 matplotlib charts, renders 7 Jinja2 templates,
and outputs everything to dist/.
"""

import json
import os
import shutil
from datetime import datetime, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "data.json")
TEMPLATES_DIR = os.path.join(ROOT, "templates")
DIST_DIR = os.path.join(ROOT, "dist")
IMAGES_DIR = os.path.join(DIST_DIR, "images")


def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)


def compute_staleness(last_updated_str):
    last = datetime.fromisoformat(last_updated_str.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    hours = (now - last).total_seconds() / 3600
    return int(hours)


def chart_damage_by_zone(data, output_path):
    zones = [z for z in data["zones"] if z["damage_score"] > 0]
    names = [z["name"] for z in zones]
    scores = [z["damage_score"] for z in zones]

    colors = []
    for z in zones:
        if z["damage_level"] == "severe":
            colors.append("#e74c3c")
        elif z["damage_level"] == "major":
            colors.append("#e67e22")
        else:
            colors.append("#f1c40f")

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#1a1d27")
    ax.set_facecolor("#1a1d27")

    bars = ax.barh(names, scores, color=colors, edgecolor="none", height=0.65)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Damage Score", color="#8b8fa3", fontsize=11)
    ax.set_title("Damage by Zone", color="#e1e4ed", fontsize=14, fontweight="bold", pad=15)

    ax.tick_params(colors="#8b8fa3", labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#2e3148")
    ax.spines["bottom"].set_color("#2e3148")

    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                str(score), va="center", color="#8b8fa3", fontsize=9)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def chart_aftershock_timeline(data, output_path):
    aftershocks = data.get("aftershocks_data", [])
    if not aftershocks:
        return

    dates = [datetime.fromisoformat(a["date"].replace("Z", "+00:00")) for a in aftershocks]
    mags = [a["magnitude"] for a in aftershocks]

    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#1a1d27")
    ax.set_facecolor("#1a1d27")

    ax.scatter(dates, mags, c="#e74c3c", s=30, alpha=0.7, zorder=3)
    ax.plot(dates, mags, color="#e74c3c", linewidth=0.5, alpha=0.3, zorder=1)

    ax.set_ylabel("Magnitude", color="#8b8fa3", fontsize=11)
    ax.set_title("Aftershock Timeline", color="#e1e4ed", fontsize=14, fontweight="bold", pad=15)

    ax.tick_params(colors="#8b8fa3", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#2e3148")
    ax.spines["bottom"].set_color("#2e3148")

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d\n%H:%M"))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=12))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, ha="center")
    ax.set_ylim(2, 6)
    ax.set_yticks([2, 3, 4, 5])

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def chart_missing_persons(data, output_path):
    mp = data.get("missing_persons_data", [])
    if not mp:
        return

    dates = [m["date"] for m in mp]
    reported = [m["reported"] for m in mp]
    found = [m["found"] for m in mp]

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#1a1d27")
    ax.set_facecolor("#1a1d27")

    x = range(len(dates))
    ax.fill_between(x, reported, alpha=0.15, color="#e74c3c")
    ax.fill_between(x, found, alpha=0.15, color="#27ae60")
    ax.plot(x, reported, color="#e74c3c", linewidth=2, marker="o", label="Reported Missing")
    ax.plot(x, found, color="#27ae60", linewidth=2, marker="s", label="Found")

    ax.set_xticks(x)
    ax.set_xticklabels(dates, color="#8b8fa3", fontsize=9)
    ax.set_ylabel("People", color="#8b8fa3", fontsize=11)
    ax.set_title("Missing Persons: Reported vs Found", color="#e1e4ed", fontsize=14, fontweight="bold", pad=15)

    ax.tick_params(colors="#8b8fa3", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#2e3148")
    ax.spines["bottom"].set_color("#2e3148")
    ax.legend(facecolor="#242738", edgecolor="#2e3148", labelcolor="#e1e4ed", fontsize=10)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def chart_ml_gaps_summary(data, output_path):
    gaps = data.get("gaps", [])
    if not gaps:
        return

    gap_types = {}
    for gap in gaps:
        key = f"{gap['gap_type'].replace('_', ' ')} ({gap['severity']})"
        gap_types[key] = gap_types.get(key, 0) + 1

    labels = list(gap_types.keys())
    values = list(gap_types.values())

    severity_colors = {"high": "#e74c3c", "medium": "#e67e22", "low": "#f1c40f"}
    colors = []
    for label in labels:
        for sev, color in severity_colors.items():
            if sev in label:
                colors.append(color)
                break
        else:
            colors.append("#8b8fa3")

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#1a1d27")
    ax.set_facecolor("#1a1d27")

    bars = ax.barh(labels, values, color=colors, edgecolor="none", height=0.6)
    ax.set_xlabel("Count", color="#8b8fa3", fontsize=11)
    ax.set_title("Response Gaps by Type and Severity", color="#e1e4ed", fontsize=14, fontweight="bold", pad=15)

    ax.tick_params(colors="#8b8fa3", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#2e3148")
    ax.spines["bottom"].set_color("#2e3148")

    for bar, val in zip(bars, values):
        if val > 0:
            ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
                    str(val), va="center", color="#8b8fa3", fontsize=9)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def build_site():
    data = load_data()
    staleness_hours = compute_staleness(data["last_updated"])

    os.makedirs(IMAGES_DIR, exist_ok=True)

    chart_damage_by_zone(data, os.path.join(IMAGES_DIR, "damage_by_zone.png"))
    chart_aftershock_timeline(data, os.path.join(IMAGES_DIR, "aftershock_timeline.png"))
    chart_missing_persons(data, os.path.join(IMAGES_DIR, "missing_persons_trend.png"))
    chart_ml_gaps_summary(data, os.path.join(IMAGES_DIR, "ml_gaps_summary.png"))

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    pages = ["index", "intel", "handbook", "contributing", "gaps", "zone_la_guaira", "zone_caracas"]

    # Format timestamp for humans
    last_dt = datetime.fromisoformat(data["last_updated"].replace("Z", "+00:00"))
    last_updated_formatted = last_dt.strftime("%d %B %Y, %I:%M %p Caracas time (UTC−4)")

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

    chart_files = ["damage_by_zone.png", "aftershock_timeline.png",
                   "missing_persons_trend.png", "ml_gaps_summary.png"]
    for cf in chart_files:
        path = os.path.join(IMAGES_DIR, cf)
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  Chart: {cf} ({size / 1024:.1f} KB)")

    print(f"\nSite built in {DIST_DIR}/")
    print(f"  {len(pages)} pages, {len(chart_files)} charts")


if __name__ == "__main__":
    build_site()
