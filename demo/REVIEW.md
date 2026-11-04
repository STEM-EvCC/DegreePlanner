# STEM and health demo: review notes

The demo at `demo/` is a separate copy of the Degree Planner for EvCC's sciences, health sciences and Advanced Manufacturing programs. It reads `demo/data.json` only. The live planner, PathwaysData and the Pathways site don't see any of it.

Live demo (once this branch is merged and Pages has updated): `https://stem-evcc.github.io/DegreePlanner/demo/`

## What's in it

| Area | EvCC programs | Transfer and next-step data |
|---|---|---|
| Sciences | Biology AS-T Track 1, Chemistry AS-T Track 1, Geology AS-T Track 1, Physics and Astronomy AS-T Track 2 | Biology at 9 schools; chemistry, biochemistry, physics, astronomy and geology at UW Seattle, UW Bothell, WWU, WSU Pullman, CWU, EWU; statewide AS-T Track 1 and 2 agreements |
| Nursing | Associate in Nursing DTA/MRP (RN), Associate in Pre-Nursing DTA/MRP | Pre-licensure BSN: UW Seattle, WSU (Spokane, Tri-Cities), Seattle U, SPU, PLU, Northwest U. RN to BSN: UW Bothell, UW Tacoma, WWU, WSU. Statewide nursing agreements |
| Allied health | DTA with Allied Health emphasis | Dental hygiene, sonography, respiratory care, public health, healthcare leadership, nutrition and exercise physiology (10 programs) |
| Health careers | Medical Assistant (certificate, ATA; AAS-T left out for now), Medical Billing and Coding (ATA, 2 certificates), Phlebotomy, Nursing Assistant, EMT, Medical Interpreter (Spanish), Healthcare Risk Management | Career paths with certifications, BLS wages (WA, Seattle area, US), and BAS next steps at Bellevue, Edmonds, Seattle Central, Tacoma CC, LWTech, Skagit, Columbia Basin, CityU |
| Advanced Manufacturing | All 25 AMTEC programs, moved here from the live data | Unchanged from the live data |

EvCC's 2026-27 catalog has no math degree or math emphasis, so math appears through the degrees above. Aviation Maintenance, Avionics and Fire Science are not included (EvCC doesn't list them under STEM).

Every university entry carries its sources and a `verified` status (see **Data & sources** in the demo's footer). Most are "partial": several universities' equivalency tools and catalogs load only with scripts and couldn't be read, so some course matches are by subject and flagged "confirm" in their notes.

## Editing

- Facts: edit `demo/data.json`, then run `python3 demo/validate.py` (same checks as PathwaysData, plus the `science` and `health` areas).
- Page: the demo page is generated from the live `index.html` so it keeps every fix made there. After changing `index.html` or `demo/explore.js`, run `python3 demo/build_demo.py`.
- When a program is approved, move its entries into PathwaysData's `data.json` (add `science`/`health` to the schema's area list first).

## Questions for you

### Catalog questions (EvCC)
1. ~~**Physics and Astronomy AS-T**: the printed blocks add to 85 credits, but the page says 90.~~ **Decided:** the total is 90. The demo adds a 5-credit "Additional credits to reach 90" block, to plan with an advisor, until the catalog says where they come from.
2. **Chemistry AS-T**: the 93 total assumes the physics choices. With BIOL& 221-223 instead it's 94.5.
3. **PHYS& 116** lists PHYS& 114 as its prerequisite, not PHYS& 115. **PHYS& 115** lists MATH 138. Is MATH 138 current?
4. **Geology AS-T** electives include MFG T 105 at 20 credits.
5. ~~**Biology AS-T** physics~~ **Decided:** added an advisor note (plan on PHYS& 114-116 or the calculus series and check each school) and a hint on the PHYS& 114 choice.
6. **Nursing admission criteria** (points, GPA, deadlines, tests): **Decided:** the Nursing office can supply them, but they stay out of the demo for now. The demo shows only what the catalog says.
7. **Medical Assistant AAS-T**: blocks add to 98, catalog says 99. **Decided:** the AAS-T is left out of the demo for now (the certificate and ATA stay). Also unresolved for the certificate and ATA: The line "HLTH 130 or BIOL 105 or ANTH& 206 and BIOL& 231 and 232" is modeled as pick one of the first three. "BUS 130 or MATH/TS 76" has no credit value (counted as 5).
8. **Medical Billing and Coding ATA**: no total-credits line (blocks add to 90). Its elective list names CL 105, which isn't in the 2026-27 course catalog.
9. **EMT certificate** lists a 30-credit residency minimum and a Diversity requirement that can't apply to a 13-16 credit certificate.
10. Should Billing and Coding list CPC, CPB and CBCS? Only AHIMA's CCA is named in the catalog.

### Transfer questions
11. **UW physics credit**: does UW credit EvCC PHYS& 241-243 as PHYS 121-123, or as 121, 122 and 2XX? UW teaches E&M second; EvCC teaches it third. UW's 2024 Everett planning sheet shows PHYS& 242 as PHYS 2XX. This affects UW Physics, Astronomy **and the live engineering data**, which maps 242 to PHYS 122.
12. **UW Seattle Biology** is a single BS/BA from Fall 2026 (the EEC, MCD, Physiology and Plant options are gone). **WWU Biology** is one BS with seven concentrations.
13. **UW Tacoma** has no Biology major; BS Biomedical Sciences is listed under Biology. Keep it there?
14. **CWU** recommends the AA-DTA over the AS-T for Biology (AS-T students owe extra general education).
15. **WSU RN to BSN**: does WSU accept the ADN's built-in nutrition credits and ANTH& 206 for its Human Nutrition and Intro to Sociology requirements?
16. **Seattle U Nursing**: which EvCC courses count for Introductory Biology and College Algebra?
17. **Statewide nursing agreements**: the Pre-Nursing DTA/MRP (2020) was due for renewal by Summer 2025. Is there a newer one?
18. Add Saint Martin's, Walla Walla, EWU or WGU nursing? Community-college RN to BSN programs (Bellevue, LWTech)? Bellevue and Tacoma CC sonography (associate level)?
19. **WWU RN to BSN**: is there an Everett cohort? The application page lists Everett; the program pages don't.
20. **EWU dental hygiene**: how do EvCC's two-course chemistry and A&P map to EWU's three-course series?
21. **WWU Geology**: admissions lists the BS as direct admission; the department still describes a Phase I/II step. **WWU Biochemistry**: BIOL 204 and 205, or only 205?
22. **UW Astronomy deadline**: catalog says Apr 5 and Oct 5; department says the third Friday of autumn and spring quarters.
23. **Healthcare Risk Management certificate**: which career direction should it point to? Next steps currently assume healthcare management.
24. Not included because no readable page gave requirements: WSU Biochemistry, CWU BS Geology (only Environmental Geological Sciences is in).
