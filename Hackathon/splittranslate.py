# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:24:10 2019

@author: Shubham Bhate
"""
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr 
import os

myaudio = AudioSegment.from_file("job.wav" , "wav") 
chunk_length_ms = 5000 
chunks = make_chunks(myaudio, chunk_length_ms) 
translate=""
for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    chunk.export(chunk_name, format="wav")
    AUDIO_FILE = "chunk{0}.wav".format(i)  
    r = sr.Recognizer() 
    with sr.AudioFile(AUDIO_FILE) as source: 
        audio = r.record(source)   
    try: 
        translate=translate +" "+ r.recognize_google(audio)
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    
    os.remove("chunk{0}.wav".format(i))
print(translate)