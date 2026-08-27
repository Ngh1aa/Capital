from pathlib import Path
import re

for page in sorted(Path('.').glob('*.html')):
    text = page.read_text()
    updated = re.sub(r'\s+/\s+(?=(?:width|height)=)', ' ', text)
    if updated != text:
        page.write_text(updated)
        print(page.name)
