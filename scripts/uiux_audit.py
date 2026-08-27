from pathlib import Path
import re

for page in sorted(Path('.').glob('*.html')):
    text = page.read_text(errors='ignore')
    imgs = re.findall(r'<img\b[^>]*>', text, re.I)
    buttons = re.findall(r'<button\b[^>]*>', text, re.I)
    links = re.findall(r'<a\b[^>]*>', text, re.I)
    forms = re.findall(r'<(?:input|select|textarea)\b[^>]*>', text, re.I)
    headings = re.findall(r'<h[1-6]\b', text, re.I)
    h1 = len(re.findall(r'<h1\b', text, re.I))
    missing_alt = sum('alt=' not in tag.lower() for tag in imgs)
    missing_dims = sum(not re.search(r'\b(width|height)=', tag, re.I) for tag in imgs)
    missing_type = sum('type=' not in tag.lower() for tag in buttons)
    empty_href = sum(re.search(r'href=["\'](?:#|javascript:)', tag, re.I) is not None for tag in links)
    labelled_controls = sum(bool(re.search(r'aria-label|aria-labelledby|id=', tag, re.I)) for tag in forms)
    ids = re.findall(r'id=["\']([^"\']+)', text)
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    print(f'{page.name}: h1={h1}, headings={len(headings)}, images={len(imgs)}, missing_alt={missing_alt}, missing_dims={missing_dims}, buttons={len(buttons)}, buttons_without_type={missing_type}, forms={len(forms)}, controls_with_basic_label_signal={labelled_controls}, empty_href={empty_href}, duplicate_ids={duplicate_ids}')
