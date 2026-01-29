whisper:
	OMP_NUM_THREADS=2 nice -n 15 whisper audio.wav --model small --language Spanish --task transcribe --output_format txt
