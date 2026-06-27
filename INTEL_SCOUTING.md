# Information Scouting — Forum & Social Media Intelligence

Compiled 2026-06-27 from swarm search. This is the "where to look and what's been found" document.

---

## Reddit

### r/AskLatinAmerica — Megathread
- URL: https://www.reddit.com/r/asklatinamerica/comments/1ufa4wj/megathread_venezuelan_earthquake_updates_info_and/
- Active 2 days ago. Key info: structures weakened but still standing may collapse; disrupted services and damaged roads complicating evacuation/relief.

### r/news — Thousands feared dead
- URL: https://www.reddit.com/r/news/comments/1ufdj41/thousands_feared_dead_in_venezuela_after_two/
- Note: government only lists confirmed deaths to avoid panic — actual toll likely higher than reported.

### r/Damnthatsinteresting — La Guaira video
- URL: https://www.reddit.com/r/Damnthatsinteresting/comments/1uevvg8/devastation_in_la_guaira_after_being_struck_by/
- Video of devastation in La Guaira.

### r/Earthquakes — Los Palos Grandes damage
- URL: https://www.reddit.com/r/Earthquakes/rising/
- Photo of damaged building at Los Palos Grandes (Caracas district).

---

## X/Twitter (OSINT accounts to follow)

- **@sentdefender** (OSINTdefender) — posted immediate damage reports, satellite imagery references, and real-time updates on June 24.
- **@amilcarrock** — Venezuelan user posting ground-level videos (cracked staircases, building evacuations).
- **@TheGlobeNewt** — compiled video of stadium earthquake (baseball game at Estadio Universitario de Caracas).
- **Héctor A.** — posted stadium shaking video during baseball game.

### Key X threads to mine for ground-truth damage:
- Search: "terremoto Venezuela edificio colapsado" + location
- Search: "La Guaira terremoto daño" 
- Search: "Caracas sismo edificio" + colonia/barrio name

---

## OpenStreetMap Community Forum

### "Mapping to support the Venezuela earthquake response"
- URL: https://community.openstreetmap.org/t/mapping-to-support-the-venezuela-earthquake-response/144882
- Posted 1 day ago. Key quote: "I'd like to highlight how important it is for the authorities and people working on the ground to have accurate maps of the buildings in the affected areas."
- **This is our direct entry point.** Someone is already calling for mapping but no organised activation yet.

---

## HOT-OSM (Humanitarian OpenStreetMap Team)

- Instagram (@_hotosm): "Following the widespread damage brought on by two large earthquakes in Venezuela, partners on the ground are looking for an updated base map."
- Website disaster services: https://www.hotosm.org/disaster-services/project_activations.html
- **No formal activation listed yet** (as of search), but the call is out.
- HOT OSM toolbox for post-earthquake assessment: https://toolbox.hotosm.org/pages/8_use_case/8_2_post_earthquake/

---

## Structural Engineering Intelligence — Miyamoto International

Miyamoto (led by Kit Miyamoto) is on the ground doing rapid structural assessments. Their website published:

1. **"Venezuela's Strongest Earthquake in 125 Years"** — overview + rapid exposure assessment
   - URL: https://miyamotointernational.com/venezuelas-strongest-earthquake-in-125-years-what-happened-on-june-24-2026/

2. **Rapid Exposure Assessment** — specific damage data
   - URL: https://miyamotointernational.com/venezuela-earthquake-rapid-exposure-assessment/

3. **"Why Venezuela Earthquake Damage Was Severe"** — structural analysis
   - URL: https://miyamotointernational.com/why-venezuela-earthquake-damage-was-severe/

Key findings from their assessment:
- Many collapsed buildings were "brittle concrete without adequate steel reinforcement"
- After life-safety rescue, next phase is rapid structural assessment (safe / restricted-use / unsafe)
- Goal: reduce secondary casualties, support shelter decisions

**This is gold for training data.** Their damage classifications map directly to our ML classes.

---

## ReliefWeb (UN OCHA)

- Event page: https://reliefweb.int/disaster/eq-2026-000093-ven
- Official UN tracking. Will have situation reports, needs assessments, cluster updates.

---

## PAHO/WHO (Health-specific)

- URL: https://www.paho.org/en/venezuela-earthquake-response
- Rapid assessments of health facility functionality/safety
- Mapping partner presence and operational capacity
- Identifying requirements: medicines, medical supplies, oxygen, fuel

---

## Key Damage Hotspots (from compiled reports)

| Location | Damage Level | Notes |
|----------|-------------|-------|
| La Guaira | Severe | Worst-affected; dozens of buildings collapsed; port area |
| Caracas (capital) | Major | Los Palos Grandes, Catia La Mar; stadium damage; hospital evacuated |
| Morón | Epicentre zone | Near epicentre; rural/semi-urban |
| San Felipe, Yaracuy | Epicentre zone | Both quakes centred here |
| Valencia | Moderate | 59km from M7.5 epicentre |

---

## What We Can Mine From These Sources

1. **Reddit/Twitter** → geolocated damage reports, photos, videos → training data + ground truth
2. **Miyamoto** → structured damage assessments → validation labels for our model
3. **OSM Forum** → coordination channel — we can post offering ML-based damage mapping
4. **HOT-OSM** → formal activation would create tasking for imagery analysis
5. **ReliefWeb** → situation reports → structured needs/damage data
6. **X OSINT** → before/after imagery, building-level damage documentation

## Action Items

- [ ] Monitor OSM forum thread for activation status
- [ ] Scrape/collect geolocated social media posts for training imagery
- [ ] Contact Miyamoto about sharing damage assessment data
- [ ] Check if HOT-OSM has imagery partnerships (Planet, Maxar) we can piggyback on
- [ ] Set up X search alerts for "Venezuela terremoto daño colapsado" with geolocation
