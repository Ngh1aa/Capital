def srgb(value):
    value /= 255
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4

def luminance(rgb):
    r, g, b = [srgb(x) for x in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    l1, l2 = sorted([luminance(a), luminance(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

def blend(fg, alpha, bg):
    return tuple(round(alpha * x + (1 - alpha) * y) for x, y in zip(fg, bg))

pairs = {
    'white on graphite': ((255,255,255), (17,17,17)),
    'white 62% on graphite': (blend((255,255,255), .62, (17,17,17)), (17,17,17)),
    'white 55% on graphite': (blend((255,255,255), .55, (17,17,17)), (17,17,17)),
    'ink 68% on paper': (blend((17,17,17), .68, (242,239,232)), (242,239,232)),
    'ink 58% on paper': (blend((17,17,17), .58, (242,239,232)), (242,239,232)),
    'accent on white': ((255,105,56), (255,255,255)),
    'accent ink on white': ((17,17,17), (255,255,255)),
}
for name, (fg, bg) in pairs.items():
    print(f'{name}: fg={fg}, bg={bg}, ratio={contrast(fg,bg):.2f}')
