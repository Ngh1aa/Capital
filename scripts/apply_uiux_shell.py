from pathlib import Path
import re

for page in sorted(Path('.').glob('*.html')):
    text = page.read_text()
    if 'capital-uiux-v2.css' not in text:
        text = text.replace('</head>', '  <link rel="stylesheet" href="assets/capital-uiux-v2.css?v=uiux-20260827-1" />\n</head>', 1)
    if 'capital-uiux-v2.js' not in text:
        text = text.replace('</body>', '  <script src="assets/capital-uiux-v2.js?v=uiux-20260827-1"></script>\n</body>', 1)
    def add_body_class(match):
        attrs = match.group(1)
        if re.search(r'\bclass="', attrs):
            attrs = re.sub(r'class="([^"]*)"', lambda m: f'class="{m.group(1)} capital-uiux-v2"', attrs, count=1)
        else:
            attrs += ' class="capital-uiux-v2"'
        return '<body' + attrs + '>'
    text = re.sub(r'<body([^>]*)>', add_body_class, text, count=1)
    if 'href="visit.html"' not in text and 'class="nav-links"' in text:
        text = text.replace('<a href="amenities.html">Amenities</a>', '<a href="amenities.html">Amenities</a><a href="visit.html">Visit</a><a href="resources.html">Resources</a>', 1)
    if 'onclick="closeMob()">Visit</a>' not in text and 'id="mob-menu"' in text:
        text = text.replace('<a href="amenities.html" onclick="closeMob()">Amenities</a>', '<a href="amenities.html" onclick="closeMob()">Amenities</a><a href="visit.html" onclick="closeMob()">Visit</a><a href="resources.html" onclick="closeMob()">Resources</a>', 1)
    text = text.replace('<button type="button" class="active" onclick="setLang(\'EN\')">EN</button>', '<button type="button" class="active" aria-label="English" onclick="setLang(\'EN\')">EN</button>')
    text = text.replace('<button type="button" onclick="setLang(\'VI\')">VI</button>', '<button type="button" aria-label="Vietnamese" onclick="setLang(\'VI\')">VI</button>')
    page.write_text(text)
