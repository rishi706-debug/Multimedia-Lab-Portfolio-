"""Inspect a PCM WAV file and create a reversed WAV copy using stdlib only."""
from pathlib import Path
import argparse
import wave

def inspect_and_reverse(source: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    with wave.open(str(source), "rb") as wav:
        channels = wav.getnchannels()
        width = wav.getsampwidth()
        rate = wav.getframerate()
        frames_count = wav.getnframes()
        compression = wav.getcomptype()
        frames = wav.readframes(frames_count)

    duration = frames_count / rate if rate else 0
    print(f"File: {source.name}")
    print(f"Channels: {channels}")
    print(f"Sample width: {width * 8} bits")
    print(f"Sample rate: {rate} Hz")
    print(f"Frames: {frames_count}")
    print(f"Duration: {duration:.3f} seconds")
    print(f"Compression: {compression}")

    # Reverse complete audio frames, preserving channel/sample grouping.
    frame_width = channels * width
    if frame_width == 0 or len(frames) % frame_width:
        raise ValueError("Unexpected WAV frame data.")
    reversed_frames = b"".join(
        frames[i:i + frame_width]
        for i in range(len(frames) - frame_width, -1, -frame_width)
    )
    destination = output / f"{source.stem}_reversed.wav"
    with wave.open(str(destination), "wb") as result:
        result.setnchannels(channels)
        result.setsampwidth(width)
        result.setframerate(rate)
        result.writeframes(reversed_frames)
    print(f"Reversed audio saved to: {destination.resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect and reverse an uncompressed PCM WAV.")
    parser.add_argument("audio", type=Path, help="Input WAV file")
    parser.add_argument("--out", type=Path, default=Path("outputs/audio"))
    args = parser.parse_args()
    if not args.audio.is_file():
        parser.error(f"Input file not found: {args.audio}")
    try:
        inspect_and_reverse(args.audio, args.out)
    except (wave.Error, ValueError) as exc:
        parser.error(str(exc))
