#!/usr/bin/env python3
"""Generate and validate the GlassesResearch social-preview PNG with no external dependencies."""
from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path

WIDTH, HEIGHT = 1200, 630
BACKGROUND = (247, 247, 244)
INK = (44, 48, 55)
MUTED = (78, 82, 88)
ACCENT = (76, 105, 112)
RULE = (205, 207, 205)
SOCIAL_URL = "https://glassesresearch.org/images/social-card.png"

FONT = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "C": ("01111", "10000", "10000", "10000", "10000", "10000", "01111"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01111", "10000", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "11011", "10001"),
    ".": ("00000", "00000", "00000", "00000", "00000", "00110", "00110"),
    " ": ("00000",) * 7,
}


def fill_rect(pixels: bytearray, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]) -> None:
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(WIDTH, x1), min(HEIGHT, y1)
    row = bytes(color) * max(0, x1 - x0)
    for y in range(y0, y1):
        start = (y * WIDTH + x0) * 3
        pixels[start:start + len(row)] = row


def draw_text(pixels: bytearray, text: str, x: int, y: int, scale: int, color: tuple[int, int, int]) -> None:
    cursor = x
    for char in text.upper():
        glyph = FONT.get(char, FONT[" "])
        for gy, row in enumerate(glyph):
            for gx, bit in enumerate(row):
                if bit == "1":
                    fill_rect(pixels, cursor + gx * scale, y + gy * scale,
                              cursor + (gx + 1) * scale, y + (gy + 1) * scale, color)
        cursor += 6 * scale


def draw_glasses(pixels: bytearray) -> None:
    x1, y1, w, h, t, x2 = 780, 160, 128, 86, 6, 940
    for x in (x1, x2):
        fill_rect(pixels, x, y1, x + w, y1 + t, INK)
        fill_rect(pixels, x, y1 + h - t, x + w, y1 + h, INK)
        fill_rect(pixels, x, y1, x + t, y1 + h, INK)
        fill_rect(pixels, x + w - t, y1, x + w, y1 + h, INK)
    fill_rect(pixels, x1 + w, y1 + 28, x2, y1 + 34, INK)
    fill_rect(pixels, x1 - 46, y1 + 20, x1, y1 + 25, INK)
    fill_rect(pixels, x2 + w, y1 + 20, x2 + w + 46, y1 + 25, INK)


def png_chunk(kind: bytes, payload: bytes) -> bytes:
    return (struct.pack(">I", len(payload)) + kind + payload
            + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF))


def write_png(path: Path) -> None:
    pixels = bytearray(BACKGROUND * (WIDTH * HEIGHT))
    fill_rect(pixels, 72, 64, 1128, 70, ACCENT)
    draw_text(pixels, "GLASSESRESEARCH", 72, 148, 7, INK)
    draw_text(pixels, "EVIDENCE FOR SMART GLASSES", 76, 302, 5, INK)
    draw_text(pixels, "MODELS  LINEAGES  OPENNESS  OWNER CONTROL", 76, 370, 4, MUTED)
    fill_rect(pixels, 72, 520, 1128, 522, RULE)
    draw_text(pixels, "GLASSESRESEARCH.ORG", 76, 548, 4, ACCENT)
    draw_glasses(pixels)

    scanlines = bytearray()
    stride = WIDTH * 3
    for y in range(HEIGHT):
        scanlines.append(0)
        scanlines.extend(pixels[y * stride:(y + 1) * stride])

    png = b"\x89PNG\r\n\x1a\n"
    png += png_chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0))
    png += png_chunk(b"IDAT", zlib.compress(bytes(scanlines), level=9))
    png += png_chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


def validate_built_preview(site_dir: Path) -> None:
    image = site_dir / "images" / "social-card.png"
    payload = image.read_bytes() if image.exists() else b""
    if len(payload) < 24 or payload[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError("social preview image is missing or invalid")
    if struct.unpack(">II", payload[16:24]) != (WIDTH, HEIGHT):
        raise RuntimeError("social preview image dimensions drifted")

    required = (
        f'<meta property="og:image" content="{SOCIAL_URL}">',
        '<meta property="og:image:type" content="image/png">',
        f'<meta property="og:image:width" content="{WIDTH}">',
        f'<meta property="og:image:height" content="{HEIGHT}">',
        '<meta property="og:image:alt" content="GlassesResearch — independent evidence for smart glasses">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:image" content="{SOCIAL_URL}">',
        '<meta name="twitter:image:alt" content="GlassesResearch — independent evidence for smart glasses">',
    )
    html_files = [p for p in site_dir.rglob("*.html") if p.name != "404.html"]
    failures = []
    for html_path in html_files:
        text = html_path.read_text(encoding="utf-8")
        missing = sum(marker not in text for marker in required)
        if missing:
            failures.append(f"{html_path}: {missing} missing share-preview markers")
    if not html_files or failures:
        raise RuntimeError("social preview validation failed: " + "; ".join(failures[:10]))


def on_config(config):
    write_png(Path(config.docs_dir) / "images" / "social-card.png")
    return config


def on_post_build(config) -> None:
    validate_built_preview(Path(config.site_dir))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_png(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
