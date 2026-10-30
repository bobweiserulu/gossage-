import os
from PIL import Image, ImageDraw, ImageChops
RES = "android/app/src/main/res"
src = Image.open("icon.png").convert("RGB")
white = Image.new("RGB", src.size, (255, 255, 255))
bbox = ImageChops.difference(src, white).point(lambda v: 255 if v > 40 else 0).convert("L").getbbox()
logo = src.crop(bbox)

def render(size, frac, shape):
    S = size * 4
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if shape == "round":
        d.ellipse((0, 0, S - 1, S - 1), fill=(255, 255, 255, 255))
    elif shape == "square":
        d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.18), fill=(255, 255, 255, 255))
    else:
        d.rectangle((0, 0, S, S), fill=(255, 255, 255, 255))
    k = S * frac / max(logo.size)
    l = logo.resize((round(logo.width * k), round(logo.height * k)), Image.LANCZOS)
    img.paste(l, ((S - l.width) // 2, (S - l.height) // 2))
    return img.resize((size, size), Image.LANCZOS)

for name, (legacy, fg) in {"mdpi": (48, 108), "hdpi": (72, 162), "xhdpi": (96, 216),
                           "xxhdpi": (144, 324), "xxxhdpi": (192, 432)}.items():
    d = f"{RES}/mipmap-{name}"
    os.makedirs(d, exist_ok=True)
    render(legacy, 0.78, "square").save(f"{d}/ic_launcher.png")
    render(legacy, 0.66, "round").save(f"{d}/ic_launcher_round.png")
    render(fg, 0.58, "none").save(f"{d}/ic_launcher_fg.png")

os.makedirs(f"{RES}/mipmap-anydpi-v26", exist_ok=True)
xml = ('<?xml version="1.0" encoding="utf-8"?>\n'
       '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
       ' <background android:drawable="@android:color/white"/>\n'
       ' <foreground android:drawable="@mipmap/ic_launcher_fg"/>\n'
       '</adaptive-icon>\n')
for n in ("ic_launcher", "ic_launcher_round"):
    open(f"{RES}/mipmap-anydpi-v26/{n}.xml", "w").write(xml)
print("icones ok")
