"""Build-time leasing UX upgrade for the static Capital Place prototype.

The original page generator remains the source for the established visual
direction. This module adds the P0/P1 information architecture and interaction
layer without replacing the existing typography, palette, imagery or layout
language.
"""

from __future__ import annotations

import re
from typing import Callable, Dict


VERSION = "ux-20260824-1"


def finder_markup() -> str:
    return """<div class="finder-shell" data-space-finder>
  <div class="finder-progress" aria-label="Space finder steps"><span class="active">1 · Requirement</span><span>2 · Timeline</span><span>3 · Results</span></div>
  <p class="ux-kicker">How would you like to search?</p>
  <div class="finder-mode" role="group" aria-label="Choose requirement method">
    <button type="button" class="finder-choice active" data-finder-mode="area" aria-pressed="true">I know my area</button>
    <button type="button" class="finder-choice" data-finder-mode="headcount" aria-pressed="false">I know my team size</button>
  </div>
  <form novalidate>
    <div class="finder-grid">
      <div class="ux-field" data-finder-area-field><label for="finder-required-area">Required Area</label><select id="finder-required-area" name="requiredArea"><option value="lt500">Under 500 m²</option><option value="500-1000">500–1,000 m²</option><option value="1000-2000" selected>1,000–2,000 m²</option><option value="2000plus">2,000+ m²</option><option value="unsure">Not sure</option></select></div>
      <div class="ux-field" data-finder-headcount-field hidden><label for="finder-team-size">Team Size</label><input id="finder-team-size" name="teamSize" type="number" min="1" max="5000" inputmode="numeric" placeholder="e.g. 120" /></div>
      <div class="ux-field"><label for="finder-timeline">Target Move-in</label><select id="finder-timeline" name="timeline"><option value="planning">Planning ahead</option><option value="immediate">Immediately</option><option value="0-3">0–3 months</option><option value="3-6">3–6 months</option><option value="6-12">6–12 months</option><option value="12plus">12+ months</option></select></div>
      <div class="ux-field"><label for="finder-tower">Preferred Tower</label><select id="finder-tower" name="tower"><option value="all">Either tower</option><option value="1">Tower 01</option><option value="2">Tower 02</option></select></div>
    </div>
    <div class="finder-estimate" data-finder-estimate hidden></div>
    <p class="finder-assumption">Availability and capacity are indicative only. Final requirements, timing and divisibility are confirmed by the leasing and workplace teams.</p>
    <div class="ux-actions"><button type="submit" class="btn-gold">Find Matching Spaces <span aria-hidden="true">→</span></button><a class="btn-outline-gold" href="leasing.html?intent=office">Talk to Leasing</a></div>
  </form>
  <div class="finder-results" data-finder-results hidden aria-live="polite"></div>
</div>"""


def page_header(kicker: str, title: str, copy: str, image: str, image_alt: str, actions: str = "") -> str:
    return f"""<div class="page-header" style="--hero-position:center 48%;background-image:url({image});background-position:center 48%">
  <img class="page-header-media" src="{image}" alt="{image_alt}" fetchpriority="high" />
  <div class="container"><p class="page-header-eyebrow">{kicker}</p><h1>{title}</h1><p>{copy}</p>{actions}</div>
</div>"""


def availability_page() -> str:
    hero = page_header(
        "Office Availability",
        "Find a space<br><em>for what’s next</em>",
        "Explore indicative opportunities across both towers, evaluate fit and continue directly to a viewing or proposal request.",
        "assets/images/feedback/office-page-header.jpg",
        "Capital Place twin office towers in Hanoi",
        '<div class="page-header-actions ux-actions"><a class="btn-gold" href="#space-finder">Find a Space <span aria-hidden="true">→</span></a><a class="btn-outline-gold" href="#current-opportunities">View Availability</a></div>',
    )
    return hero + f"""
<section class="ux-section alt" id="space-finder" aria-labelledby="space-finder-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Space Finder</p><h2 id="space-finder-title" class="section-title">Start with your<br><em>requirement</em></h2></div><p class="ux-section-copy">Search by required area or team size, then refine by move-in timing and preferred tower.</p></div>{finder_markup()}</div></section>
<section class="ux-section" id="current-opportunities" aria-labelledby="availability-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Current Opportunities</p><h2 id="availability-title" class="section-title">Explore the<br><em>building</em></h2></div><div><p class="ux-section-copy">Availability is represented as a decision-support layer rather than a live commercial schedule.</p><div class="ux-notice">Indicative opportunities for website demonstration. Current availability, areas and commercial terms must be confirmed by the Capital Place leasing team.</div></div></div>
  <div class="availability-toolbar" aria-label="Filter office opportunities">
    <div class="ux-field"><label for="availability-area">Required Area</label><select id="availability-area" data-filter-area><option value="all">All areas</option><option value="lt500">Under 500 m²</option><option value="500-1000">500–1,000 m²</option><option value="1000-2000">1,000–2,000 m²</option><option value="2000plus">2,000+ m²</option></select></div>
    <div class="ux-field"><label for="availability-tower">Tower</label><select id="availability-tower" data-filter-tower><option value="all">Both towers</option><option value="1">Tower 01</option><option value="2">Tower 02</option></select></div>
    <div class="ux-field"><label for="availability-timeline">Move-in</label><select id="availability-timeline" data-filter-timeline><option value="all">Any timing</option><option value="immediate">Immediately</option><option value="0-3">0–3 months</option><option value="3-6">3–6 months</option><option value="6-12">6–12 months</option><option value="12plus">12+ months</option></select></div>
    <div class="ux-field"><label for="availability-status">Status</label><select id="availability-status" data-filter-status><option value="all">All statuses</option><option value="available">Available</option><option value="available-soon">Available Soon</option><option value="under-offer">Under Offer</option><option value="future-availability">Future Availability</option><option value="on-request">On Request</option><option value="leased">Leased</option></select></div>
  </div>
  <p class="availability-count" data-availability-count aria-live="polite"></p><div data-availability-list></div>
</div></section>
<section class="ux-section graphite"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Evaluate Further</p><h2 class="section-title">From opportunity<br><em>to decision</em></h2></div><p class="ux-section-copy">Review the stacking plan, illustrative floor plates, building specifications and sustainability credentials before requesting a site visit.</p></div><div class="gateway-grid"><a class="gateway-link" href="office.html#floor-explorer"><div><h3>Floor Plans</h3><p>Review typical floor plates and early capacity assumptions.</p></div><span>Explore Plans →</span></a><a class="gateway-link" href="resources.html"><div><h3>Leasing Resources</h3><p>Building facts, specifications, sustainability and location resources.</p></div><span>View Resources →</span></a><a class="gateway-link" href="leasing.html?intent=viewing"><div><h3>Request a Viewing</h3><p>Share a preferred date and time for leasing-team confirmation.</p></div><span>Request Viewing →</span></a></div></div></section>"""


def space_page() -> str:
    return """<div data-space-page>
  <div class="space-detail-valid" data-space-valid hidden>
    <div class="page-header space-detail-header" style="--hero-position:center 55%;background-image:url(assets/images/feedback/office-page-header.jpg);background-position:center 55%"><img class="page-header-media" src="assets/images/feedback/office-page-header.jpg" alt="Capital Place office towers" fetchpriority="high"/><div class="container"><p class="page-header-eyebrow">Office Opportunity</p><h1 data-space-field="tower-floor">Tower · Floor</h1><p class="space-detail-area" data-space-field="area">Area</p><span class="space-detail-status" data-space-field="status">Status</span></div></div>
    <section class="ux-section" aria-labelledby="space-evaluate-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Evaluate the Space</p><h2 id="space-evaluate-title" class="section-title">A clearer path<br><em>to fit</em></h2></div><div><p class="ux-section-copy">Use the public information below for early evaluation. Detailed drawings, technical packages and final commercial terms are provided through leasing.</p><div class="ux-notice">Illustrative floor plan and capacity only. This page does not represent a binding offer or live commercial schedule.</div></div></div><div class="space-detail-main"><div><div class="space-plan" data-space-plan></div><p class="space-plan-caption">Illustrative public floor plan · detailed plan available through the leasing team</p><div class="capacity-grid"><div class="capacity-item"><span class="capacity-value" data-space-field="capacity">—</span><span class="capacity-label">Indicative people at 10 m²/person</span></div><div class="capacity-item"><span class="capacity-value" data-space-field="capacity-range">—</span><span class="capacity-label">Indicative planning range</span></div></div></div><aside class="space-sticky-card"><h2 data-space-field="tower-floor">Tower · Floor</h2><dl class="space-facts"><div class="space-fact"><dt>Area</dt><dd data-space-field="area">—</dd></div><div class="space-fact"><dt>Availability</dt><dd data-space-field="status">—</dd></div><div class="space-fact"><dt>Timing</dt><dd data-space-field="timing">—</dd></div><div class="space-fact"><dt>Fit-out</dt><dd data-space-field="fitout">—</dd></div><div class="space-fact"><dt>Divisibility</dt><dd data-space-field="divisibility">—</dd></div><div class="space-fact"><dt>Orientation</dt><dd data-space-field="view">—</dd></div></dl><div class="ux-actions"><a class="btn-gold" data-space-action="viewing" href="leasing.html?intent=viewing">Request a Viewing</a><a class="btn-outline-gold" data-space-action="proposal" href="leasing.html?intent=proposal">Request Proposal</a><a class="text-link" data-space-action="plan" href="leasing.html?intent=technical-package">Request Detailed Plan →</a></div></aside></div></div></section>
    <section class="ux-section alt"><div class="container"><div class="gateway-grid"><a class="gateway-link" href="office.html#office-specifications"><div><h3>Building Specifications</h3><p>Space, access, comfort and resilience specifications.</p></div><span>View Specs →</span></a><a class="gateway-link" href="location.html"><div><h3>Location</h3><p>Business access, employee journey and client experience.</p></div><span>Explore Location →</span></a><a class="gateway-link" href="sustainability.html"><div><h3>Sustainability</h3><p>LEED credentials and what they mean for occupiers.</p></div><span>Explore ESG →</span></a></div></div></section>
  </div>
  <section class="ux-section space-detail-invalid" data-space-invalid hidden><div class="container"><div class="ux-empty"><p class="eyebrow">Opportunity Update</p><h3>This opportunity is no longer available.</h3><p>The floor reference may be outdated or unavailable. Continue to current indicative opportunities or speak with the leasing team about a future requirement.</p><div class="ux-actions"><a class="btn-gold" href="availability.html">View Current Availability</a><a class="btn-outline-gold" href="leasing.html?intent=future-availability">Register Interest</a></div></div></div></section>
</div>"""


def leasing_page() -> str:
    hero = page_header(
        "Leasing",
        "The right next step,<br><em>with context</em>",
        "Tell the Capital Place leasing team what you need, when you need it and which opportunity you have evaluated.",
        "assets/images/feedback/office-page-header.jpg",
        "Capital Place office towers",
    )
    return hero + """
<section class="ux-section" aria-labelledby="enquiry-routing-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Choose Your Enquiry</p><h2 id="enquiry-routing-title" class="section-title">Route your request<br><em>to the right team</em></h2></div><p class="ux-section-copy">Office, viewing and retail enquiries capture different decision criteria. Your selected space remains attached to the request.</p></div>
  <div class="intent-grid" role="group" aria-label="Select enquiry type"><button type="button" class="intent-option active" data-intent="office"><strong>Office Leasing</strong><span>Area, move-in timing and business requirement.</span></button><button type="button" class="intent-option" data-intent="viewing"><strong>Request a Viewing</strong><span>Preferred date and time, subject to confirmation.</span></button><button type="button" class="intent-option" data-intent="retail"><strong>Retail / F&B</strong><span>Brand, category, area and target opening.</span></button></div>
  <div class="leasing-layout"><aside><p class="eyebrow">Capital Place Leasing</p><h2 class="section-title" data-form-title>Office Leasing Enquiry</h2><div class="leasing-context" data-leasing-context hidden><p class="leasing-context-title">Interested Space</p><p class="leasing-context-value" data-leasing-context-value></p></div><div class="leasing-contact-list"><a data-contact="phone" href="tel:18009289"><span>Hotline</span><span>1800 9289</span></a><a data-contact="email" href="mailto:leasing@capitalplace.vn"><span>Email</span><span>leasing@capitalplace.vn</span></a></div><p class="finder-assumption">This static portfolio prototype prepares an enquiry but does not transmit personal data to a CRM. Use the generated email action to send it to leasing.</p></aside>
    <div><form class="leasing-form" data-leasing-form novalidate><input type="hidden" name="intent" value="office"/><input type="hidden" name="spaceContext" value=""/>
      <div class="leasing-form-grid two"><div class="ux-field"><label for="lead-name">Full Name</label><input id="lead-name" name="fullName" type="text" autocomplete="name" required aria-describedby="lead-name-error"/><span class="ux-error" id="lead-name-error"></span></div><div class="ux-field"><label for="lead-company">Company</label><input id="lead-company" name="company" type="text" autocomplete="organization" required aria-describedby="lead-company-error"/><span class="ux-error" id="lead-company-error"></span></div></div>
      <div class="leasing-form-grid two"><div class="ux-field"><label for="lead-email">Work Email</label><input id="lead-email" name="workEmail" type="email" autocomplete="email" required aria-describedby="lead-email-error"/><span class="ux-error" id="lead-email-error"></span></div><div class="ux-field"><label for="lead-phone">Phone</label><input id="lead-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="lead-phone-error"/><span class="ux-error" id="lead-phone-error"></span></div></div>
      <div class="leasing-form-grid two" data-conditional="office availability proposal viewing future-availability technical-package"><div class="ux-field"><label for="lead-area">Required Area</label><select id="lead-area" name="requiredArea" data-required-when-visible aria-describedby="lead-area-error"><option value="">Select an area</option><option>Under 500 m²</option><option>500–1,000 m²</option><option>1,000–2,000 m²</option><option>2,000+ m²</option><option>Not sure</option></select><span class="ux-error" id="lead-area-error"></span></div><div class="ux-field"><label for="lead-timeline">Target Move-in</label><select id="lead-timeline" name="targetMoveIn" data-required-when-visible aria-describedby="lead-timeline-error"><option value="">Select a timeline</option><option>Immediately</option><option>0–3 months</option><option>3–6 months</option><option>6–12 months</option><option>12+ months</option><option>Planning ahead</option></select><span class="ux-error" id="lead-timeline-error"></span></div></div>
      <div class="leasing-form-grid two conditional-fields" data-conditional="viewing" hidden><div class="ux-field"><label for="viewing-date">Preferred Date</label><input id="viewing-date" name="preferredDate" type="date" data-required-when-visible aria-describedby="viewing-date-error"/><span class="ux-error" id="viewing-date-error"></span></div><div class="ux-field"><label for="viewing-time">Preferred Time</label><select id="viewing-time" name="preferredTime" data-required-when-visible aria-describedby="viewing-time-error"><option value="">Select a time</option><option>Morning</option><option>Afternoon</option></select><span class="ux-error" id="viewing-time-error"></span></div></div>
      <div class="conditional-fields" data-conditional="retail" hidden><div class="leasing-form-grid two"><div class="ux-field"><label for="retail-brand">Brand</label><input id="retail-brand" name="brand" type="text" data-required-when-visible aria-describedby="retail-brand-error"/><span class="ux-error" id="retail-brand-error"></span></div><div class="ux-field"><label for="retail-category">Category</label><select id="retail-category" name="category" data-required-when-visible aria-describedby="retail-category-error"><option value="">Select category</option><option>Restaurant / F&B</option><option>Café</option><option>Convenience Retail</option><option>Wellness</option><option>Services</option><option>Other</option></select><span class="ux-error" id="retail-category-error"></span></div></div><div class="leasing-form-grid two"><div class="ux-field"><label for="retail-area">Area Requirement <span class="form-optional">Optional</span></label><input id="retail-area" name="retailArea" type="text" placeholder="e.g. 80–120 m²"/></div><div class="ux-field"><label for="retail-opening">Target Opening <span class="form-optional">Optional</span></label><input id="retail-opening" name="targetOpening" type="text" placeholder="e.g. Q2 2027"/></div></div></div>
      <div class="ux-field"><label for="lead-message">Message <span class="form-optional">Optional</span></label><textarea id="lead-message" name="message" rows="4" placeholder="Workplace priorities, access requirements or questions for the leasing team"></textarea><span class="ux-error" id="lead-message-error"></span></div>
      <label class="form-consent" for="privacy-consent"><input id="privacy-consent" name="privacyConsent" type="checkbox" value="confirmed" required aria-describedby="privacy-consent-error"/><span>I have reviewed the <a href="privacy.html" target="_blank">prototype privacy notice</a> and understand this demo prepares an email rather than transmitting form data automatically.<span class="ux-error" id="privacy-consent-error"></span></span></label>
      <div class="form-submit-row"><button class="btn-gold" type="submit">Prepare Enquiry <span aria-hidden="true">→</span></button><p class="form-submit-note">A preferred viewing time is a request only. The leasing team must confirm the appointment.</p></div>
    </form><div class="form-success" data-form-success hidden tabindex="-1"><p class="eyebrow">Request Prepared</p><h2>Your enquiry is ready.</h2><p>This prototype has not transmitted your information. Use the email action below to send the prepared request to Capital Place leasing.</p><div class="ux-actions"><a class="btn-gold email-fallback" data-email-fallback href="mailto:leasing@capitalplace.vn">Send via Email</a><a class="btn-outline-gold" href="resources.html">Explore Leasing Resources</a><a class="text-link" href="location.html">Explore Location →</a></div></div></div>
  </div>
</div></section>"""


def visit_page() -> str:
    hero = page_header(
        "Visit Capital Place",
        "Arrive with<br><em>clarity</em>",
        "Plan the journey from the city to drop-off, reception and your destination inside Capital Place.",
        "assets/images/feedback/fb4-arrival.jpg",
        "Arrival experience at Capital Place",
        '<div class="page-header-actions ux-actions"><a class="btn-gold" href="#visitor-guide">Plan Your Visit <span aria-hidden="true">→</span></a><a class="btn-outline-gold" href="https://www.google.com/maps/search/?api=1&amp;query=Capital+Place+29+Lieu+Giai+Hanoi" target="_blank" rel="noopener">Get Directions</a></div>',
    )
    return hero + """
<section class="ux-section" id="visitor-guide" aria-labelledby="visitor-guide-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Visitor Journey</p><h2 id="visitor-guide-title" class="section-title">From arrival<br><em>to destination</em></h2></div><p class="ux-section-copy">Building access arrangements can vary by host and event. Confirm your visit with the occupier or leasing contact before arrival.</p></div><div class="visit-grid"><article class="visit-item"><span class="visit-number">01</span><h3>Address</h3><p>29 Lieu Giai, Ngoc Ha, Ba Dinh, Hanoi, Vietnam.</p></article><article class="visit-item"><span class="visit-number">02</span><h3>Drop-off</h3><p>Use the main Capital Place arrival at 29 Lieu Giai. Follow on-site signage and security direction.</p></article><article class="visit-item"><span class="visit-number">03</span><h3>Parking</h3><p>Parking access and availability should be confirmed with your host or building contact before the visit.</p></article><article class="visit-item"><span class="visit-number">04</span><h3>Reception</h3><p>Have your host company, tower and meeting contact ready for reception and security registration.</p></article><article class="visit-item"><span class="visit-number">05</span><h3>Building Access</h3><p>Access to office and tenant-only amenity areas may require host approval or a visitor pass.</p></article><article class="visit-item"><span class="visit-number">06</span><h3>Accessibility</h3><p>Contact your host in advance for step-free arrival or any specific access support.</p></article></div></div></section>
<section class="ux-section alt"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">29 Lieu Giai</p><h2 class="section-title">See the<br><em>address</em></h2></div><p class="ux-section-copy">Open the map only when needed; the address and journey guidance remain available as readable content.</p></div><div class="visit-map"><iframe title="Capital Place at 29 Lieu Giai, Hanoi" src="https://www.google.com/maps?q=Capital+Place+29+Lieu+Giai+Hanoi&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div><div class="ux-actions"><a class="btn-gold" href="https://www.google.com/maps/search/?api=1&amp;query=Capital+Place+29+Lieu+Giai+Hanoi" target="_blank" rel="noopener">Open in Maps</a><a class="btn-outline-gold" href="location.html#transport">Transport Options</a></div></div></section>
<section class="ux-section graphite"><div class="container"><div class="gateway-grid"><a class="gateway-link" href="amenities.html#amenity-directory"><div><h3>Amenity Directory</h3><p>Find dining, meeting, workspace and wellness destinations.</p></div><span>Explore Amenities →</span></a><a class="gateway-link" href="occupiers.html"><div><h3>For Occupiers</h3><p>Public gateway to amenities, notices and building support routes.</p></div><span>Occupier Gateway →</span></a><a class="gateway-link" href="leasing.html?intent=viewing"><div><h3>Leasing Visit</h3><p>Request a preferred date and time for a space viewing.</p></div><span>Request Viewing →</span></a></div></div></section>"""


def resources_page() -> str:
    hero = page_header(
        "Leasing Resources",
        "Evaluate with<br><em>the right information</em>",
        "Public building, floor, specification, sustainability and location resources for occupiers, executives and brokers.",
        "assets/images/feedback/office-page-header.jpg",
        "Capital Place building architecture",
        '<div class="page-header-actions ux-actions"><a class="btn-gold" href="#resource-library">View Resources <span aria-hidden="true">→</span></a></div>',
    )
    return hero + """
<section class="ux-section" id="resource-library" aria-labelledby="resource-library-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Resource Library</p><h2 id="resource-library-title" class="section-title">Public first.<br><em>Detailed on request.</em></h2></div><div><p class="ux-section-copy">Core facts and illustrative plans remain visible. CAD, technical packages and fit-out guidelines are routed through leasing when qualification is appropriate.</p><div class="ux-notice">Resources on this portfolio site are web-based previews. Final leasing documents and drawings must be issued by the Capital Place leasing team.</div></div></div><div class="resource-list" data-resource-list></div></div></section>
<section class="ux-section alt"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Detailed Package</p><h2 class="section-title">Need more<br><em>technical depth?</em></h2></div><p class="ux-section-copy">Request detailed drawings, fit-out guidance or a tailored proposal with the space and requirement already attached.</p></div><div class="ux-actions"><a class="btn-gold" href="leasing.html?intent=technical-package">Request Technical Package</a><a class="btn-outline-gold" href="availability.html">View Availability</a></div></div></section>"""


def retail_page() -> str:
    hero = page_header(
        "The Link · Retail / F&B",
        "A place for brands<br><em>to belong</em>",
        "Explore the business ecosystem and start a dedicated retail or F&B leasing conversation at Capital Place.",
        "assets/images/feedback/fb4-the-link.jpg",
        "Retail and dining experience at Capital Place",
        '<div class="page-header-actions ux-actions"><a class="btn-gold" href="#retail-opportunity">Explore Retail <span aria-hidden="true">→</span></a><a class="btn-outline-gold" href="leasing.html?intent=retail">Retail Enquiry</a></div>',
    )
    return hero + """
<section class="ux-section" id="retail-opportunity" aria-labelledby="retail-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Retail Leasing</p><h2 id="retail-title" class="section-title">Built around<br><em>a working community</em></h2></div><p class="ux-section-copy">Capital Place brings together office occupiers, visitors and a premium amenity environment. Retail proposals are evaluated by brand, category, area and operating requirement.</p></div><div class="gateway-grid"><div class="gateway-link"><div><h3>F&B & Café</h3><p>Restaurant, café and food concepts assessed against unit and operational requirements.</p></div><span>Category</span></div><div class="gateway-link"><div><h3>Convenience & Services</h3><p>Everyday retail and professional services supporting the building community.</p></div><span>Category</span></div><div class="gateway-link"><div><h3>Wellness & Lifestyle</h3><p>Concepts that complement workplace wellbeing and amenity experience.</p></div><span>Category</span></div></div></div></section>
<section class="ux-section alt"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Retail Opportunities</p><h2 class="section-title">Available<br><em>on request</em></h2></div><div><p class="ux-section-copy">No retail inventory is invented or presented as live on this prototype. Share your brand profile and requirement for current unit information.</p><div class="ux-notice">Unit area, frontage, exhaust, access and availability are confirmed individually by the retail leasing team.</div></div></div><div class="ux-actions"><a class="btn-gold" href="leasing.html?intent=retail">Start Retail Enquiry</a><a class="btn-outline-gold" href="amenities.html#the-link">Explore The Link</a></div></div></section>"""


def occupiers_page() -> str:
    hero = page_header(
        "For Occupiers",
        "The building,<br><em>beyond the lease</em>",
        "A public gateway to amenities, arrival guidance and the appropriate route for building support.",
        "assets/images/feedback/fb4-business.jpg",
        "Capital Place workplace environment",
    )
    return hero + """
<section class="ux-section" aria-labelledby="occupier-gateway-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Occupier Gateway</p><h2 id="occupier-gateway-title" class="section-title">Find the right<br><em>building resource</em></h2></div><p class="ux-section-copy">Secure tenant services remain in the building’s approved portal or operational channels; the public website only provides safe entry points.</p></div><div class="gateway-grid"><a class="gateway-link" href="amenities.html#amenity-directory"><div><h3>Amenities</h3><p>Dining, workspace, meeting, lounge, wellness and family amenities.</p></div><span>Open Directory →</span></a><a class="gateway-link" href="visit.html"><div><h3>Visitor Guidance</h3><p>Address, reception, drop-off and access information for guests.</p></div><span>Plan a Visit →</span></a><a class="gateway-link" href="mailto:leasing@capitalplace.vn?subject=Capital%20Place%20building%20support%20routing"><div><h3>Building Support</h3><p>Use your registered occupier channel first; public email can help route an enquiry.</p></div><span>Request Routing →</span></a></div><div class="ux-notice" style="margin-top:2rem">Emergency procedures, secure notices and service requests are not reproduced on the public site. Occupiers should follow official building-management channels.</div></div></section>"""


def privacy_page() -> str:
    return """<section class="ux-section" style="padding-top:10rem;min-height:72vh"><div class="container"><p class="eyebrow">Prototype Privacy Notice</p><h1 class="section-title" style="margin-top:1rem">Your information<br><em>stays in your browser</em></h1><div class="ux-section-copy" style="margin-top:2rem"><p>This Capital Place redesign is a static portfolio prototype. Form entries are not sent to a server, CRM or analytics platform by the website.</p><p style="margin-top:1rem">When you submit an enquiry, the site prepares a mailto link. Your email application controls whether the message is sent. Analytics events contain only interaction context such as intent or selected space ID and exclude names, email addresses, phone numbers, companies and messages.</p><p style="margin-top:1rem">Do not enter confidential commercial information into a public prototype.</p></div><div class="ux-actions"><a class="btn-gold" href="leasing.html">Return to Enquiry</a><a class="btn-outline-gold" href="index.html">Explore Capital Place</a></div></div></section>"""


def not_found_page() -> str:
    return """<section class="ux-section" style="padding-top:10rem;min-height:74vh"><div class="container"><p class="eyebrow">404 · Page Not Found</p><h1 class="section-title" style="margin-top:1rem">The page you’re looking for<br><em>isn’t here.</em></h1><p class="ux-section-copy" style="margin-top:1.5rem">Continue to Capital Place, current indicative availability or the leasing team.</p><div class="ux-actions"><a class="btn-gold" href="index.html">Explore Capital Place</a><a class="btn-outline-gold" href="availability.html">View Office</a><a class="text-link" href="leasing.html">Contact Leasing →</a></div></div></section>"""


def replace_required(source: str, old: str, new: str, label: str) -> str:
    if old not in source:
        raise ValueError(f"Upgrade marker not found: {label}")
    return source.replace(old, new, 1)


def add_common_layer(html: str) -> str:
    html = html.replace(
        "</head>",
        f'<meta name="theme-color" content="#111111" />\n  <meta property="og:site_name" content="Capital Place Hanoi" />\n  <link rel="stylesheet" href="assets/capital-upgrade.css?v={VERSION}" />\n</head>',
        1,
    )
    html = html.replace("</nav>", '</nav>\n<main id="main-content">', 1)
    html = html.replace("<footer>", "</main>\n<footer>", 1)
    html = html.replace(
        "</body>",
        f'<script src="assets/capital-data.js?v={VERSION}"></script>\n<script src="assets/capital-upgrade.js?v={VERSION}"></script>\n</body>',
        1,
    )
    return html


def update_common_content(html: str) -> str:
    html = html.replace('href="amenities.html#leasing" class="btn-enquire">Enquire', 'href="availability.html" class="btn-enquire">Find a Space')
    html = html.replace('<a href="amenities.html" onclick="closeMob()">Amenities</a>\n    <a href="amenities.html#leasing" class="mob-enq"', '<a href="amenities.html" onclick="closeMob()">Amenities</a>\n    <a href="availability.html" onclick="closeMob()">Availability</a>\n    <a href="leasing.html" class="mob-enq"')
    html = html.replace('href="amenities.html#leasing"', 'href="leasing.html?intent=office"')
    html = html.replace('leasing@capitalplace.com.vn', 'leasing@capitalplace.vn')
    html = html.replace('93,700 SQM', '93,000 SQM')
    html = html.replace('93,700', '93,000')
    html = html.replace('41 Storeys', '37 Storeys Per Tower')
    html = html.replace('data-target="41">41</span><span class="stat-label">Storeys', 'data-target="37">37</span><span class="stat-label">Storeys Per Tower')
    html = html.replace('SQM Total GFA', 'SQM Leasable Area')
    html = html.replace('column-free, 1,850–2,100 SQM per floor, full-height glazing.', 'column-free floor plates, flexible layouts and full-height glazing.')
    html = html.replace('Column-free open-plan layouts from 1,850 SQM per floor with full-height glazing.', 'Column-free floor plates, flexible workplace layouts and full-height glazing.')
    html = html.replace('<a href="amenities.html">Amenities</a>\n      </div>\n      <div class="ft-col">', '<a href="amenities.html">Amenities</a>\n        <a class="ft-secondary" href="availability.html">Availability</a>\n        <a class="ft-secondary" href="visit.html">Visit</a>\n        <a class="ft-secondary" href="resources.html">Resources</a>\n      </div>\n      <div class="ft-col">')
    html = html.replace('<a href="leasing.html?intent=office">Leasing Enquiry</a>', '<a href="leasing.html">Leasing Enquiry</a>\n        <a href="retail.html">Retail / F&amp;B Leasing</a>\n        <a href="occupiers.html">For Occupiers</a>')
    return html


def update_home(html: str) -> str:
    html = html.replace('<a href="leasing.html?intent=office" class="btn-ghost">Leasing Enquiry</a>', '<a href="availability.html" class="btn-ghost">Find a Space</a>')
    html = html.replace('<a href="office.html" class="btn-primary">View Floor Plans', '<a href="availability.html" class="btn-primary">View Availability')
    html = html.replace('<a href="leasing.html?intent=office" class="btn-ghost">Request Availability</a>', '<a href="availability.html#space-finder" class="btn-ghost">Find a Space</a>')
    html = html.replace('93,000 SQM</span><span>29 Lieu Giai', '93,000 SQM</span><span>37 Storeys Per Tower</span><span>29 Lieu Giai')
    snapshot = """<section class="home-availability" data-home-availability aria-labelledby="home-availability-title"><div class="container"><div class="home-availability-grid"><div><p class="eyebrow" style="margin-bottom:1rem">Current Opportunities</p><h2 id="home-availability-title" class="section-title">Space for the<br><em>next move.</em></h2><p class="leasing-tease-copy">Start with indicative availability across both towers, then evaluate the floor, capacity and specifications in context.</p><div class="ux-actions"><a class="btn-gold" href="availability.html">View Availability <span aria-hidden="true">→</span></a><a class="btn-outline-gold" href="availability.html#space-finder">Find a Space</a></div></div><div class="home-availability-summary"><div class="home-availability-line"><strong>Tower 01</strong><span data-home-tower="1">Opportunities on request</span></div><div class="home-availability-line"><strong>Tower 02</strong><span data-home-tower="2">Opportunities on request</span></div><div class="home-availability-line"><strong>Area Range</strong><span data-home-area-range>Confirmed by leasing</span></div><p class="home-availability-note">Illustrative availability only. Current spaces and commercial terms are confirmed by the leasing team.</p></div></div></div></section>\n"""
    return replace_required(html, '<section class="quick-links">', snapshot + '<section class="quick-links">', "homepage availability insertion")


def update_office(html: str) -> str:
    html = html.replace('<a class="btn-outline-gold" href="#floor-explorer">View Floor Plans', '<a class="btn-outline-gold" href="availability.html">View Availability')
    html = html.replace('<section class="office-v2-section office-specs"', '<section class="office-v2-section office-specs" id="office-specifications"')
    entry = f"""<section class="ux-section office-availability-entry" id="space-finder" aria-labelledby="office-finder-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Find a Space</p><h2 id="office-finder-title" class="section-title">Does it fit<br><em>your business?</em></h2></div><p class="ux-section-copy">Move from the office proposition into a requirement-led search by area, headcount, timing and tower.</p></div>{finder_markup()}</div></section>\n"""
    return replace_required(html, '<section class="office-v2-section office-stacking"', entry + '<section class="office-v2-section office-stacking"', "office finder insertion")


def update_amenities(html: str) -> str:
    replacement = """<section id="leasing" class="ux-section graphite" aria-labelledby="amenity-next-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Next Steps</p><h2 id="amenity-next-title" class="section-title">Choose your<br><em>Capital Place journey</em></h2></div><p class="ux-section-copy">Amenities support occupiers, visitors and prospective tenants in different ways. Continue through the route that matches your intent.</p></div><div class="gateway-grid"><a class="gateway-link" href="availability.html"><div><h3>Office Leasing</h3><p>Find indicative space, review a floor and request a viewing.</p></div><span>Find a Space →</span></a><a class="gateway-link" href="retail.html"><div><h3>Retail / F&amp;B</h3><p>Explore The Link and start a brand-specific enquiry.</p></div><span>Retail Leasing →</span></a><a class="gateway-link" href="occupiers.html"><div><h3>For Occupiers</h3><p>Open public amenity, visitor and building-support routes.</p></div><span>Occupier Gateway →</span></a></div></div></section>\n"""
    updated, count = re.subn(r'<section id="leasing">.*?</section>\s*(?=<div class="am-dialog")', replacement, html, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Upgrade marker not found: amenities enquiry section")
    return updated


def update_location(html: str) -> str:
    html = html.replace('<section class="loc-v2-section loc-transport"', '<section class="loc-v2-section loc-transport" id="transport"')
    visit = """<section class="ux-section alt" aria-labelledby="visit-shortcut-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Plan Your Visit</p><h2 id="visit-shortcut-title" class="section-title">From the city<br><em>to reception</em></h2></div><p class="ux-section-copy">Get practical arrival guidance for address, drop-off, parking, reception and building access.</p></div><div class="ux-actions"><a class="btn-gold" href="visit.html">Open Visitor Guide <span aria-hidden="true">→</span></a><a class="btn-outline-gold" href="https://www.google.com/maps/search/?api=1&amp;query=Capital+Place+29+Lieu+Giai+Hanoi" target="_blank" rel="noopener">Get Directions</a></div></div></section>\n"""
    return replace_required(html, '<section class="loc-statement"', visit + '<section class="loc-statement"', "location visit insertion")


def update_sustainability(html: str) -> str:
    resources = """<section class="ux-section alt" id="sustainability-resources" aria-labelledby="sustainability-resource-title"><div class="container"><div class="ux-section-head"><div><p class="eyebrow">Occupier Value</p><h2 id="sustainability-resource-title" class="section-title">From credentials<br><em>to workplace value</em></h2></div><p class="ux-section-copy">Connect certifications and building systems to the information corporate occupiers need for workplace, ESG and technical evaluation.</p></div><div class="gateway-grid"><a class="gateway-link" href="resources.html"><div><h3>Sustainability Overview</h3><p>Review public LEED and performance information in the resource hub.</p></div><span>View Resources →</span></a><a class="gateway-link" href="office.html#office-specifications"><div><h3>Building Specifications</h3><p>Review air filtration, floor systems, vertical transport and resilience.</p></div><span>View Specifications →</span></a><a class="gateway-link" href="leasing.html?intent=technical-package"><div><h3>Detailed ESG Package</h3><p>Request qualified technical and sustainability documentation.</p></div><span>Request Package →</span></a></div></div></section>\n"""
    return replace_required(html, '<section class="sus-cta">', resources + '<section class="sus-cta">', "sustainability resources insertion")


def add_home_schema(html: str) -> str:
    schema = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Place","name":"Capital Place","description":"Grade A office building comprising two 37-storey towers and approximately 93,000 sqm of office and retail space.","address":{"@type":"PostalAddress","streetAddress":"29 Lieu Giai","addressLocality":"Hanoi","addressCountry":"VN"},"telephone":"18009289","email":"leasing@capitalplace.vn","url":"https://ngh1aa.github.io/Capital/"}</script>"""
    return html.replace("</head>", schema + "\n</head>", 1)


def build_new_pages(head: Callable[..., str], nav: str, footer: str) -> Dict[str, str]:
    definitions = {
        "availability.html": ("Office Availability – Capital Place Hanoi", "Find indicative office opportunities by area, team size, move-in timing and tower at Capital Place Hanoi.", availability_page()),
        "space.html": ("Office Opportunity – Capital Place Hanoi", "Evaluate an indicative Capital Place office opportunity, floor plan, capacity and leasing next steps.", space_page()),
        "leasing.html": ("Leasing Enquiry – Capital Place Hanoi", "Request office availability, a viewing, proposal, technical package or retail leasing conversation at Capital Place Hanoi.", leasing_page()),
        "visit.html": ("Visit Capital Place Hanoi", "Plan your visit to Capital Place at 29 Lieu Giai with directions, drop-off, reception and access guidance.", visit_page()),
        "resources.html": ("Leasing Resources – Capital Place Hanoi", "Review Capital Place building facts, floor plans, specifications, sustainability and location resources.", resources_page()),
        "retail.html": ("Retail & F&B Leasing – Capital Place Hanoi", "Explore retail and F&B leasing at The Link, Capital Place Hanoi.", retail_page()),
        "occupiers.html": ("For Occupiers – Capital Place Hanoi", "Access public amenity, visitor and building support routes for Capital Place occupiers.", occupiers_page()),
        "privacy.html": ("Prototype Privacy Notice – Capital Place Hanoi", "Privacy information for the static Capital Place redesign prototype.", privacy_page()),
        "404.html": ("Page Not Found – Capital Place Hanoi", "Continue to Capital Place, office availability or leasing.", not_found_page()),
    }
    return {name: head(title, description) + "\n" + nav + "\n" + body + "\n" + footer for name, (title, description, body) in definitions.items()}


def apply_upgrade(pages: Dict[str, str], head: Callable[..., str], nav: str, footer: str) -> Dict[str, str]:
    upgraded = dict(pages)
    upgraded["index.html"] = update_home(upgraded["index.html"])
    upgraded["office.html"] = update_office(upgraded["office.html"])
    upgraded["amenities.html"] = update_amenities(upgraded["amenities.html"])
    upgraded["location.html"] = update_location(upgraded["location.html"])
    upgraded["sustainability.html"] = update_sustainability(upgraded["sustainability.html"])
    upgraded.update(build_new_pages(head, nav, footer))

    for name, html in list(upgraded.items()):
        html = update_common_content(html)
        html = add_common_layer(html)
        if name == "index.html":
            html = add_home_schema(html)
        upgraded[name] = html
    return upgraded

