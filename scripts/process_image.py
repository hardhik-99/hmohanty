"""Generate the landscape black-and-white hero image.

Crops the portrait-orientation `hm_beach.jpeg` to a ~3:2 landscape frame that
keeps the palm trees (left), the beach and ocean band (center), and the subject
(right), then converts the result to black and white with a gentle contrast
and sharpness bump so the editorial look reads as intentional.

Run from repo root (or anywhere):

    python scripts/process_image.py
"""
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img" / "hm_beach.jpeg"
DST = ROOT / "assets" / "img" / "hm_beach_bw.jpg"

CROP_TOP_PCT = 0.30
CROP_BOTTOM_PCT = 0.90
CONTRAST = 1.15
SHARPNESS = 1.10
JPEG_QUALITY = 90


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source image not found: {SRC}")

    with Image.open(SRC) as src:
        src.load()
        width, height = src.size
        top = int(height * CROP_TOP_PCT)
        bottom = int(height * CROP_BOTTOM_PCT)
        cropped = src.crop((0, top, width, bottom))

    bw = ImageOps.grayscale(cropped).convert("RGB")
    bw = ImageEnhance.Contrast(bw).enhance(CONTRAST)
    bw = ImageEnhance.Sharpness(bw).enhance(SHARPNESS)

    DST.parent.mkdir(parents=True, exist_ok=True)
    bw.save(DST, quality=JPEG_QUALITY, optimize=True)
    print(f"Wrote {DST} ({bw.size[0]}x{bw.size[1]})")


if __name__ == "__main__":
    main()
