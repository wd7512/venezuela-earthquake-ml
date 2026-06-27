# Venezuela Earthquake Response Hub

**Event:** 2026-06-24 — Mw 7.2 + Mw 7.5 doublet, Yaracuy / Caribbean coast
**Status:** Active response, aftershocks ongoing
**Live site:** https://wd7512.github.io/venezuela-earthquake-ml/

Static information hub for the June 2026 Venezuela earthquake response. Built with Jinja2 templates + `data.json` single source of truth. Rebuilt every 6 hours via GitHub Actions.

---

## What's here

| Page | Purpose |
|------|---------|
| **Overview** | Zone status, key numbers, missing persons, safety |
| **Intel** | Seismic data, statistics, aid tracking, historical context |
| **Handbook** | What to do during/after, finding family, communication |
| **How to Help** | Donate, share, technical volunteer opportunities |
| **Get Aid** | Emergency contacts, missing persons search, donate, safety |
| **Sources** | Every data point traceable to primary source |
| **Statistics** | All figures sourced, methodology notes |
| **Contributing** | Contribution tracks, build instructions, data pipeline |
| **Gaps** | Prioritized response gaps where help is needed |

---

## Data

All site content is driven by `data.json`. To update:
1. Edit `data.json` with new figures, sources, or zone status
2. Run `uv run python build_site.py` (outputs to `dist/`)
3. Push to main — GitHub Actions deploys automatically

The `last_updated` field in `data.json` controls the "Updated" timestamp on all pages. Set it when you pull fresh data from sources.

---

## Tracks (ML / data science)

The repository also contains research tracks for ML-assisted damage assessment. These are longer-term research goals, not active for the current response window:

1. **Satellite Damage Assessment** — building damage classification from imagery
2. **Humanitarian Mapping (HOT-OSM)** — automated footprint extraction
3. **Road Network / Logistics** — passability + route optimisation
4. **Thermal/SAR Detection** — person detection in drone imagery (research)
5. **Aftershock Forecasting** — ML-enhanced ETAS models (research)

---

## Key Links

- USGS event page: https://earthquake.usgs.gov/earthquakes/eventpage/us6000t7zp/executive
- iMMAP impact map: https://immap.org/publications-and-resources/venezuela-earthquake-impact-map-24th-june-2026
- Copernicus EMS: https://emergency.copernicus.eu
- HOT-OSM Tasking Manager: https://tasks.hotosm.org/
- Desaparecidos Terremoto Venezuela: https://www.desaparecidososterremotovenezuela.com/
- Venezuela Te Busca: https://venezuelatebusca.com/

---

## Local development

```bash
uv sync
uv run python build_site.py        # build to dist/
# Or serve locally:
uv run python -m http.server --directory dist 8080
```

---

## License

Data compiled from public sources (UN OCHA, USGS, Miyamoto International, HOT-OSM, Copernicus EMS, ReliefWeb). Code: MIT.
