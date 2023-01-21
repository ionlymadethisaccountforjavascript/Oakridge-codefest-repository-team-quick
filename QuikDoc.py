import speech_recognition as sr
import pyttsx3 as tts
import random as rdm    
import requests as req
import datetime as dt
import os
from googlesearch import search
import time as tm
from urllib.request import urlopen
import wikipedia as wk
import pyaudio
from os.path import exists
import tkinter as tk

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
            print(audio)
            try:    
                queryspeak = r.recognize_sphinx(audio)
                return queryspeak                   
                break
            except:
                print("Try Again")

    
speak("Quick    and    easy    medical    solutions    by    quick doc") #Started
print("Would you like to type or speak? (T/S)")
mode=input(" ")
if (mode=="T"):
    print("1. View symptoms of your illness")
    print("2. View details of your illness")
    print("3. View treatments of your illness")
    opt=int(input(" "))
    if opt==2:
        qtext=input("Please enter your illness or condition: ")
    qtext=qtext.lower()
    print(wk.summary(qtext,5))
    speak(wk.summary(qtext,5)) 
 
    
elif (mode=="S"):
    qspeak=getQuery()
    qspeak=qspeak.lower()
    print(wk.summary(qspeak,5))
    speak(wk.summary(qspeak,5)) 

  