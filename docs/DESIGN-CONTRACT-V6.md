# Capital Place — Design Contract V6

Checked: 2026-09-01
Mode: interactive/static leasing prototype

## 1. Business ↔ user match

Owner wants to show:
- Capital Place as a landmark Grade A business address in Hanoi.
- Twin-tower scale, architecture and local identity.
- Workplace suitability and floor-planning flexibility.
- Sustainability credentials and measurable operating evidence.
- Amenities/community as part of the tenant proposition.
- A clear path to a qualified leasing enquiry/private viewing.

Users need to decide:
- Is this the right address for our company and people?
- Does the building/floor plate fit our team and workplace strategy?
- What is the day-to-day employee/client experience?
- Does the building support ESG / sustainability requirements?
- What space is actually available and how do we proceed?

Primary decision journey:
`landmark/brand → location → workplace fit → amenities/experience → ESG proof → availability planning → leasing conversation`

Secondary journeys:
- broker/consultant: `facts → floor plan/specs → availability → leasing`
- visitor: `location → arrival → amenities → contact`

## 2. Source of truth

First-party Capital Place pages:
- https://capitalplace.com.vn/
- https://capitalplace.com.vn/location-2/
- https://capitalplace.com.vn/office/
- https://capitalplace.com.vn/sustainability-and-community/
- https://capitalplace.com.vn/the-link/
- https://capitalplace.com.vn/contact-us/

Verified public facts used in V6:
- 29 Lieu Giai, Ngoc Ha, Hanoi.
- Grade A office.
- 93,000 sqm leasable area.
- 2 towers / 37 storeys each.
- Published reference floor plate: 1,847 sqm.
- Published planning: occupancy 184; 156 workstations; 16 offices; 7 MD offices; 60 meeting-room seats.
- LEED Platinum O+M + LEED Gold BD+C.
- Published sustainability metrics remain qualified as published figures.
- Hotline 1800 9289 / leasing@capitalplace.vn.

System reality:
- No verified live vacancy feed.
- No verified pricing feed.
- No CRM/booking backend in this GitHub Pages prototype.
- Availability pages are planning/decision support; Leasing confirms current conditions.

## 3. Design DNA

Direction:
**Architectural Editorial × Leasing Blueprint × Hanoi Landmark**

Domain artifacts:
- tower elevation → page composition / scale
- floor plan → office and availability decision object
- building directory → information hierarchy / navigation mental model
- architectural datum line → recurring orange wayfinding cue
- leasing brochure/spec sheet → technical information rhythm

Fidelity: L1–L2 by default. Floor plan/elevation can use L3 when they are the real decision objects.

## 4. Visual rules

Color roles:
- Graphite `#1D1B1A`: architecture, high-value proof, nav, decision bands.
- Architectural white `#FFFFFF`: clarity, office/spec surfaces.
- Warm stone `#F2EEE7`: editorial/supporting information.
- Capital orange `#F15F22`: wayfinding datum, active state, primary leasing CTA, evidence emphasis.

Do not use orange as general decoration.

Typography:
- DM Sans, light/regular for large editorial display.
- Strong size contrast, compressed leading, architectural poster rhythm.
- Body copy 16–19px with readable line length.
- Kicker/action labels uppercase but never microtype below practical readability.

Shape/elevation:
- square/planar controls; no SaaS pill language.
- minimal shadow; rely on line, contrast and composition.
- no generic rounded card grid as dominant pattern.

Imagery:
- real Capital Place assets first.
- large crops with architecture/workplace purpose.
- floor plans shown as information objects, not decoration.

## 5. Page compositions

### Overview
1. Split monument hero: graphite manifesto + tower media.
2. Identity: facade/lobby / Thang Long story.
3. Capital Address: map + business/diplomatic context.
4. Workplace: 1,847 sqm floor plan as primary object.
5. Workday: Nexus / Premium Lounge / The Link.
6. Sustainability evidence.
7. Find a Space conversion.

### Location
1. Address hero.
2. City context map.
3. Connection metrics.
4. Surroundings photography.
5. MRT/future connectivity with qualifier.
6. Plan a Visit.

### Office
1. Workplace hero.
2. Twin-tower anatomy/elevation.
3. Building scale/spec band.
4. Published 1,847 sqm planning reference.
5. Workplace quality/panorama.
6. Technical decision layer.
7. Availability CTA.

### Sustainability
1. Certification-led hero.
2. Dual LEED evidence.
3. Building-system performance matrix.
4. Community participation.
5. Tenant value / ESG request.

### Amenities
1. Workday hero.
2. Day timeline.
3. The Nexus.
4. The Link.
5. Hospitality spaces.
6. Wellbeing.
7. Visit CTA.

### Availability
1. Transparent planning-mode hero.
2. Requirement form.
3. Published floor-plan reference.
4. Explicit list of what Leasing must confirm.
5. Leasing CTA.

### Leasing
1. Qualified-enquiry hero.
2. Direct contact + short requirement form.
3. Prototype prepares email only.
4. Explain next-step sequence.

## 6. Non-negotiables

- No fake live inventory, pricing, booking, CRM or real-time status.
- No white logo on white nav state.
- Primary CTA never outline-only on a light surface.
- Page compositions must differ according to the decision task.
- Preserve real official imagery/content facts.
- Mobile is a recomposition, not desktop shrunk down.
- Utility/support pages may be simpler but should inherit the same navigation, typography and color role system.
