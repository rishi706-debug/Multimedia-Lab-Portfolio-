"""Image properties and basic transformations practical."""
from pathlib import Path
import argparse
from PIL import Image, ImageFilter, ImageOps

def run(source: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as original:
        print(f"File: {source.name}")
        print(f"Format: {original.format}")
        print(f"Dimensions: {original.width} x {original.height}")
        print(f"Mode: {original.mode}")
        print(f"File size: {source.stat().st_size:,} bytes")

        image = ImageOps.exif_transpose(original).convert("RGB")
        image.save(output / "original_copy.jpg", quality=95)
        ImageOps.grayscale(image).save(output / "grayscale.png")
        ImageOps.mirror(image).save(output / "mirror.png")
        ImageOps.flip(image).save(output / "vertical_flip.png")
        ImageOps.contain(image, (640, 640)).save(output / "thumbnail.png")
        image.filter(ImageFilter.FIND_EDGES).save(output / "edges.png")
    print(f"Created outputs in: {output.resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect and transform an image.")
    parser.add_argument("image", type=Path, help="Input image path")
    parser.add_argument("--out", type=Path, default=Path("outputs/image"))
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f"Input file not found: {args.image}")
    run(args.image, args.out)
