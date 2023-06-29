## REQUIREMENTS

Anaconda installation (https://www.anaconda.com/download).

## SETUP

1.	Install demucs in new environment.

	- Install dependencies and library:
		```
		cd ./demucs_repo
		conda env update -f environment-cpu.yml  # if you don't have GPUs
		conda env update -f environment-cuda.yml # if you have GPUs
		conda activate demucs
		pip install -e .
		```
	- If using NVIDIA GPU, ensure it is recognized by PyTorch:
		```python
		import torch
		assert torch.cuda.is_available()
		```
	- If NVIDIA GPU is not recognized:
		```
		conda activate demucs
		conda remove pytorch
		```
		- Install latest CUDA bundled PyTorch from https://pytorch.org/
2.	Install yt-dlp in the same environment:
	```
	conda activate demucs
	pip install yt-dlp
	```
3.	Download ffmpeg.exe from https://github.com/yt-dlp/FFmpeg-Builds and place it in the root directory.

## USAGE

Launch split.py from demucs Anaconda environment and input YouTube URL.