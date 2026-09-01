# Capital Place Hero System V6.2

## Why this exists

V6 initially reused one generic subpage formula too often: `copy left + image right`. That created template monotony and failed the `visual-design-direction` requirement that repetition create consistency without making page families feel interchangeable.

The corrected rule is:

> Shared brand language, different opening composition for different decision jobs.

## Research basis

### First-party Capital Place

- Home / brand story: landmark architecture, Thang Long / dragon-scale identity, 93,000 sqm, 2 towers, 37 storeys.
- Location: 29 Lieu Giai as a business / diplomatic / transit address.
- Office: Grade A workplace, twin towers, large column-free planning, 1,847 sqm published floor reference.
- Sustainability: dual LEED certification plus measurable operating evidence.
- Amenities: The Link, The Nexus, hospitality, F&B, fitness and the workday ecosystem.
- Leasing: current commercial availability is a conversation with Leasing, not a fake live catalogue.

### Benchmark principles

- The Spiral: architecture and floor planning are treated as product objects, not decorative banners.
- One Vanderbilt: location, floors and amenities each open with a proposition specific to that page role rather than one repeated component.
- 22 Bishopsgate: leasing, workplace, ESG and directory pages expose the decision state or service directly.

Do not copy any one reference surface. Transfer the relationship between `page job → dominant visual object → first decision`.

## Hero matrix

| Page | User question on entry | Hero archetype | Dominant object | Signature |
|---|---|---|---|---|
| Overview | What is Capital Place and why does it matter? | Landmark cinematic | Twin towers | Monument scale + building facts |
| Location | Where is it and how does the address help me? | City canvas | Hanoi / building context | Full-bleed spatial image + vertical 29 Lieu Giai datum |
| Office | Can this building fit my workplace? | Leasing blueprint | Published floor plan | Drawing sheet + 1,847 sqm reference + interior inset |
| Sustainability | Is the ESG story credible? | Evidence / certification field | LEED credentials | Platinum / Gold blocks over building image |
| Amenities | What is the working day like? | Workday montage | The Link / The Nexus / experience | 3-part image montage + time rail |
| Availability | What space could fit and what is actually known? | Leasing planner | Floor plan / requirement | Drawing desk + explicit leasing-confirmed state |
| Leasing | How do I start a serious conversation? | Contact desk | Direct contact / lobby | Quiet dark conversion composition + phone/email datum |
| Visit | How do I arrive and orient myself? | Wayfinding / arrival | Arrival sequence | Address, drop-off and lobby orientation |
| Resources | What technical material can I use? | Technical library | Document index | Drawing/document catalogue rather than lifestyle image |
| FAQ | Can I resolve a practical question quickly? | Editorial index | Question taxonomy | Search / contents-first utility opening |

## Shared brand language

The heroes may differ in structure, but all keep:

- Capital graphite / warm paper / white;
- orange as wayfinding / action datum, not decorative fill;
- DM Sans and restrained large typography;
- square planar controls;
- verified Capital Place imagery and drawings;
- architectural lines, plans, directories and evidence objects;
- clear leasing progression.

## Rules

1. Never create a new page by copying `.cp6-page-hero` markup and changing only title/image.
2. The opening composition must be selected from the page's decision job.
3. Hero photography is not mandatory. For Office and Availability, floor-plan / planning artifacts may dominate.
4. Sustainability opens with proof, not green decoration.
5. Amenities opens with human/workday experience, not another tower portrait.
6. Leasing opens with action/contact clarity, not a marketing image.
7. Mobile keeps the page-specific dominant object and reading order; it must not collapse every archetype into the same image-under-copy stack without a retained signature.
8. Any new page family must document its hero archetype before implementation.

## QA contract

Core page heroes must have unique dominant media sources and dedicated page-role selectors. CI checks Location, Office, Sustainability, Amenities, Availability and Leasing for their corresponding visual signatures.
