# Capital Place — Pre-Design Research & UI/UX Upgrade v3

Date: 2026-09-01

Basis: MASTER PRE-DESIGN RESEARCH PROMPT v2 + `Ngh1aa/skills_UIUX` adaptive routing.

## 01 — Executive Summary

Capital Place should remain an architecture-led Grade A office website, but every major page must also function as a leasing decision-support surface. The current redesign already moved substantially beyond a brochure through Space Finder, availability states, floor detail, viewing and qualified enquiry flows. v3 therefore does **not** replace the current experience. It strengthens orientation, brand distinction, trust and responsive interaction while preserving the established visual language and conversion architecture.

Primary outcome:

`Discover → understand location/building → evaluate workplace/specs/amenities/ESG → find a suitable space → request viewing / leasing contact`

The visual direction remains graphite / cream / white with a controlled orange accent, cinematic Capital Place photography, large editorial typography and floor-plan information. The upgrade adds a more architectural grammar: planar geometry, survey/elevation rules, section numbering and a page-directory pattern derived from building wayfinding rather than generic SaaS cards.

## 02 — Evidence & Unknowns

| Information | Finding | Source | Status | Design implication |
|---|---|---|---|---|
| Building | Capital Place is a Grade A office complex with 2 towers and 37 storeys | capitalplace.com.vn/office | FACT | Keep scale visible early |
| Area | Official site states 93,000 sqm office/retail space | capitalplace.com.vn/office | FACT | Keep centralised fact; no conflicting values |
| Sustainability | LEED Platinum O+M + LEED Gold BD+C | official site + Capital Place LinkedIn | FACT | ESG is decision proof, not decoration |
| Location | 29 Lieu Giai, Ngoc Ha, Hanoi | official site | FACT | Location page must explain business utility, not only map |
| Conversion | Official site exposes leasing enquiry, email and hotline | official site | FACT | Leasing is the principal commercial conversion |
| Floor planning | Official site publishes a 1,847 sqm planning reference with 184 pax example | official office page | FACT | Floor plan / capacity should remain decision objects |
| Live inventory | Official public source does not provide a complete real-time commercial inventory API | research + current prototype contract | UNKNOWN / NOT VERIFIED | Never present prototype floor states as live truth |
| Pricing / commercial terms | Not published as reliable official live data | official site research | UNKNOWN | Route to leasing, do not invent |
| CRM submission | Current GitHub Pages implementation prepares email; no CRM confirmed | repository documentation | FACT | Keep transparent prototype behavior |
| Official brand book | No reliable public brand guideline located in research | web research | UNKNOWN | Use partial-asset fallback, not a fabricated official guideline |

### Key unknowns to validate before production

- Current real-time vacancy and divisibility by floor.
- Commercial rental terms, service charge and incentive rules.
- CRM / lead-routing endpoint and SLA.
- Exact official digital typography specification.
- Whether a current official brand book exists internally.
- Rights/approval matrix for tenant logos and campaign photography.

## 03 — Business & KPI

### Primary business goal
Generate **qualified office leasing interest** and private viewing conversations for Capital Place.

### Secondary goals
- Strengthen Capital Place as a high-quality Hanoi business address.
- Demonstrate workplace, location and ESG value before asking for contact information.
- Support visitor, retail/F&B and occupier information without distracting the leasing journey.

| Business goal | Website responsibility | User action | KPI |
|---|---|---|---|
| Qualified leasing | Let users self-qualify space requirement | Find a Space → enquiry | qualified enquiries |
| Private viewing | Build enough confidence to justify visit | Book a Private Tour | viewing intent |
| ESG proof | Translate certifications/performance into occupier relevance | inspect sustainability proof | sustainability engagement |
| Location proof | Show commute/access/business context | explore location / visit | location-to-leasing progression |
| Trust | Keep public data clearly real vs representative | understand status/disclaimer | fewer misleading interactions |

Guardrails: do not increase conversion by pretending availability, pricing or backend confirmation is live.

## 04 — Brand Strategy & Brand Source Resolution

### Brand source status
**B — PARTIAL OFFICIAL BRAND ASSETS AVAILABLE**

Available evidence:
- official public website;
- official building photography;
- official Capital Place logo asset used in the project;
- official/verified public messaging around Grade A, sustainability, wellbeing and Thang Long-inspired architecture.

No public brand book was verified, so typography and semantic UI tokens remain proposed digital decisions rather than official brand rules.

### PROPOSED BRAND GUIDELINE — OFFICIAL-ASSET-DERIVED

| Token / signal | Value / direction | Status | Confidence |
|---|---|---|---|
| Logo | Capital Place vertical mark / wordmark | VERIFIED_FROM_OFFICIAL_ASSET | High |
| Logo artwork in repository | white SVG paths | VERIFIED_FROM_PROJECT_ASSET | High |
| Graphite | `#231F20` | INFERRED_FROM_OFFICIAL_ASSETS / preserved project system | Medium |
| Dark | `#171717` / `#252525` | PROPOSED_FOR_DIGITAL | High |
| Cream | `#F0EFE9` | INFERRED_FROM_OFFICIAL_ASSETS / preserved project system | Medium |
| White | `#FFFFFF` | PROPOSED_FOR_DIGITAL | High |
| Orange accent | `#F15F22` | INFERRED_FROM_OFFICIAL_ASSETS / preserved project system | Medium |
| Accessible orange text | `#A63C12` | PROPOSED_FOR_ACCESSIBILITY | High |
| Typeface | DM Sans + Manrope in current redesign | PROPOSED_FOR_DIGITAL / PRESERVE | Medium |

Important: the repository logo SVG is white-only; therefore orange is **not** claimed to be extracted from the logo.

### Brand attributes → design translation

| Attribute | Evidence | Translation |
|---|---|---|
| Landmark | architecture / twin towers | large-scale imagery, vertical rhythm, strong silhouette |
| International Grade A | official positioning/specs | precise typography, technical data, calm high-information layouts |
| Hanoi / local identity | Thang Long / dragon-scale architectural story | pattern/detail appears through architecture content, not fake ornamental motifs |
| Sustainable | dual LEED proof | measurable performance + occupier value |
| Business confidence | tenant/community messaging | restrained CTA hierarchy and trust-first content |
| Connected | location + amenities + community | journey links building, workday and city context |

## 05 — Audience & JTBD

| Audience | Trigger | Motivation | Barrier | Top task | Success |
|---|---|---|---|---|---|
| Corporate real-estate / admin decision maker | office relocation/expansion | fit, cost discussion, staff experience, timeline | insufficient commercial clarity | assess suitability and contact leasing | shortlist / viewing |
| Country manager / leadership | HQ / prestige decision | address, brand, talent, client impression | marketing-only content | understand why Capital Place is credible | confidence to progress |
| Tenant rep / broker | active requirement | floorplate, area, timing, technical info | incomplete availability | match requirement quickly | qualified leasing discussion |
| ESG / workplace stakeholder | sustainability requirement | certification, energy, wellbeing | claims without evidence | evaluate ESG/workplace value | internal approval evidence |
| Visitor / candidate / partner | scheduled visit | route, arrival, parking/access | uncertainty at arrival | plan visit | smooth arrival |

Core JTBD:

> When my company is considering a premium Hanoi office, I want to quickly understand whether Capital Place fits our location, workplace, ESG and space requirements so I can confidently arrange a viewing or leasing discussion.

## 06 — Top Tasks & Entry Intent

1. Check whether Capital Place can fit my team / area requirement.
2. Understand floorplate, capacity and core technical specifications.
3. Understand location, access and commute context.
4. Evaluate amenities and day-to-day employee experience.
5. Verify sustainability / LEED proof and occupier relevance.
6. Arrange a private tour / leasing discussion.
7. Plan an actual visit.

Entry contexts include organic search to Office/Location/Sustainability, direct brand visits, broker/referral deep links, social/campaign traffic and returning users going directly to availability.

## 07 — Existing Website Audit

### Preserve list

- Existing page URLs and current navigation habit unless evidence requires a migration.
- 93,000 sqm / 2 towers / 37 storeys factual foundation.
- Official Capital Place photography and architecture storytelling.
- Space Finder and representative-floor planning model.
- Availability state language that avoids pretending inventory is live.
- Floor detail / viewing / proposal / leasing intent flow.
- Visitor, resource, retail and occupier supporting routes.
- Mailto-only prototype truth until a real backend is connected.
- Current cinematic/editorial visual language.

### Improve

| Finding | Evidence | Impact | Decision |
|---|---|---|---|
| Shared UI layer accumulated many corrective overrides | `capital-uiux-v2.css` includes repeated final/mobile/recovery patches | harder to maintain visual coherence | preserve legacy, add a deliberate v3 semantic override layer |
| Rounded/floating controls can drift toward generic app/SaaS language | v2 uses 14px radius and floating mobile dock | weak building-domain distinctiveness | flatten to architectural planar geometry |
| Long deep pages need stronger orientation | Office and Home contain many decision sections | scanning cost | add unobtrusive building-directory on-page navigation on desktop |
| Current-page state is not consistently explicit | nav markup lacks `aria-current` | orientation/accessibility | apply route-aware active state |
| Mobile menu opens with focus but does not fully trap/restore focus | v2 JS behavior | keyboard friction | add focus loop, Escape restore and body scroll lock |
| Brand semantic accent drift | v2 root uses `#FF6938` while project foundation documents `#F15F22` | inconsistent system | align shared token with preserved brand-orange |

No high-value page is removed in v3.

## 08 — User Journey

| Stage | Question | Proof/content | CTA |
|---|---|---|---|
| Awareness | What is Capital Place? | twin towers, location, Grade A scale | Explore Office |
| Orientation | Is this relevant to my company? | 93,000 sqm, location, specs, ESG | Find a Space |
| Evaluation | Will it fit our workplace? | floorplate, capacity, technical features | Match requirement |
| Experience | Will employees/clients value it? | amenities, views, community, arrival | Explore Amenities / Visit |
| Trust | Is this credible and future-ready? | LEED + measurable performance + official facts | Sustainability |
| Decision | Is there a suitable opportunity? | reference availability / floor detail | Request Viewing |
| Conversion | Can I speak with leasing? | selected requirement context | Leasing Enquiry |
| Post-conversion | What happens next? | transparent contact channel / no fake confirmation | email/call follow-up |

## 09 — UX Principles

- **Recognition over recall:** persistent route state + on-page directory.
- **Progressive disclosure:** show building proof before enquiry form.
- **Hick's Law:** keep primary leasing actions limited and outcome-named.
- **Consistency:** same geometry, controls, focus and CTA language across routes.
- **Visibility of system status:** availability states and form prototype behavior remain explicit.
- **User control:** mobile menu Escape, focus restoration, no trapped scrolling.

## 10 — IA & Sitemap

Current expanded redesign IA remains appropriate for the leasing platform:

```text
Home
├── Location
├── Office
├── Sustainability
├── Amenities
├── Availability / Find a Space
├── Visit
├── Resources
├── Leasing Enquiry
├── Retail / F&B Leasing
├── Occupiers
├── FAQs
└── Space detail / utility states
```

Primary decision path remains:

`Home / deep landing → Office or Location → Availability → Space detail → Leasing / Private Tour`

## 11 — Page Experience Contracts

### Home
Role: orient, establish scale/identity, expose workplace proof, send users to decision pages.
Primary CTA: Find a Space.
Secondary: Private Tour after sufficient proof.

### Office
Role: decision page for workplace suitability.
Must answer: floorplate, capacity, specs, tower/floor logic, fit and next availability step.

### Availability
Role: requirement matching and truthful commercial handoff.
Must never imply real-time certainty without a connected source.

### Location
Role: business-access decision page, not a generic map page.

### Sustainability
Role: translate certification/performance into ESG + employee/workplace relevance.

### Amenities
Role: prove day-to-day experience through real spaces and services.

### Leasing
Role: low-friction qualified handoff; no competing sticky CTA over the form on mobile.

## 12 — Competitor Matrix

| Reference | Strength | Transferable principle | Do not copy |
|---|---|---|---|
| 22 Bishopsgate | people-led workplace ecosystem; leasing state is explicit | combine workplace experience, proof and honest leasing status | London brand tone / content density |
| The Henderson | iconic architecture + workplace + certifications + tenant community | architecture can lead while practical office information remains available | sculptural luxury styling |
| One Bangkok Workplace | location, smart workplace and sustainability tied to rental intent | connect infrastructure features to user/occupier benefit | mixed-use mega-project IA |
| Capital Place official site | authoritative building facts, architecture story, amenities and LEED | preserve content truth and official imagery | legacy form density / brochure-style sequencing |

## 13 — Reference Benchmark

Reference principles selected:

1. **22 Bishopsgate — workplace ecosystem:** amenities and people are decision proof, not decorative gallery content.
2. **The Henderson — iconic building + practical leasing:** architecture can remain aspirational while contact remains clear.
3. **One Bangkok — location + smart/ESG utility:** explain why infrastructure matters to occupiers.
4. **Capital Place official assets — local truth:** Thang Long architectural identity, real photos, floor plans and LEED claims remain the project source of truth.

## 14 — Design DNA

Dominant grammar: **architectural editorial + building directory + floor-plan precision**.

### Signature cues

1. Graphite / cream / white with orange used as a locator/decision marker, not a decorative wash.
2. Planar edges and thin rules rather than rounded SaaS shells.
3. Numbering / section index language inspired by building directories, elevations and leasing documents.
4. Large real architecture imagery with restrained editorial overlays.
5. Technical proof presented like a specification document: scan-friendly, aligned, factual.

### Real-world artifact transfer

Artifact: building directory / floor plan / leasing brochure.
Transfer layer: L1–L2 (cue + structural).
Use: numbering, rules, indexing, planar panels, section orientation.
Do not use: fake blueprint textures, pseudo-CAD interactions, skeuomorphic paper, decorative rulers everywhere.

## 15 — Design System Direction

- Radius: 0–4px default; circles only where functionally meaningful.
- Accent: `#F15F22`; deep accessible companion `#A63C12`.
- Focus: highly visible peach/orange outline.
- Controls: rectangular, 1px border, orange focus edge.
- CTA: one filled primary + restrained secondary.
- Navigation: dark architectural bar; current page visibly marked.
- On-page navigation: building-directory pattern on long desktop pages.
- Motion: short, purposeful; respect reduced motion.

## 16 — Responsive Strategy

Desktop:
- full cinematic layouts;
- page-directory rail on long pages where viewport width permits;
- persistent Find a Space route.

Tablet:
- remove side directory;
- use existing section hierarchy and hamburger menu.

Mobile:
- no compressed desktop side rail;
- full-screen menu with grid cue and clear route state;
- flat two-action dock on decision pages;
- hide dock on leasing/retail forms to avoid competing actions;
- respect safe area and 44px+ targets.

## 17 — Accessibility

Baseline: WCAG 2.2 AA intent.

Implemented / reinforced in v3:
- `aria-current` route state;
- focus-visible styling;
- keyboard tab navigation retained;
- mobile menu Tab loop, Escape close and focus restore;
- reduced-motion-aware scrolling;
- on-page directory is semantic navigation;
- form fields remain 16px+ on mobile.

Production still requires rendered screen-reader / browser verification.

## 18 — SEO

Preserve current URLs and page intent. Do not merge/remove current high-value pages in this visual/system pass.

Production SEO checklist:
- canonical per route;
- VI/EN hreflang only when real translated routes exist;
- unique title/H1/description per decision page;
- Place/Organization/Breadcrumb structured data where accurate;
- downloadable brochures/floor plans with descriptive link labels;
- redirects before any future slug migration.

## 19 — Technical & Performance

Current system: static HTML/CSS/JS on GitHub Pages.

Reality labels:
- building content: REAL where sourced from official public evidence;
- floor planning examples: REPRESENTATIVE / STATIC;
- availability: PARTIAL / representative unless leasing confirms live data;
- form submission: STATIC/MAILTO workflow, not CRM;
- language switch: prototype state, not full translated content.

v3 does not add framework dependencies, image libraries, 3D or heavy animation. The new directory uses native DOM + IntersectionObserver and is hidden below 1320px.

## 20 — Analytics

Useful intent events for a future connected analytics layer:
- `find_space_start`
- `space_match_view`
- `space_detail_view`
- `viewing_intent`
- `leasing_intent`
- `phone_click`
- `email_click`
- `brochure_open`

Do not send personal form values in analytics events.

## 21 — Priority Matrix

| Finding | User impact | Business impact | Effort | Priority | Action |
|---|---:|---:|---:|---:|---|
| Commercial truth / fake live data risk | High | High | Medium | P0 | preserve representative-status contract |
| Deep-page orientation | High | Medium | Low | P1 | building-directory navigation |
| Mobile menu keyboard behavior | Medium | Medium | Low | P1 | trap/restore focus + scroll lock |
| Generic rounded/app-like UI drift | Medium | Medium | Low | P1 | planar architecture grammar |
| Current route visibility | Medium | Medium | Low | P1 | `aria-current` + active marker |
| Token inconsistency | Medium | Medium | Low | P1 | align orange/cream/graphite semantics |
| Further motion novelty | Low | Low | Medium | P3 | do not add unless purpose emerges |

## 22 — Wireframe Brief

```text
PROJECT: Capital Place Hanoi — building / leasing experience
BUSINESS GOAL: generate qualified office leasing interest
PRIMARY CONVERSION: Find a Space → Leasing / Private Tour

PRIMARY AUDIENCE:
corporate real-estate/admin/leadership decision makers and tenant representatives

TOP TASKS:
check suitability; understand floorplate/specs; assess location; evaluate amenities/ESG;
find a space; request viewing

DESIGN PROBLEM:
preserve the strong cinematic redesign while making long pages easier to scan,
more domain-distinctive and more trustworthy as leasing decision tools

BRAND SOURCE STATUS: B — partial official assets
POSITIONING: international Grade A workplace / landmark Hanoi business address
BRAND ATTRIBUTES: landmark, precise, international, local identity, sustainable, connected

VISUAL DIRECTION:
architectural editorial + floor-plan precision + building-directory indexing

DESIGN SIGNATURE:
orange locator line; planar geometry; numbered directory; technical rules; real architecture photography

PRIMARY JOURNEY:
Discover → Evaluate building/location/workplace/ESG → Find a Space → Floor detail → Viewing/Leasing

HOMEPAGE ROLE:
orient and route; not a long generic corporate brochure

PROOF STRATEGY:
real building facts, plans, certifications, real amenities/location imagery, transparent prototype status

CTA STRATEGY:
Find a Space first; Private Tour/Leasing after proof; no premature repeated form

MOBILE PRIORITIES:
clear menu, flat sticky actions on decision pages, no dock over conversion forms,
large targets, correct focus and no horizontal overflow

MUST PRESERVE:
URLs, current facts, official imagery, leasing journey, representative-data disclaimers,
mailto-only prototype truth, cinematic editorial language

MUST FIX:
route orientation, long-page orientation, generic rounded controls,
mobile focus behavior, design-token drift

MUST NOT DO:
marketplace/dashboard UI; gold luxury theme; glass everywhere; invented pricing;
fake live availability; stock imagery replacing Capital Place; decorative blueprint skeuomorphism
```

## Quality Gate

v3 passes concept/code readiness when:
- business and conversion remain explicit;
- official facts remain unchanged;
- no live commercial data is fabricated;
- long pages have better orientation;
- the UI remains recognizably Capital Place without relying only on the logo;
- mobile menu and sticky actions remain usable;
- all new motion respects reduced-motion;
- production claims remain traceable to official evidence.
