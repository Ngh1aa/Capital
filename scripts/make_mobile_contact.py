from pathlib import Path
from PIL import Image, ImageDraw

src = Path('/home/ubuntu/Capital-mobile-audit')
files = sorted(src.glob('*.png'))
thumb_w, thumb_h = 195, 422
label_h = 32
cols = 5
rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols * thumb_w, rows * (thumb_h + label_h)), '#dedbd4')
draw = ImageDraw.Draw(sheet)
for i, path in enumerate(files):
    image = Image.open(path).convert('RGB')
    image.thumbnail((thumb_w, thumb_h))
    x = (i % cols) * thumb_w + (thumb_w - image.width) // 2
    y = (i // cols) * (thumb_h + label_h)
    sheet.paste(image, (x, y))
    draw.text(((i % cols) * thumb_w + 8, y + thumb_h + 6), path.stem, fill='#111')
sheet.save('/home/ubuntu/Capital-mobile-audit/contact-sheet.png')
