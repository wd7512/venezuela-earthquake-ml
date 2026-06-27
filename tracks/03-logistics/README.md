# Track 3: Road Network & Logistics

## Goal
Classify road passability and optimise aid delivery routes on the damaged network.

## Pipeline
1. Extract road graph from OpenStreetMap (pre-event)
2. Classify each road segment from post-event imagery: intact / debris-blocked / bridge-collapsed / unknown
3. Build weighted graph (passable = weight, impassable = infinite)
4. Solve vehicle routing for aid distribution

## ML Component
- Road damage classification from satellite/drone imagery
- Similar to Track 1 but simpler (linear features vs. buildings)
- Could reuse building damage model with road-specific fine-tuning

## Data Needs
- OSM road network for affected area (quick to pull via Overpass API)
- Post-event imagery with road visibility
- Population data for demand estimation (WorldPop, Meta High-Res)

## Open Questions
- [ ] How granular does road classification need to be for routing to work?
- [ ] Coordinate with logistics cluster (WFP / UN OCHA) on format
- [ ] Consider real-time updates as new imagery comes in
