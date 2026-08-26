from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
issues = []
for path in sorted(ROOT.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    links = soup.select('link[href*="assets/media-frame.css"]')
    if len(links) != 1:
        issues.append(f'{path.name}: expected one media-frame.css link, got {len(links)}')
    for frame in soup.select('.media-frame'):
        if frame.name == 'img':
            issues.append(f'{path.name}: media-frame applied directly to img instead of wrapper')
        cls = set(frame.get('class', []))
        if not cls.intersection({'media-frame--hero','media-frame--cinematic','media-frame--landscape','media-frame--wide','media-frame--portrait','media-frame--square'}):
            if not cls.intersection({'media-frame--contain','media-frame--absolute'}):
                issues.append(f'{path.name}: frame without preset/modifier: {sorted(cls)}')
        for img in frame.find_all('img', recursive=False):
            src = img.get('src', '')
            if not src or src.startswith(('http://','https://','data:')):
                continue
            img_path = ROOT / src
            if not img_path.exists():
                issues.append(f'{path.name}: missing image {src}')
                continue
            try:
                with Image.open(img_path) as im:
                    w, h = im.size
                # Technical visuals should never use cover, but also flag tiny photo sources
                # if a frame is likely to be rendered larger than 700px in either dimension.
                if 'media-frame--contain' not in cls and max(w, h) < 700 and src.lower().endswith(('.jpg','.jpeg','.png','.webp')):
                    print(f'NOTICE low-resolution source in cover frame: {path.name} {src} {w}x{h}')
            except Exception as exc:
                issues.append(f'{path.name}: cannot inspect {src}: {exc}')

if issues:
    print('\n'.join(issues))
    raise SystemExit(1)
print('Media Frame System static QA: PASS')
print(f'HTML pages checked: {len(list(ROOT.glob("*.html")))}')
print(f'Frames checked: {sum(len(BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser").select(".media-frame")) for p in ROOT.glob("*.html"))}')
