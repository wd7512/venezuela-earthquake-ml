# Track 6: Missing Persons Aggregation & Image Matching

## Goal
Aggregate scattered missing-person reports into a structured, searchable database. Explore image-matching as a supplementary tool with strict ethical guardrails.

## Context
- 50,000+ people reported missing after the June 24 doublet
- Families posting photos + descriptions on X, Instagram, Facebook, handwritten flyers
- Multiple fragmented databases already exist (see below)
- 6,000+ already found — but no unified system connecting reports to found persons

## Existing Databases
| Name | URL | Notes |
|------|-----|-------|
| Desaparecidos Terremoto Venezuela | (site has been unstable) | Opposition-run; 57,000+ reports, 6,000+ found |
| Venezuela Te Busca | — | Alternative registry |
| TerremotoVE | KoboToolbox form | Structured data collection |
| ICRC Family Links | familylinks.icrc.org | Red Cross global RFL network; may not be activated yet |

## Pipeline (Text-Based — Low Risk)

1. **Scrape** missing persons posts from X, Instagram, Facebook (Spanish-language: "buscando", "desaparecido", "terremoto", + name/age/location)
2. **Aggregate** into unified database: name, age, description, last known location, photo URL, contact info, source
3. **Normalise** names (accents, nicknames, spelling variants)
4. **Deduplicate** — same person reported across multiple platforms
5. **Cross-reference** with found-persons lists, hospital registries, shelter lists (if available)
6. **Publish** searchable database for families + responders

## Image Matching — ⚠️ STRONG ETHICAL CONCERNS

### What it would do
- Match a family's photo of a missing person against:
  - Photos from survivors in hospitals/shelters
  - Social media posts showing people alive in shelters
  - (NOT morgue photos — that's forensic DVI, separate protocol)

### Why this is high-risk

**1. Privacy & Biometric Data**
- Facial recognition = biometric processing under GDPR and most privacy laws
- Missing persons cannot consent; families can consent on their behalf, but legal basis in disaster context is unclear
- Collecting/building a face database at scale without institutional backing is legally and ethically dangerous

**2. Accuracy & Harm**
- False positive in this context is devastating: family told their loved one is alive when they're not, or vice versa
- Disaster imagery is low-quality: dust, injuries, poor lighting, occlusion — FR accuracy degrades significantly
- No seismology or ML model should be the sole basis for confirming someone's death or survival

**3. Institutional Protocols Exist for a Reason**
- Interpol DVI (Disaster Victim Identification) uses fingerprints, dental records, DNA — NOT facial recognition as primary ID
- ICRC has formal Restoring Family Links protocols with trained staff
- Facial recognition is supplementary at best, and only with trained human review
- Building a parallel technical system outside these frameworks risks undermining the formal process

**4. Precedent**
- PimEyes scraping images of deceased people for FR training has been documented in AI incident databases as harmful
- Using FR on vulnerable populations (disaster survivors, missing persons' families) without institutional oversight is widely considered unacceptable

### Conditions under which image matching could be considered
- ✅ Explicit, informed consent from family for their specific photo
- ✅ Institutional backing (ICRC, Interpol DVI, Venezuelan authorities)
- ✅ Only as a ranking/suggestion tool — never definitive identification
- ✅ Only against survivor photos, never morgue imagery
- ✅ Human expert review of every match before any family notification
- ✅ Clear data retention/deletion policy
- ❌ NOT a solo open-source project by unaffiliated individuals

## Recommended Approach

**Phase 1 (do now):** Text-based aggregation + deduplication + cross-referencing. High value, low risk, immediately useful.

**Phase 2 (with partners):** If ICRC or Red Cross activates and wants technical support for image matching, contribute within their framework with their ethical oversight.

**Phase 3 (research):** Publish on the challenges and ethical framework for FR in disaster contexts — contributes to the field without building harmful tooling.

## Open Questions
- [ ] Can we access the Desaparecidos Terremoto Venezuela database directly (API, export)?
- [ ] Is ICRC Family Links activated for this event?
- [ ] What data protection laws apply to Venezuelan citizens' biometric data processed abroad?
- [ ] Are hospital/shelter registries being published in any structured format?
