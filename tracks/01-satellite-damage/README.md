# Track 1: Satellite Damage Assessment

## Goal
Classify building damage from before/after satellite imagery into structured GeoJSON for responders.

## Classes (xView2-compatible)
- no-damage
- minor-damage
- major-damage
- destroyed

## Data Sources
| Source | Resolution | Access |
|--------|-----------|--------|
| Sentinel-2 | 10m | Free (Copernicus / Google Earth Engine) |
| Planet Labs | 3m | Research license or paid |
| Maxar | 0.3m | Restricted (may need humanitarian access) |
| NASA Black Marble | 500m | Night lights — power outage proxy |

## Pipeline
1. **Imagery acquisition** — pull pre-event + post-event pairs for affected tiles
2. **Co-registration** — align before/after
3. **Tiling** — 256x256 or 512x512 chips
4. **Inference** — damage classification model
5. **Post-processing** → GeoJSON polygons with damage class + confidence
6. **Delivery** — push to HOT-OSM / UN OCHA / responders

## Baseline Models
- xView2 baseline (ResNet/U-Net on pre-trained backbone)
- SpaceNet building footprint extraction (for pre-event building locations)
- Consider: Siamese network on before/after pairs for change detection

## Venezuela-Specific Considerations
- Building types: reinforced concrete high-rises (Caracas/La Guaira), informal housing (barrios), mixed masonry
- Urban density is high — pixel-level classification may struggle with 10m resolution
- Informal structures may not appear in pre-event imagery at all

## Open Questions
- [ ] Get Planet research license or find free high-res imagery
- [ ] Check if xView2 pre-trained weights transfer to Venezuela building stock
- [ ] Decide: classification per-building or per-pixel segmentation
- [ ] Coordinate with HOT-OSM on output format / integration
