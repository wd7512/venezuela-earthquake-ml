# Information Scouting — Forum & Social Media Intelligence

Last updated: 2026-06-27 (evening scout run)
Compiled from swarm + cron search runs. This is the "where to look and what's been found" document.

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
| La Guaira | Severe | Worst-affected; 100+ buildings collapsed (UN OCHA); port area; Vantor before/after imagery available |
| Catia La Mar | Severe | Adjacent to airport; Microsoft AI4G damage dataset available; NYT featured destruction |
| Caracas (capital) | Major | Los Palos Grandes, Catia La Mar; stadium damage; hospital evacuated |
| Morón | Epicentre zone | Near epicentre (Carabobo State); rural/semi-urban |
| San Felipe, Yaracuy | Epicentre zone | Both quakes centred here (updated: epicentres near Yumare, 23km SE) |
| Maiquetia | Severe | Airport area; Vantor imagery shows building damage; main international airport closed |
| Valencia | Moderate | 59km from M7.5 epicentre |
| Tucacas, Falcón | Aftershock-hit | M5.1 aftershock on night of June 25 |
| Guatire, Miranda | Aftershock-hit | M4.4 aftershock early June 26 |

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
- [ ] Download & evaluate Microsoft AI4G Catia La Mar dataset as training/validation data
- [ ] Access Vantor Open Data Program imagery for broader coverage
- [ ] Mine OCHA SitRep #3 for structured damage/needs data

---

## 🔥 NEW HIGH-VALUE INTEL (2026-06-27 Evening Scout)

### 1. Microsoft AI for Good Lab — Building Damage Assessment Dataset (Catia La Mar)
- **URL:** https://data.humdata.org/dataset/venezuela-earthquakes-catia-la-mar
- **Published:** 2026-06-26 (updated 2026-06-27)
- **What:** Microsoft AI4G Lab ran damage assessment AI models on satellite imagery from 25 June 2026 for Catia La Mar
- **Files available:**
  - `predicted_damage_catia_la_mar_footprints.gpkg` — GeoPackage with building footprints + damage predictions
  - `venezuela-2026-page-2-updated.jpg` — overview image
  - Additional data resource (preview image)
- **Key metadata from the dataset description:**
  - "Damaged = 1 will take any building with at least a pixel showing damage"
  - Recommendation: filter with `damage_pct_0m >= 0.8` or `damage_pct_10m` because post-event scene had orthorectification issues
- **ML relevance:** ⭐⭐⭐⭐⭐ — This is a ready-made labeled dataset for Catia La Mar. We can use it as:
  - Training data (building-level damage labels)
  - Validation/benchmark for our own model
  - Comparison point to evaluate our model's accuracy vs. Microsoft's
- **Croissant ML metadata:** Available at `?profiles=croissant` — standardized ML dataset description

### 2. Vantor Open Data Program — Free Satellite Imagery
- **URL:** https://www.linkedin.com/posts/vantortech_vantor-has-activated-its-open-data-program-activity-7476261311316832256-5vXE
- **What:** Vantor activated its Open Data Program for Venezuela, releasing free high-resolution satellite imagery
- **Imagery details:**
  - Before/after pairs for La Guaira, Catia La Mar, Maiquetia
  - Pre-event: June 22, 2026 (and April 30 for Maiquetia)
  - Post-event: June 25, 2026 (morning after the quake)
  - Used by NYT, NBC, AP, USA Today for their before/after comparisons
- **ML relevance:** ⭐⭐⭐⭐⭐ — Free high-res before/after imagery is exactly what we need for training data. This is our primary imagery source.

### 3. OCHA Situation Report #3 (26 June 2026, 3:00 PM)
- **URL:** https://reliefweb.int/report/venezuela-bolivarian-republic/earthquakes-venezuela-situation-report-no-3-26-june-2026-time-300-pm
- **Key new info:**
  - 302+ aftershocks recorded
  - M5.1 aftershock in Tucacas (Falcón state) on night of June 25
  - M4.4 aftershock NE of Guatire (Miranda state) early June 26
  - Sustained high-risk conditions
- **Earlier sitreps now available:**
  - SitRep #1 (June 25, 3:00 AM): 32 fatalities, 700+ injured (preliminary)
  - SitRep #2 (June 25, 3:00 PM): OCHA coordination
  - SitRep #3 (June 26, 3:00 PM): 302 aftershocks, updated impact
  - IOM SitRep #1 (June 26): migration/displacement focus
  - UNICEF SitRep #1 (June 25): child-focused needs

### 4. Updated Death Toll & Impact Scale
- **Current official toll:** 920+ dead, 3,360+ injured (per multiple sources including BBC, New Indian Express)
- **Earlier reports:** 164→188→235→589→920 (escalating as rescue progresses)
- **USGS PAGER estimate:** 44% chance final death toll exceeds 10,000
- **UN OCHA:** 100+ buildings collapsed in La Guaira alone
- **iMMAP impact map:** ~590,000 people in MMI VII+ shaking zones; 4.8M exposed to MMI VI from M7.5 alone; 16M+ in total footprint
- **Economic loss estimate:** $4.7–8.7 billion (UNDP); some estimates $10–100 billion

### 5. Miyamoto International — New Update Post
- **URL:** https://miyamotointernational.com/venezuela-earthquake-update-june-2026/
- **Published:** June 26, 2026
- **Key info:**
  - As of June 26: ~235 dead, ~4,300 injured (Health Ministry)
  - National Assembly count: at least 188 dead
  - Officials expect toll to rise
  - Airport status: main international airport closed
  - Multiple governments advising against travel

### 6. iMMAP — Venezuela Earthquake Impact Map
- **URL:** https://immap.org/publications-and-resources/venezuela-earthquake-impact-map-24th-june-2026
- **Based on:** USGS ShakeMap + WorldPop 2026 data
- **Key stats:**
  - ~590,000 people in severe-to-violent shaking zones (MMI VII+) across both events
  - 4.8 million exposed to strong shaking (MMI VI) from M 7.5 alone
  - Over 16 million people within total earthquake footprint
- **ML relevance:** ⭐⭐⭐ — Population exposure data useful for prioritizing areas for ML damage mapping

### 7. Euronews — Before/After Satellite Image Gallery
- **URL:** https://www.euronews.com/2026/06/27/venezuela-satellite-images-reveal-scale-of-disaster
- **Published:** Today (June 27)
- **Content:** Curated set of before/after satellite images showing La Guaira destruction
- **Source:** Vantor imagery (see #2 above)

### 8. IFRC Emergency Page
- **URL:** https://go.ifrc.org/emergencies/7990/details
- **Emergency ID:** VEN: Earthquake - 06-2026
- **Status:** Active, with situational overview and Red Cross response details

---

## Search Effectiveness Log

| Query | Result | Notes |
|-------|--------|-------|
| "Venezuela earthquake" + damage + satellite | ⭐⭐⭐⭐⭐ | Rich results — Vantor imagery, Microsoft dataset, Euronews gallery |
| "Venezuela earthquake" + HOT-OSM + activation | ⭐⭐⭐ | HOT has posted about it but no formal activation page yet; Pete Masters LinkedIn confirms mapping campaign is being set up |
| "Venezuela earthquake" + Miyamoto | ⭐⭐⭐⭐ | New update post (June 26) with current toll + airport status |
| "Venezuela earthquake" + ReliefWeb + situation report | ⭐⭐⭐⭐⭐ | Multiple sitreps now available (#1, #2, #3, IOM, UNICEF) |
| "Venezuela earthquake" + github + machine learning | ⭐ | No github projects found yet |
| "Venezuela earthquake" + "open data" + dataset | ⭐⭐⭐⭐⭐ | Microsoft AI4G dataset on HDX + Vantor Open Data Program — major finds |
| "Venezuela earthquake" + death toll + latest | ⭐⭐⭐⭐ | Toll escalated to 920+; USGS estimates possible 10,000+ |
| site:reliefweb.int Venezuela earthquake 2026 | ⭐⭐⭐⭐⭐ | Best source for structured situation reports |

### What's working:
- **HDX/humdata.org** is the best source for ML-ready datasets — check daily
- **ReliefWeb** is the best source for structured damage/needs data — new sitreps daily
- **Vantor + Microsoft AI4G** are the two key data releases so far
- **LinkedIn** (Pete Masters, Vantor) is surprisingly good for activation announcements

### What's not working:
- No github projects yet — opportunity for us to be first
- No formal HOT-OSM tasking manager link yet — monitor the OSM forum thread
- X/Twitter search via web_search is limited — need direct X access for OSINT mining
