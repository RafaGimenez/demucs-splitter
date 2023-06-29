import os
import yt_dlp
import argparse
import demucs.separate

from pathlib import Path

SONG_DIR = "./music"
STEM_DIR = "./stems"

ydl_opts = {
    "outtmpl": os.path.join(SONG_DIR, "%(title)s.%(ext)s"),
    "extract_audio": True,
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
    "compat_opts": set(),
    "ffmpeg_location": "./",
}

if __name__ == "__main__":
    # Parse arguments and create music directory
    Path(SONG_DIR).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description="Stem splitting with Demucs")
    parser.add_argument("url", type=str, help="YouTube URL")
    args = parser.parse_args()

    # Download music
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        track: str = ydl.extract_info(args.url, download=False)["title"]
        ydl.download(args.url)

    # Separate track
    demucs.separate.main(
        [
            "--mp3",
            "-n",
            "htdemucs_6s",
            os.path.join(SONG_DIR, f"{track}.mp3"),
            "-o",
            STEM_DIR,
        ]
    )
