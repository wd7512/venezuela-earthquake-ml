# Track 2: Humanitarian Mapping (HOT-OSM)

## Goal
Automate building and road footprint extraction from satellite imagery to feed OpenStreetMap for responders.

## Approach
1. Pull fresh post-event imagery (Sentinel-2 free, or Planet if available)
2. Run segmentation model to extract building footprints and road network
3. Validate / post-process
4. Push to OSM via HOT-OSM tasking platform

## Models
- SpaceNet / building segmentation (U-Net, DeepLabV3+)
- Road extraction: RoadTracer, VecNet
- Consider: SAM (Segment Anything) for zero-shot building detection on new imagery

## Integration
- HOT-OSM tasking: https://tasking.hotosm.org/
- Look for existing Venezuela earthquake activation project
- Output format: OSM XML / GeoJSON → JOSM for validation

## Open Questions
- [ ] Check if HOT-OSM has activated for this event yet
- [ ] Determine if pre-event OSM data for the area is adequate (may need full re-mapping)
- [ ] GPU requirements for large-area inference
