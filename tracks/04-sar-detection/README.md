# Track 4: Thermal / SAR Detection (Stretch)

## Goal
Detect survivors in rubble using ML on thermal or acoustic data.

## Approaches

### Thermal Person Detection
- Drone-mounted thermal camera → detect human heat signatures in rubble
- ML: YOLO/DETR fine-tuned on thermal imagery (domain shift from RGB)
- Challenge: thermal signatures ambiguous (warm pipes, sun-heated surfaces)

### Acoustic/Seismic Rubble Detection
- Place sensors on rubble, detect tapping/breathing signals
- ML: 1D CNN or spectrogram classifier on seismic/acoustic data
- Challenge: extremely low SNR, not enough training data

### Cell Phone Detection
- WiFi/Bluetooth sniffing for phones under debris
- More RF engineering than ML, but signal classification could help

## Reality Check
- SAR teams already have dogs, listening devices, cameras
- ML contribution is incremental and requires physical access to rubble
- Best case: partner with an SAR team and add ML to their existing sensor suite

## Open Questions
- [ ] Identify any SAR teams accepting technical volunteers
- [ ] Find open datasets for thermal person detection in rubble
- [ ] Assess feasibility of acoustic approach vs. existing commercial tools
