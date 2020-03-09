from pydub import AudioSegment
sound = AudioSegment.from_wav("/path/to/file.wav")
sound = sound.set_channels(1)
sound.export("/output/path.wav", format="wav")