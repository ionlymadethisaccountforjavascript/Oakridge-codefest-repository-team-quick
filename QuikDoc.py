import speech_recognition as sr
import pyttsx3 as tts
import random as rdm    
import requests as req
import datetime as dt
import os as os
from googlesearch import search
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
            print(audio)
            try:    
                queryspeak = r.recognize_google(audio)
                yn=input("Is it",queryspeak,"?  (Y/N)")
                if(yn=="Y"):
                    return queryspeak
                elif(yn=="N"):
                    print("Please say it again")
                    queryspeak = r.recognize_google(audio)  
                    
                
                break
            except:
                print("Try Again")

    
speak("Quick    and    easy    medical    solutions    by    quick doc") #Started
print("Would you like to type or speak? (T/S)")
mode=input(" ")
if (mode=="T"):
    qtext=input("Please enter your illness or condition: ")
elif (mode=="S"):
    qspeak=getQuery()

qtext=qtext.lower()
print(wk.summary(qtext,3))
speak(wk.summary(qtext,3))

