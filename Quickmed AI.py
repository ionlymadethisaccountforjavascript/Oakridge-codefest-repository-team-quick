import speech_recognition as sr
import pyttsx3 as tts
import random as rdm    
import requests as req
import datetime as dt
import os as os
# from googlesearch import search
import time 
from urllib.request import urlopen
import wikipedia as wk
import pyaudio

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def getQuery():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=1) as source:
            
            speak("Please tell us your illness or condition... ")
            print("Please tell us your illness or condition... ")
            audio=r.listen(source)
            try:    
                queryspeak = r.recognize_google(audio)
                return queryspeak                   
                
                break
            except:
                print("Try Again")

    
speak("Quick    and    easy    medical    solutions    by    quick doc") #Started
print("Would you like to type or speak? (T/S)")
mode=input(" ")
if (mode=="T"):
    qtext=input("Please enter your illness or condition: ")
    qtext=qtext.lower()
    print(wk.summary(qtext,5))
    speak(wk.summary(qtext,5))

    
elif (mode=="S"):
    qspeak=getQuery()
    print(qspeak)
    print(wk.summary(qspeak,5))
    speak(wk.summary(qspeak,5))
