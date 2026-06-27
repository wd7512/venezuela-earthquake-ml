# Information Scouting — Forum & Social Media Intelligence

Last updated: 2026-06-27 23:45 UTC (evening scout — Life-saving window closing + new imagery + detailed ground truth)
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
- **Note:** HOT-OSM has now formally activated (see below). This forum thread was the initial call; the official response is now at hotosm.org.

---

## HOT-OSM (Humanitarian OpenStreetMap Team) — ✅ FORMALLY ACTIVATED

- **Official project page:** https://www.hotosm.org/en/projects/2026-venezuela-earthquake-response/
- **Activation announced:** ~2 days ago (June 25, 2026)
- **What they're doing:**
  - Using **fAIr** (their AI-assisted mapping tool) to identify geospatial data gaps
  - Building **building density maps** for Caracas and La Guaira
  - Running remote mapping campaigns via Tasking Manager
  - Sharing available satellite imagery through their Portal
- **Portal features:**
  - Remote mapping campaigns (link: https://tasks.hotosm.org — check for Venezuela projects)
  - Available data: area of interest, buildings, building density, healthcare sites
  - fAIr building density predictions cover Caracas and La Guaira urban areas
- **HDX data:** https://data.humdata.org/event/venezuela-earthquake (includes fAIr predictions)
- **Contact:** disasterservices@hotosm.org
- **ML relevance:** ⭐⭐⭐⭐⭐ — HOT is literally doing AI-assisted damage mapping. Their fAIr tool produces building density maps. We should coordinate with them — their tasking manager could be a channel to offer ML-based damage assessment.
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
- [ ] ~~Check if HOT-OSM has imagery partnerships (Planet, Maxar) we can piggyback on~~ — ✅ DONE: HOT activated with fAIr; check their Portal for available imagery
- [ ] Set up X search alerts for "Venezuela terremoto daño colapsado" with geolocation
- [ ] Download & evaluate Microsoft AI4G Catia La Mar dataset as training/validation data
- [ ] Access Vantor Open Data Program imagery for broader coverage
- [ ] Mine OCHA SitRep #3 for structured damage/needs data
- [ ] **NEW:** Monitor Copernicus EMSR884 activation page for grading map releases (check daily)
- [ ] **NEW:** Check HOT-OSM Tasking Manager for Venezuela mapping projects to contribute to
- [ ] **NEW:** Download HOT fAIr building density predictions from HDX when available
- [ ] **NEW:** Watch for Copernicus EMS grading maps — use as ground-truth labels
- [ ] **NEW:** Consider InSAR change detection as secondary ML product (ground displacement)
- [ ] **NEW:** Reach out to HOT-OSM via disasterservices@hotosm.org to offer ML damage mapping

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

## 🔥 NEW HIGH-VALUE INTEL (2026-06-27 Late Scout)

### 1. HOT-OSM — Formally Activated with fAIr AI Mapping
- **URL:** https://www.hotosm.org/en/projects/2026-venezuela-earthquake-response/
- **Status:** ✅ Active. HOT is using their **fAIr** AI-assisted mapping tool for building density estimation in Caracas and La Guaira
- **HDX datasets:** https://data.humdata.org/event/venezuela-earthquake — includes fAIr building density predictions (GeoPackage + SHP)
- **ML relevance:** ⭐⭐⭐⭐⭐ — HOT is doing AI-assisted mapping. Their fAIr tool produces building density maps. Direct coordination opportunity: offer ML damage assessment via their Tasking Manager
- **Action:** Monitor tasks.hotosm.org for Venezuela mapping projects we can contribute to

### 2. Copernicus EMS — Rapid Mapping Activated (EMSR884) — 13 Sectors
- **Activation page:** https://mapping.emergency.copernicus.eu/activations/EMSR884/
- **News post:** https://mapping.emergency.copernicus.eu/news/earthquake-in-venezuela-emsr884/
- **What:** EU Copernicus EMS activated Rapid Mapping for Venezuela earthquake. **13 sectors selected for damage assessment grading maps**
- **Sectors include:** Caracas, Petare, Maracay (and ~10 others) — covering the most affected urban areas
- **Products to expect:** Grading maps (damage severity), vector packages (GeoPackage/Shapefile), PDF maps
- **Imagery source:** Very High Resolution (VHR) Copernicus Contributing Missions
- **ML relevance:** ⭐⭐⭐⭐⭐ — Free damage grading maps will be published. These are ground-truth labels we can use for:
  - Training data (damage classification per building/area)
  - Validation of our own model outputs
  - Benchmark comparison
- **Timeline:** Products typically delivered within hours-days of imagery acquisition

### 3. New GitHub Project — Copernicus Data Dashboard
- **URL:** https://github.com/YIN-Renlong/venezuela-earthquake-copernicus-data-dashboard-2026
- **What:** Unofficial public dashboard using Copernicus EMS Rapid Mapping data for activation EMSR884
- **ML relevance:** ⭐⭐⭐ — Shows community interest in the data. Could be a model for our own visualization/dashboard

### 4. Scientific Analysis — InSAR Ground Displacement Data
- **Source:** https://earthquakeinsights.substack.com/p/early-scientific-picture-of-the-deadly (June 26, 2026)
- **Key findings:**
  - Radar-based satellite imagery (InSAR) reveals ground displacement areas
  - Earthquake started near San Felipe and propagated nearly uniformly eastward toward Caracas
  - Complex fault rupture on Bocono fault system
- **New scientific article (June 26):** https://www.science.org/content/article/venezuela-s-double-earthquake-struck-faults-scientists-had-flagged
  - Centuries of strain had built up on faults in the region
  - The doublet struck faults scientists had previously flagged as overdue
- **ML relevance:** ⭐⭐⭐ — InSAR coherence/change detection is itself an ML task. Could be a secondary product (ground displacement detection from SAR)

### 5. Updated Casualty & Impact Figures
- **Death toll:** 920+ confirmed (per Anadolu Agency, Wikipedia, multiple sources)
- **Earlier figures:** 164→188→235→589→920 (escalating as rescue progresses)
- **Injured:** 3,360+ (some sources say 4,300+)
- **Buildings damaged/collapsed:** 250+ identified by early assessments (ENR)
- **People still missing:** 200+ (per ENR 1-day-old report)
- **International rescue teams deployed:**
  - Switzerland: 80 rescuers (arrived first, per Guardian)
  - Mexico: 250 rescuers
  - El Salvador: 188 rescuers
  - Spain: ~100 rescuers
  - Colombia: 63-member rescue team
  - Dominican Republic: first to deploy to La Guaira
  - Brazil, Canada, UK: supporting/standby

### 6. Miyamoto International — Additional Detail from Their Assessment
- **New finding:** "In parts of southeastern Caracas, nearly all high-rise buildings sustained heavy damage or collapsed entirely"
- **250+ damaged or collapsed buildings** identified in early assessments
- **200+ people still trapped/missing** in rubble (1-day-old report)
- Their rapid exposure assessment and update posts remain the key structured data sources

### 7. Euronews — Before/After Gallery (Updated)
- **URL:** https://www.euronews.com/2026/06/27/venezuela-satellite-images-reveal-scale-of-disaster
- Updated gallery with Vantor imagery showing La Guaira destruction

---

## Search Effectiveness Log

| Query | Result | Notes |
|-------|--------|-------|
| "Venezuela earthquake" + damage + satellite | ⭐⭐⭐⭐⭐ | Rich results — Vantor imagery, Microsoft dataset, Euronews gallery |
| "Venezuela earthquake" + HOT-OSM + activation | ⭐⭐⭐⭐⭐ | **MAJOR: HOT formally activated** with fAIr AI mapping + building density maps for Caracas & La Guaira |
| "Venezuela earthquake" + Miyamoto | ⭐⭐⭐⭐ | New detail: "nearly all high-rise buildings sustained heavy damage or collapsed" in SE Caracas |
| "Venezuela earthquake" + ReliefWeb + situation report | ⭐⭐⭐⭐⭐ | Multiple sitreps now available (#1, #2, #3, IOM, UNICEF) |
| "Venezuela earthquake" + github + machine learning | ⭐⭐⭐ | New GitHub project: Copernicus Data Dashboard (YIN-Renlong) using EMSR884 data |
| "Venezuela earthquake" + "open data" + dataset | ⭐⭐⭐⭐⭐ | Microsoft AI4G dataset on HDX + Vantor Open Data Program — major finds |
| "Venezuela earthquake" + death toll + latest | ⭐⭐⭐⭐ | Toll escalated to 920+; USGS estimates possible 10,000+ |
| site:reliefweb.int Venezuela earthquake 2026 | ⭐⭐⭐⭐⭐ | Best source for structured situation reports |
| "EMSR884" + Venezuela + Copernicus | ⭐⭐⭐⭐⭐ | **MAJOR: 13 sectors selected** for damage grading maps — free ground-truth data coming |
| "Venezuela earthquake" + InSAR + radar | ⭐⭐⭐⭐ | New scientific analysis — InSAR ground displacement data from Sentinel-1; Science.org article |
| "Venezuela earthquake" + Copernicus + 13 sectors | ⭐⭐⭐⭐ | MichelBaljet tweet confirms sectors include Caracas, Petare, Maracay + ~10 more |
| "Venezuela earthquake" + international rescue teams | ⭐⭐⭐⭐ | Detailed deployment list: Mexico 250, El Salvador 188, Spain ~100, Switzerland 80, Colombia 63 |

### What's working:
- **HDX/humdata.org** is the best source for ML-ready datasets — check daily
- **ReliefWeb** is the best source for structured damage/needs data — new sitreps daily
- **Vantor + Microsoft AI4G** are the two key imagery/data releases so far
- **Copernicus EMS** (mapping.emergency.copernicus.eu) — activation EMSR884 will produce free grading maps = ground truth
- **HOT-OSM website** (hotosm.org/en/projects/...) — now the best source for AI-mapping coordination
- **LinkedIn** (Pete Masters, Vantor) is surprisingly good for activation announcements
- **X/Twitter** (MichelBaljet, CopernicusEMS) — good for activation details (sector lists, product status)

### What's not working:
- GitHub projects are just starting — we still have an opportunity to be the primary ML project
- X/Twitter search via web_search is limited — need direct X access for OSINT mining
- Full list of 13 Copernicus sectors not yet public — check the EMSR884 activation page for updates

---

## 🔥 NEW HIGH-VALUE INTEL (2026-06-27 Evening Scout — Life-Saving Window Closing)

### 1. HOT-OSM Tasking Manager — TWO Active Venezuela Earthquake Projects (Live Stats)
- **Project #54390:** "OSM Venezuela Earthquake 2026 Response - Buildings (4)"
  - URL: https://tasks.hotosm.org/projects/54390
  - Priority: URGENT | Org: Open Mapping Hub LAC
  - Status: 14 contributors, 29% mapped, 6% validated
- **Project #54159:** "OSM Venezuela Earthquake 2026 Response - Buildings (3)"
  - URL: https://tasks.hotosm.org/projects/54159
  - Priority: URGENT | Org: Open Mapping Hub LAC
  - Status: 196 contributors, 98% mapped, 86% validated (!!)
- **Key finding:** Project #54159 is 98% MAPPED with 197 contributors — OSM community has been extremely active
- **ML relevance:** ⭐⭐⭐⭐ — The mapping is mostly done; the remaining opportunity is damage ASSESSMENT (not building mapping). Their data gives us building footprints; the tasking footprint boundaries define our AOIs.

### 2. Vantor — Continued Imagery Updates
- Vantor (@shafeKoreshe, X): "Vantor said it would continue uploading new imagery to aid damage assessment, infrastructure mapping, and resource allocation"
- AP/CNN now have before/after Vantor imagery for Caraballeda specifically (Dec 28, 2025 vs June 26, 2026)
- CNN reel: 14K likes, 345 comments on the Vantor imagery — massive public engagement
- **ML relevance:** ⭐⭐⭐⭐⭐ — New imagery keeps being uploaded. Check Vantor Open Data Program page regularly for more before/after pairs.

### 3. HDX — Updated OSM + Overture Data (June 25-26)
- **New dataset:** "Venezuela - M 7.5 Earthquake - June 2026 - OSM & Overture Data"
  - Org: HOT (Humanitarian OpenStreetMap Team)
  - Time period: 25 June 2026 - 26 June 2026
  - Available at: https://data.humdata.org/group/ven
  - **Includes both OSM AND Overture Maps Foundation data** — this is NEW and significant
- **Total HDX crisis page:** 30+ datasets from UNOSAT, MSFTResearch, HOT, GIScienceHD, and others
- **Also listed:** Health facilities datasets specific to the earthquake zone
- **ML relevance:** ⭐⭐⭐⭐⭐ — Overture Maps data gives us authoritative building footprints (often better than OSM in underserved areas). Combined with OSM post-event data, this enables change detection.

### 4. Updated Casualty Figures & Impact Scale
- **Death toll:** 920+ confirmed (per gov, reported by BBC, CNN, CNBC, Al Jazeera)
- **Tens of thousands missing:** Government reports >50,000 people missing (per RT, Metro News, Yahoo News)
- **Economic loss:** UNDP estimates **US$6.7 billion** in direct damage (updated from earlier $4.7-8.7bn range)
- **Guardian:** "More than 100 buildings collapsed in La Guaira... declared a disaster zone"
- **NYT interactive damage map:** https://www.nytimes.com/interactive/2026/06/25/world/americas/venezuela-earthquake-map-damage.html
  - Photos show Petunia residential building in Los Palos Grandes "reduced to rubble"
- **CNN live updates still running** (June 27) — rescue race against time

### 5. Detailed Ground-Truth Building Collapse Info
- **Petunia Residences, Los Palos Grandes (Caracas):**
  - 13-story apartment building partially collapsed — 14 floors pancaked, only 6 intact
  - NPR: "More than a dozen people were rescued from the building"
  - NYT: Before/after photos show near-total destruction
  - This is a SPECIFIC geolocated collapse with rescue outcome data — excellent ML training example
- **Altamira (Caracas):** Three buildings collapsed
- **La Guaira (Caraballeda):** Multiple high-rise collapses — AP has new satellite before/after for this exact area

### 6. Aftershock Update — M4.9 on June 26
- **June 26 afternoon:** M4.9 earthquake struck off northern coast of Venezuela
- Per Al Jazeera, Reuters, multiple sources
- Caused continued stress on already-damaged structures
- **Aftershock count:** 300+ total since mainshock (per OCHA SitRep #3)

### 7. Scientific Analysis Deep Dives
- **American Geophysical Union (EOS):** "Venezuelan Earthquakes Struck in a Complex Zone of Faults"
  - USGS map shows shaking intensity across northern Venezuela
  - Detailed tectonic analysis of the doublet mechanism
  - URL: https://eos.org/research-and-developments/venezuelan-earthquakes-struck-in-a-complex-zone-of-faults
- **CRV Science:** "Anatomy of a Disaster: The June 2026 Venezuelan Seismic Doublet"
  - Comprehensive analysis of rupture mechanics + geotechnical amplification in Caracas basin
  - URL: https://www.crvscience.com/post/anatomy-of-a-disaster-the-june-2026-venezuelan-seismic-doublet
- **British Geological Survey** posted preliminary info on Facebook (cross-organization awareness)
- **ML relevance:** ⭐⭐⭐ — Understanding WHY certain structures failed helps us engineer features (soil amplification, building age, floor count)

### 8. UNDP RAPIDA Assessment
- **UNDP press release (June 26):** "Venezuela faces US$6.7 billion in economic losses"
- Uses **RAPIDA** tool: combines satellite imagery + GIS for rapid damage assessment
- This is itself an ML-adjacent damage assessment — UNDP's methodology is public
- URL: https://www.undp.org/press-releases/venezuela-faces-us67-billion-economic-losses-earthquakes-undp-estimates

### 9. CRSV Science / ABC Australia — Damage Lessons
- ABC Australia (June 27): "Venezuela: Caracas assess damage after doublet earthquake"
  - Geotechnical failure lessons + slope risks
  - URL: https://www.abc.net.au/news/2026-06-27/venezuela-caracas-assess-damage-after-doublet-earthquake/106843050

---

## Search Effectiveness Log (Updated)

| Query | Result | Notes |
|-------|--------|-------|
| "Venezuela earthquake" + damage + satellite | ⭐⭐⭐⭐⭐ | Rich results — Vantor imagery, Microsoft dataset, Euronews gallery |
| "Venezuela earthquake" + HOT-OSM + activation | ⭐⭐⭐⭐⭐ | **MAJOR: HOT formally activated** with fAIr AI mapping + building density maps for Caracas & La Guaira |
| tasks.hotosm.org + Venezuela text-search | ⭐⭐⭐⭐⭐ | **TWO active projects (#54159, #54390). #54159 is 98% mapped with 197 contributors** |
| humdata.org + Venezuela + earthquake | ⭐⭐⭐⭐⭐ | 30+ datasets now. NEW: OSM + Overture Maps combined dataset |
| humdata.org + Venezuela + Overture | ⭐⭐⭐⭐⭐ | NEW dataset combining OSM + Overture Maps Foundation data for building footprints |
| "Venezuela earthquake" + Petunia + collapse | ⭐⭐⭐⭐ | Specific building collapse details — Petunia Residences, 13-story, 14 floors collapsed |
| "Venezuela earthquake" + Miyamoto | ⭐⭐⭐⭐ | New detail: "nearly all high-rise buildings sustained heavy damage or collapsed" in SE Caracas |
| "Venezuela earthquake" + ReliefWeb + situation report | ⭐⭐⭐⭐⭐ | Multiple sitreps now available (#1, #2, #3, IOM, UNICEF) |
| "Venezuela earthquake" + github + machine learning | ⭐⭐⭐ | New GitHub project: Copernicus Data Dashboard (YIN-Renlong) using EMSR884 data |
| "Venezuela earthquake" + "open data" + dataset | ⭐⭐⭐⭐⭐ | Microsoft AI4G dataset on HDX + Vantor Open Data Program — major finds |
| "Venezuela earthquake" + death toll + latest | ⭐⭐⭐⭐ | Toll escalated to 920+; USGS estimates possible 10,000+ |
| site:reliefweb.int Venezuela earthquake 2026 | ⭐⭐⭐⭐⭐ | Best source for structured situation reports |
| "EMSR884" + Venezuela + Copernicus | ⭐⭐⭐⭐⭐ | **MAJOR: 13 sectors selected** for damage grading maps — free ground-truth data coming |
| "Venezuela earthquake" + InSAR + radar | ⭐⭐⭐⭐ | New scientific analysis — InSAR ground displacement data from Sentinel-1; Science.org article |
| "Venezuela earthquake" + Copernicus + 13 sectors | ⭐⭐⭐⭐ | MichelBaljet tweet confirms sectors include Caracas, Petare, Maracay + ~10 more |
| "Venezuela earthquake" + international rescue teams | ⭐⭐⭐⭐ | Detailed deployment list: Mexico 250, El Salvador 188, Spain ~100, Switzerland 80, Colombia 63 |
| "Venezuela earthquake" + UNDP + RAPIDA | ⭐⭐⭐⭐ | NEW: UNDP direct damage estimate $6.7bn using satellite+GIS RAPIDA tool |
| "Venezuela earthquake" + "4.9" aftershock | ⭐⭐⭐⭐ | M4.9 aftershock on June 26 — Reuters + Al Jazeera covered |
| "Venezuela earthquake" + Overture Maps | ⭐⭐⭐⭐ | NEW: HDX dataset now combines OSM + Overture Maps data |

### What's working:
- **HDX/humdata.org** is the best source for ML-ready datasets — now 30+ datasets including OSM+Overture combined
- **HOT Tasking Manager** — live project stats give us contributor engagement metrics and AOI boundaries
- **ReliefWeb** is the best source for structured damage/needs data — new sitreps daily
- **Vantor + Microsoft AI4G** are the two key imagery/data releases so far; Vantor continuing to upload
- **Copernicus EMS** (mapping.emergency.copernicus.eu) — activation EMSR884 will produce free grading maps = ground truth
- **HOT-OSM website** (hotosm.org/en/projects/...) — now the best source for AI-mapping coordination
- **LinkedIn** (Pete Masters, Vantor) is surprisingly good for activation announcements
- **X/Twitter** (MichelBaljet, CopernicusEMS) — good for activation details (sector lists, product status)
- **Searching specific building names** (Petunia, Altamira) yields detailed ground-truth collapse data
- **humdata.org + "Overture"** — newly discovered source for combined building footprint datasets

### What's not working:
- GitHub projects are just starting — we still have an opportunity to be the primary ML project
- X/Twitter search via web_search is limited — need direct X access for OSINT mining
- Full list of 13 Copernicus sectors not yet public — check the EMSR884 activation page for updates
- HDX event page returns 403 sometimes — use https://data.humdata.org/dataset?vocab_Topics=crisis-venezuela-earthquake instead
- HDX returns occasionally block Google Search — cache results quickly
