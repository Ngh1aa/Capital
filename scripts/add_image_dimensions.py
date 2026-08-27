from pathlib import Path
import re
from PIL import Image

root = Path('.')
for page in sorted(root.glob('*.html')):
    text = page.read_text()
    changed = [False]
    def replace_img(match):
        nonlocal_text = match.group(0)
        src_match = re.search(r'\bsrc=["\']([^"\']+)["\']', nonlocal_text, re.I)
        if not src_match or re.search(r'\bwidth=', nonlocal_text, re.I) or re.search(r'\bheight=', nonlocal_text, re.I):
            return nonlocal_text
        src = src_match.group(1).split('?')[0].split('#')[0]
        if src.startswith(('http://', 'https://', 'data:')):
            return nonlocal_text
        image_path = root / src
        if not image_path.exists():
            return nonlocal_text
        try:
            with Image.open(image_path) as image:
                width, height = image.size
        except Exception:
            return nonlocal_text
        changed[0] = True
        return nonlocal_text[:-1] + f' width="{width}" height="{height}" />'
    updated = re.sub(r'<img\b[^>]*?/?>', replace_img, text, flags=re.I)
    if changed[0]:
        page.write_text(updated)
        print(page.name)
