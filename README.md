# Venezuela Earthquake ML Response

**Event:** 2026-06-24 — Mw 7.2 + Mw 7.5 doublet, San Felipe / Yaracuy / Caribbean coast
**Status:** Active response, aftershocks ongoing

ML tooling for damage assessment, mapping, and logistics support.

---

## Tracks

### 1. Satellite Damage Assessment (priority)
- Before/after imagery → building damage classification
- Target classes: no-damage / minor / major / destroyed
- Data sources: Sentinel-2 (free, 10m), Planet (paid, 3m), Maxar (restricted)
- Baseline: xView2 dataset + model
- Output: GeoJSON damage polygons for responders

### 2. Humanitarian Mapping (HOT-OSM)
- Automated building/road footprint extraction
- Push to OpenStreetMap for responder use
- Model suggests → human validates pipeline

### 3. Road Network / Logistics
- Road passability classification from imagery
- Route optimisation for aid delivery on damaged network
- Demand estimation from damage density + population

### 4. Thermal / SAR Detection (stretch)
- Person detection in thermal drone imagery
- Acoustic/seismic signal classification for rubble

### 5. Aftershock Forecasting (research)
- ML-enhanced ETAS models for aftershock sequence prediction
- Longer-term research contribution, not operational

---

## Key Links
- xView2: https://xview2.org/
- HOT-OSM: https://www.hotosm.org/
- USGS event page: https://earthquake.usgs.gov/earthquakes/map/
- NYT damage analysis: https://www.nytimes.com/interactive/2026/06/26/world/americas/venezuela-earthquake-damage-coast.html
- DisasterEye (GitHub): https://github.com/Niiihariiikaa/disastereye
- Drone damage detection: https://github.com/beau-rh3a/drone-disaster-damage-detection
- Operational sUAS damage assessment: https://arxiv.org/abs/2511.03132

## Getting Started
1. Set up Python env (requirements.txt TBD)
2. Pull test imagery over affected area
3. Run xView2 baseline on sample tiles
4. Iterate on model for Venezuela building types
