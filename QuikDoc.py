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
import wikipediaapi as wkapi
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

wiki_wiki = wkapi.Wikipedia('en')


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
                return queryspeak                   
                break
            except:
                print("Try Again")

    
speak("Quick    and    easy    medical    solutions    by    quick doc") #Started
print("Would you like to type or speak? (T/S)")
mode=input(" ")
while True:
    if (mode=="T"):
        print("1. View details of your illness")
        print("2. View symptoms of your illness")
        print("3. View preventive measures for your illness")
        opt=int(input(" "))       
        if opt==1:
            qtext=input("Please enter your illness or condition: ")
            qtext=qtext.lower()
            print("\n")
            print(wk.summary(qtext,5))
            speak(wk.summary(qtext,5)) 
        elif opt==2:
            qtext=input("Please enter your illness or condition: ")      
            qtext=qtext.lower()
            pagepy=wiki_wiki.page(qtext)
            symptoms = pagepy.section_by_title('Signs and symptoms') 
            stringstring=symptoms.full_text().split('\n')
            symp=' '.join(stringstring[1].split()[0:150])
            print(symp)
            print("\n")
        elif opt==3:
            qtext=input("Please enter your illness or condition: ")
            pagepy=wiki_wiki.page(qtext)
            symptoms = pagepy.section_by_title('Prevention') 
            stringstring=symptoms.full_text().split('\n')
            symp=' '.join(stringstring[1].split()[0:150])
            print(symp)
            print("\n")

    
        
    elif (mode=="S"):
        print("1. View details of your illness")
        speak("View details of your illness")
        print("2. View symptoms of your illness")
        speak("View symptoms of your illness")
        print("3. View preventive measures for your illness")
        speak("View preventive measures for your illness")
        tm.sleep(2)
        speak("What would you like to do?")
        opt=int(input(" "))       
        if opt==1:
            print("Please enter your illness or condition: ")
            speak("Please enter your illness or condition: ")
            qspeak=getQuery()
            print("\n")
            print(wk.summary(qspeak,5))
            speak(wk.summary(qspeak,5)) 
        elif opt==2:
            print("Please enter your illness or condition: ") 
            speak("Please enter your illness or condition: ")
            qspeak=getQuery()    
            pagepy=wiki_wiki.page(qspeak)
            symptoms = pagepy.section_by_title('Signs and symptoms') 
            stringstring=symptoms.full_text().split('\n')
            symp=' '.join(stringstring[1].split()[0:150])
            print(symp)
            speak(symp)
            print("\n")
        elif opt==3:
            print("Please enter your illness or condition: ")
            speak("Please enter your illness or condition: ")
            qspeak=getQuery()
            pagepy=wiki_wiki.page(qspeak)
            symptoms = pagepy.section_by_title('Prevention') 
            stringstring=symptoms.full_text().split('\n')
            symp=' '.join(stringstring[1].split()[0:150])
            print(symp)
            speak(symp)
            print("\n")