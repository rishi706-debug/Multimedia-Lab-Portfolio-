"""Read video metadata and extract one frame at a fixed time interval."""
from pathlib import Path
import argparse
import cv2

def run(source: Path, output: Path, interval: float) -> None:
    output.mkdir(parents=True, exist_ok=True)
    capture = cv2.VideoCapture(str(source))
    if not capture.isOpened():
        raise RuntimeError("Could not open video. Check the path and codec.")

    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0

    print(f"File: {source.name}")
    print(f"Resolution: {width} x {height}")
    print(f"Frame rate: {fps:.2f} FPS")
    print(f"Frame count: {frame_count}")
    print(f"Duration: {duration:.2f} seconds")

    step = max(1, int(fps * interval)) if fps > 0 else 1
    index = 0
    saved = 0
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        if index % step == 0:
            target = output / f"frame_{index:06d}.jpg"
            if cv2.imwrite(str(target), frame):
                saved += 1
        index += 1
    capture.release()
    print(f"Extracted {saved} frame(s) to: {output.resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect a video and extract frames.")
    parser.add_argument("video", type=Path, help="Input video path")
    parser.add_argument("--out", type=Path, default=Path("outputs/video"))
    parser.add_argument("--interval", type=float, default=2.0,
                        help="Seconds between extracted frames (default: 2)")
    args = parser.parse_args()
    if not args.video.is_file():
        parser.error(f"Input file not found: {args.video}")
    if args.interval <= 0:
        parser.error("Interval must be greater than zero.")
    try:
        run(args.video, args.out, args.interval)
    except RuntimeError as exc:
        parser.error(str(exc))
