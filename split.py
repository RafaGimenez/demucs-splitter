import ffmpeg
import yt_dlp
import argparse
import demucs.separate

from pathlib import Path

SONG_DIR = Path("./music")
STEM_DIR = Path("./stems")

ydl_opts = {
    "outtmpl": Path(SONG_DIR, "%(title)s.%(ext)s").as_posix(),
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


def backing_track(track: str):
    """
    Merge all stems except guitar to create a backing track.
    """
    out_dir = Path(STEM_DIR, "htdemucs_6s", track)  # Output directory

    # Iterate over the stems
    stems = []  # List of fmmpeg streams
    for stem in out_dir.glob("*.mp3"):
        if "guitar" not in stem.name:
            stems.append(ffmpeg.input(stem.as_posix()))

    # Merge stems and save
    merged = ffmpeg.filter(stems, "amix", inputs=len(stems))
    merged = ffmpeg.output(merged, Path(out_dir, "backing.mp3").as_posix())
    try:
        ffmpeg.run(merged, capture_stderr=True)
    except ffmpeg.Error as e:
        print("stderr:", e.stderr.decode("utf8"))
        raise e


if __name__ == "__main__":
    # Parse arguments and create music directory
    SONG_DIR.mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description="Stem splitting with Demucs")
    parser.add_argument("track", type=str, help="YouTube URL or audio file path")
    args = parser.parse_args()

    # If needed download music
    if Path(args.track).exists():
        track_path = Path(args.track)
        track = track_path.name
    else:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            track: str = ydl.extract_info(args.track, download=False)["title"]
            ydl.download(args.track)
        track_path = SONG_DIR / f"{track}.mp3"

    # Separate track
    demucs.separate.main(
        [
            "--mp3",
            "-n",
            "htdemucs_6s",
            track_path.as_posix(),
            "-o",
            STEM_DIR.as_posix(),
        ]
    )

    # Create backing track
    print("Creating guitar backing track...")
    backing_track(track)
    save_path = Path(STEM_DIR, "htdemucs_6s", track)
    print(f"\nDone! Stems saved at: {save_path}")
