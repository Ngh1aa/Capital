from pathlib import Path

for page in sorted(Path('.').glob('*.html')):
    text = page.read_text()
    nav_end = text.find('</nav>')
    if nav_end < 0:
        continue
    before_nav = text[:nav_end]
    nav_links_marker = '<div class="nav-links">'
    start = before_nav.find(nav_links_marker)
    if start >= 0:
        nav_part = before_nav[start:before_nav.find('<div class="nav-sep">', start)]
        if 'href="visit.html"' not in nav_part:
            needle = '<a href="amenities.html">Amenities</a>'
            text = text.replace(needle, needle + '<a href="visit.html">Visit</a><a href="resources.html">Resources</a>', 1)
    menu_marker = '<div id="mob-menu">'
    menu_start = before_nav.find(menu_marker)
    if menu_start >= 0:
        menu_part = before_nav[menu_start:]
        if 'onclick="closeMob()">Visit</a>' not in menu_part:
            needle = '<a href="amenities.html" onclick="closeMob()">Amenities</a>'
            text = text.replace(needle, needle + '<a href="visit.html" onclick="closeMob()">Visit</a><a href="resources.html" onclick="closeMob()">Resources</a>', 1)
    page.write_text(text)
