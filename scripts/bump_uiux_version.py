from pathlib import Path

for page in Path('.').glob('*.html'):
    text = page.read_text()
    text = text.replace('capital-uiux-v2.css?v=uiux-20260827-1', 'capital-uiux-v2.css?v=uiux-20260827-2')
    text = text.replace('capital-uiux-v2.js?v=uiux-20260827-1', 'capital-uiux-v2.js?v=uiux-20260827-2')
    page.write_text(text)
