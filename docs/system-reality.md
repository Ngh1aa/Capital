# Capital Place — System Reality

Date checked: 2026-09-01
Project mode: `INTERACTIVE_PROTOTYPE`

This document prevents a polished static UI from being reported as a connected leasing system.

## Capability matrix

| Capability | Reality | Evidence | Production implication |
|---|---|---|---|
| Building facts | STATIC, FIRST-PARTY VERIFIED | `assets/capital-data.js` + capitalplace.com.vn/office | Safe to present with source/date; refresh when first-party facts change |
| Sustainability facts | STATIC, FIRST-PARTY VERIFIED | capitalplace.com.vn/sustainability-and-community | Keep qualifiers attached to figures |
| Official imagery | STATIC ASSETS | repository `assets/images/official/` + first-party site basis | Do not replace with stock imagery presented as the property |
| 1,847 m² floor planning reference | STATIC, FIRST-PARTY VERIFIED | current official Office page | Can be used as a published planning reference, not live vacancy |
| 1,240 m² planning scenario | STATIC, REPRESENTATIVE PROTOTYPE | local data model; no current first-party evidence recorded in this review | Must remain labelled representative; do not present as an official current floor plate |
| Availability / floor status | SIMULATED / LEASING-CONFIRMATION | local `CapitalData.spaces`; no verified real-time inventory feed | Current vacancy, pricing, divisibility and terms must be confirmed by Leasing |
| Space Finder | STATIC LOCAL DECISION SUPPORT | local JS + planning assumptions | Helpful for orientation only; it is not a commercial offer or workplace test fit |
| Space detail | STATIC / REPRESENTATIVE | local data and illustrative plan | No construction-grade or real-time claim |
| Leasing form | SIMULATED HANDOFF | validates locally and prepares `mailto:` | No server/CRM submission; UI must never imply receipt by Leasing |
| Viewing request | SIMULATED HANDOFF | same mailto flow | Preferred time is a request only; Leasing confirms separately |
| EN content | STATIC / IMPLEMENTED | current HTML | Current document language remains `en` |
| VI switch | NOT IMPLEMENTED | no translated route/content bundle in project | VI control must not change document language or imply translation exists |
| Analytics | PARTIAL | local `dataLayer` and custom events; no collector verified in scope | Event delivery/reporting is UNKNOWN; exclude PII from event payloads |
| Privacy notice | STATIC PROTOTYPE + FIRST-PARTY LINK | local privacy page + Twin-Peaks first-party 2026 notice | Keep the two notices distinct; do not imply legal compliance from prototype copy |
| GitHub Pages deployment | REAL STATIC HOSTING | repository deployment target | A source commit is not visual/browser proof of the deployed result |

## Dynamic / data contracts

### Availability

Source: `assets/capital-data.js`

Required public behavior:
- show planning/reference status, not live commercial certainty;
- no published price unless a verified first-party source is added;
- current floor, area, divisibility, timing and terms route to Leasing confirmation;
- empty/no-match states provide a leasing handoff instead of fake results.

Freshness owner: project maintainer + Capital Place first-party source review.

### Leasing enquiry

Current source: browser form + `mailto:` construction.

Required states:
- validation error → field remains populated and focus moves to first invalid field;
- prepared state → explicitly says nothing was transmitted;
- email action → user chooses whether to send in their mail client;
- backend success state → NOT ALLOWED until a real endpoint response is verified.

Production dependency: CRM/server endpoint, consent/privacy review, retry/error contract and target-environment verification.

### Language

Current source: English static HTML only.

Required behavior:
- `<html lang="en">` remains truthful;
- VI is unavailable until real Vietnamese content/routes exist;
- future VI implementation requires localized metadata, navigation, forms, errors and canonical/hreflang strategy.

## Production gaps

| Gap | Current reality | Required for production | Severity |
|---|---|---|---|
| Live inventory | SIMULATED / on request | authoritative source, freshness contract, failure/stale states | P1 if marketed as live |
| CRM lead capture | mailto only | verified endpoint + success/error/retry + consent/data handling | P1 for real lead operations |
| Vietnamese locale | not implemented | translated content + route architecture + QA | P1 if language toggle is promised |
| Analytics collector | unverified | actual measurement stack + event QA + privacy review | P2 |
| Cross-browser / AT verification | unverified in connector environment | Chromium/WebKit/Firefox + keyboard/AT checks | P1 before production claim |
| Field performance data | unavailable | RUM/CrUX or equivalent if production KPI requires it | P2 |

## Integrity rules

- `reference` ≠ `available`.
- `request prepared` ≠ `request sent`.
- `dataLayer.push()` ≠ analytics received.
- language button ≠ implemented locale.
- build/static QA pass ≠ visual, browser or WCAG conformance proof.
