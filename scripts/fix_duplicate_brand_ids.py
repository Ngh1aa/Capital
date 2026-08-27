from pathlib import Path
import re

page = Path('amenities.html')
text = page.read_text()
for brand in ['highlands', 'koithe', 'seven', 'akademy', 'saga', 'bowl']:
    needle = f'id="{brand}"'
    first = text.find(needle)
    if first < 0:
        continue
    second = text.find(needle, first + len(needle))
    if second >= 0:
        text = text[:second] + f'id="{brand}-detail"' + text[second + len(needle):]
page.write_text(text)
