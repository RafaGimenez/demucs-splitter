## SETUP

1.	Install demucs in new environment
	A.	Install dependencies and library
		cd ./demucs_repo
		conda env update -f environment-cpu.yml  # if you don't have GPUs
		conda env update -f environment-cuda.yml # if you have GPUs
		conda activate demucs
		pip install -e .
	B.	Ensure GPU is recognized by PyTorch if using CUDA; if not
		conda remove pytorch
		https://pytorch.org/ (install latest CUDA enabled conda package)
2.	Install yt-dlp in the same environment
	pip install yt-dlp
3.	Download ffmpeg.exe and place it in the root directory
	https://github.com/yt-dlp/FFmpeg-Builds

## USAGE

Launch split.py from demucs environment and input YouTube URL