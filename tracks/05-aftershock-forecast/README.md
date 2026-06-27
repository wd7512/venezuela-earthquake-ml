# Track 5: Aftershock Forecasting (Research)

## Goal
ML-enhanced aftershock sequence prediction for operational forecasting.

## Background
- Statistical models (ETAS) already used operationally by USGS
- ML can improve: spatiotemporal clustering, magnitude distribution, timing
- Recent claims of 90%+ accuracy 48h ahead — treat with skepticism

## Approach
- Train on historical seismicity catalogs (northern Venezuela, subduction zones)
- Features: time since mainshock, distance from epicenter, b-value, stress transfer
- Model: point process neural nets, or transformer on event sequences
- Output: probability map of aftershock occurrence over next 24-72h

## Data
- USGS earthquake catalog (free)
- Historical Venezuela seismicity (historical records back to 1900)
- GNSS/InSAR data for stress transfer modeling (advanced)

## Open Questions
- [ ] Is there enough local catalog data for ML, or is statistical ETAS already near-optimal?
- [ ] Coordinate with seismologists (USGS, FUNVISIS in Venezuela)
- [ ] Define what "useful" means — probability gain over baseline?
