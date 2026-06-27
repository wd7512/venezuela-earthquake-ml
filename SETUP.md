# Environment Setup

## Python version
3.10+ recommended (torch, rasterio, geopandas compatibility)

## Create env
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Core dependencies (TBD)
- torch / torchvision
- rasterio (geospatial raster I/O)
- geopandas (vector data)
- shapely (geometry)
- overpy or osmnx (OpenStreetMap data)
- sentinelhub or earthengine-api (imagery access)
- xarray (multi-dimensional arrays)
- folium / leafmap (visualization)

## GPU
MacBook Air — no local GPU. Options:
- Free tier Colab (T4, intermittent)
- Kaggle Notebooks (T4, session limits)
- Lambda Labs / RunPod for heavier training

## Data access
- Sentinel-2: free via Copernicus Open Access Hub or Google Earth Engine
- Planet: research license (education/academic) or Open Data program
- Maxar: restricted, humanitarian access via UNOSAT
- OSM: Overpass API (free)
