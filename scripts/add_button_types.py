from pathlib import Path
import re

for page in sorted(Path('.').glob('*.html')):
    text = page.read_text()
    updated = re.sub(r'<button(?![^>]*\btype=)([^>]*)>', r'<button type="button"\1>', text, flags=re.I)
    if updated != text:
        page.write_text(updated)
        print(page.name)
