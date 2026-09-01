# Capital Place Visual Regression Plan

Updated: 1 September 2026

## Purpose

Protect the current Capital Place visual direction during remediation and later AI-assisted changes. The approved signature remains architectural editorial + building-directory / floor-plan precision, with white, graphite and cream surfaces and restrained orange for action/locator roles.

## Preserve contract

- Existing public URLs and primary leasing journey.
- Official Capital Place imagery and verified first-party facts.
- Cinematic image-led storytelling on Home, Location, Office, Sustainability and Amenities.
- Space Finder / planning-reference journey without pretending to expose live inventory.
- Square/planar controls and restrained orange action role.
- English-first prototype truth; Vietnamese remains unavailable until real translated content exists.

## Representative coverage

| Route / state | 375 | 390 | 430 | 768 | 1024 | 1280 | 1440 | 1920 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Home | P0 | P0 | P0 | P0 | P0 | P0 | P0 | P1 |
| Office | P0 | P0 | P0 | P0 | P0 | P0 | P0 | P1 |
| Availability / filters / shortlist | P0 | P0 | P0 | P0 | P0 | P0 | P0 | P1 |
| Space detail | P0 | P0 | P0 | P0 | P0 | P0 | P0 | P1 |
| Leasing form / errors / prepared-email state | P0 | P0 | P0 | P0 | P0 | P0 | P0 | P1 |
| Location / Visit | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P2 |
| Sustainability / Amenities | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P2 |
| Resources / FAQ / Privacy / 404 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P2 |

## Visual checks

At every captured state verify:

- no horizontal overflow;
- H1/H2 wrapping remains intentional;
- nav/current-route state is readable;
- mobile menu fills viewport without trapping page scroll behind it;
- fixed mobile action dock does not cover content and respects safe area;
- action labels remain at least 12px in the final QA layer;
- footer links remain readable on white surfaces;
- focus indicator is clearly visible on both light and dark contexts;
- representative 1,240 m² scenario is not styled or worded as a published Capital Place reference;
- image crop preserves focal point and does not place important text over low-contrast areas;
- no card/button/radius drift away from the planar architectural grammar.

## Interaction states

Capture and review:

- desktop nav: default / current / hover / scrolled;
- mobile menu: closed / open / keyboard focus / Escape return;
- availability: area mode / headcount mode / no match / selected floor / saved / compare two;
- space detail: published reference / representative scenario / selected level on request / invalid reference;
- leasing: office / viewing / retail / validation error / prepared-email state;
- tabs and disclosure controls: default / selected / keyboard focus;
- reduced-motion mode for scroll and reveal behavior.

## Baseline policy

A screenshot becomes a baseline only after human visual review. Do not auto-accept screenshots just because CI/build passes. A changed screenshot must be classified as intended, unintended regression, system drift, or unstable capture before updating a baseline.

## Current verification limitation

GitHub Pages deployment and static QA can be verified through GitHub Actions. In the current assistant environment, `https://ngh1aa.github.io/Capital/` cannot be fetched reliably for browser-level screenshot inspection. Therefore rendered visual coverage remains PARTIAL until representative screenshots or a browser-capable environment are available. Do not claim visual-regression PASS from source checks alone.
