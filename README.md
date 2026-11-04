# Multimedia Lab Portfolio

An independently written MCA Multimedia Laboratory practical portfolio.

> This is a learning starter pack. Run each practical, capture your own output screenshots, fill in the report templates, and confirm the exact experiment list with your faculty. The repository that inspired the topic selection is credited here: [ARPANPATRA111/mm-lab](https://github.com/ARPANPATRA111/mm-lab). This project is not a copy of that repository.

## Practicals

| Practical | Topic | Main file | Requirements |
|---|---|---|---|
| 01 | Image properties and transformations | `practical-01-image/image_lab.py` | Pillow |
| 02 | WAV audio analysis and effects | `practical-02-audio/audio_lab.py` | Python standard library |
| 03 | Video metadata and frame extraction | `practical-03-video/video_lab.py` | OpenCV |
| 04 | Basic image enhancement and optional OCR workflow | `practical-04-image-pipeline/image_pipeline.py` | Pillow; OCR optional |

## Setup

Use Python 3.10 or newer.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## Run

```bash
# Image: show properties and create grayscale, thumbnail and edge outputs
python practical-01-image/image_lab.py path/to/photo.jpg --out outputs/image

# Audio: inspect a PCM WAV file and create a reversed copy
python practical-02-audio/audio_lab.py path/to/audio.wav --out outputs/audio

# Video: inspect a video and extract frames at a chosen interval
python practical-03-video/video_lab.py path/to/video.mp4 --out outputs/video --interval 2

# Image enhancement pipeline
python practical-04-image-pipeline/image_pipeline.py path/to/photo.jpg --out outputs/enhanced
```

Video practical requires a working OpenCV installation. If a codec is unsupported, try another MP4/AVI file.

## Report format

Each practical has a `report.md` template. Fill in:
- Aim and learning objectives
- Theory in your own words
- Software and hardware requirements
- Algorithm / procedure
- Input and output screenshots
- Observations and result
- Viva questions and answers

## Suggested submission checklist

- [ ] Run every practical on your own sample files.
- [ ] Add screenshots of actual outputs in the relevant `screenshots/` folder.
- [ ] Complete each report template.
- [ ] Check that file paths and commands work on your computer.
- [ ] Add your course, semester, roll number and faculty details only if required.
- [ ] Follow your institution's academic-integrity rules and cite adapted material.

## Credits and attribution

The practical topic selection was informed by the public repository linked above. Code in this starter pack is independently written for this portfolio. If you adapt any third-party code, media, or documentation, add its source and applicable license here.
