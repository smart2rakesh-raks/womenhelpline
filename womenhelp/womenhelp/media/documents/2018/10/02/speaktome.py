#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import re
import random
from time import ctime
import time
import pyttsx3
import pyaudio,os
import speech_recognition as sr
import webbrowser

 
   
 
def speak(msg):
	
	engine = pyttsx3.init()
	engine.setProperty('rate', 120)
	engine.say(msg)
	engine.runAndWait()
	
def listen():

	r = sr.Recognizer()
	r.pause_threshold = 0.6
	with sr.Microphone(1) as source:
		audio = r.adjust_for_ambient_noise(source)
		print ("listening...")
		audio = r.listen(source, timeout=1) # listen for the first phrase and extract it into audio data
	try:
		return r.recognize_google(audio)
	except : # speech is unintelligible
		return "i  am unable to understand"
		

	
 


         
speak(" program ,can you teach me few words ?")

val = listen()

speak("do you  mean ?"+val)








