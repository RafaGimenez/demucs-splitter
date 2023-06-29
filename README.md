## DESCRIPTION

Simple Python script to retrieve songs from YouTube using [yt-dlp](https://github.com/yt-dlp/yt-dlp)
or a given file path; and split them into 6 stems through [Hybrid Transformer Demucs](https://github.com/facebookresearch/demucs).

## REQUIREMENTS

[Anaconda](https://www.anaconda.com/download) installation.

## SETUP

1.	Install Demucs in new Anaconda environment.

	- Make sure to initialize Demucs submodule repository:
		```
		git submodule update --init --recursive
		```
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
		- Install latest CUDA bundled PyTorch from https://pytorch.org/.
2.	Install yt-dlp in the same environment:
	```
	conda activate demucs
	pip install yt-dlp
	```
3.	Download ffmpeg.exe from https://github.com/yt-dlp/FFmpeg-Builds and place it in the root directory.

## USAGE

Launch split.py from demucs Anaconda environment and input any YouTube URL or 
audio file path (with a format supported by [Torchaudio](https://github.com/pytorch/audio)):

```
conda activate demucs
python split.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```