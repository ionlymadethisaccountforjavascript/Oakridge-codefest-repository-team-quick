import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

gui = Tk(className='quickDoc')
gui.geometry("400x200")
gui['bg']='black'

def helloCallBack():
   messagebox.showinfo("About", "QUICKDOC IS A DESTINATION FOR YOUR PERSONAL MEDICAL FILES INSTEAD OF LOSING APHYSICAL COPY OUR BETTER DIGITAL COPY CAN RECOVER YOUR DECADE LONG FILE INSECONDSOUR AI CONSULTANT HAS SPECIAL VOICE RECOGNITION THAT CAN RECOGNISE YOUR ILLNESS AND TELL YOU MORE ABOUT IT THROUGH THE TEXT OR SPEECH OPTION THE TEXT OR SPEECH OPTIONIS USED TO HELP DISABLED CLIENTS FIND THEIR WAY OUR MISSION IS TOGIVE A BETTER MEDICAL RUN THROUGH FOR CLIENTS")


B = tk.Button(gui, text ="About", command = helloCallBack, activebackground="Green", activeforeground="Orange", bd="5", bg="Red", fg="White", width="10", height="5", cursor="plus")
B.config(text='About', bg='red', font='Verdana 8 bold')

def createAccountPage():
    gui.destroy()
    """Create a new top level window"""
    master = Tk() # initialization
    master.title("Registration")
    master.geometry("400x400") # size of window
    Label(master, text = "First name").grid(row = 0, column = 0) #positioning of first column 
    e1 = Entry(master)
    Label(master, text = "Last name").grid(row = 1, column = 0)
    e2 = Entry(master)

    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    
    #subheading
    Label(master, text = "Gender select").grid(row = 2, column = 0)
    #checkbox part
    #first checkbox
    var1 = IntVar
    G1 = Checkbutton(master, text = "Male", variable = var1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
    #second checkbox
    var2 = IntVar
    G2 = Checkbutton(master, text = "Female", variable = var2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
    #third checkbox
    var3 = IntVar
    G3 = Checkbutton(master, text = "Other", variable = var3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
    #fourth checkbox
    var4 = IntVar
    G4 = Checkbutton(master, text = "Rather Not Say", variable = var4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
    if G1 == ON and G2 == OFF and G3 == OFF and G4 == OFF:
        G1.select()
        G2.deselect()
        G3.deselect()
        G4.deselect()
    elif G1 == OFF and G2 == ON and G3 == OFF and G4 == OFF:
        G2.select()
        G1.deselect()
        G3.deselect()
        G4.deselect()
    elif G1 == OFF and G2 == OFF and G3 == ON and G4 == OFF:
        G3.select()
        G2.deselect()
        G1.deselect()
        G4.deselect()
    elif G1 == OFF and G2 == OFF and G3 == OFF and G4 == ON:
        G4.select()
        G2.deselect()
        G3.deselect()
        G1.deselect()
    else:
        G1.deselect()
        G2.deselect()
        G3.deselect()
        G4.deselect()

    G1.grid(row = 3, column = 1)
    G2.grid(row = 4, column = 1)
    G3.grid(row = 5, column = 1)
    G4.grid(row = 6, column = 1)

    #Aadhar card pin
    Label(master, text = "Enter your Aadhar card pin").grid(row = 7)
    e3 = Entry(master)
    e3.grid(row = 7, column = 1)

    e7 = e3.get()

    #Password generator
    def PasswordGenerator():
        import random

        x = str(random.randint(100,999))
        y = random.randint(0,1)
        a = random.randint(0,25)
        b = random.randint(0,1)
        c = random.randint(0,25)
        d = random.randint(0,1)
        z = random.randint(0,25)

        upperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        lowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letters = [upperCase,lowerCase]
        def password():
            hop = letters[y][z]
            hop1 = letters[b][a]
            hop2 = letters[d][c]
            final=x+hop+hop1+hop2

            return final


        xx=password()
        Label(master, text = xx).grid(row = 10)
    pg = PasswordGenerator()
    Label(master, text = "Unique ID generator").grid(row = 8)
    Label(master, text = "").grid(row = 8)
    Button(master, text = "Generate", command = PasswordGenerator).grid(row =9)

    def  main_page():
        master.destroy()
        main = Tk() # initialization
        main.title("Dashboard")
        main.geometry("400x400") # size of window
        
        def upload_files():
            upld_fles = Tk()# initialization of upload files section
            upld_fles.title("Upload files")
            upld_fles.geometry("400x400") # size of window
            def upld_fls_pg():
                upld_fls = Tk()# initialization of upload files section
                upld_fls.title("Upload files")
                upld_fls.geometry("400x400") # size of window
            Button(upld_fles, text = "Upload your files here", command = askopenfile()).grid(row = 0, column = 1)

        Button(main, text = "upload files", command = upload_files).grid(row =1)
        def account_page():
            accpage = Tk()# initialization of account page
            accpage.title("Account")
            accpage.geometry("400x400") # size of window
            accpage.title("Account details")
            def acc():
                accprn1 = Tk()
                accprn1.title("Account details")
                accprn1.geometry("400x400") # size of window
                Label(e1)
            Button(accpage, text = "name", command = acc)

            lbl.config(text = "First Name: "+e5)
            e5 = tk.Text(accpage, height = 5, width = 20)
            e5.pack()
            lbl = tk.Label(accpage, text = "")
            lbl.pack()
            e7 = acc()
            def acc1():
                e6 = e2.get()
                lbl.config(text = "Last Name: "+e6)
                e6 = tk.Text(accpage, height = 5, width = 20)
                e6.pack()
                lbl = tk.Label(accpage, text = "")
                lbl.pack()
            e8 = acc1()
            #Account details
            Label(accpage, text=e7).grid(row = 2, column = 1)
            Label(accpage, text=e8).grid(row = 3, column = 1)
            #Aadhar pin number
            Label(accpage, text = "Aadhar card pin",).grid(row = 5, column = 1)
            Button(accpage,text = "Obtain Pin", command = PasswordGenerator).grid()
            #Password
            Label(accpage, text = "Password",).grid(row = 7, column = 1)
            Label(accpage, text = pg,).grid(row = 8, column = 1)
        
        Button(main, text = "Account details", command = account_page).grid( row = 1, column = 4)

        def aiConsultant():
            aiCons = Tk()# initialization of ai consultant page
            aiCons.title("AI Consultant")
            aiCons.geometry("400x400") # size of window
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
                        Label(aiCons,"Please tell us your illness or condition... ")
                        audio=r.listen(source)
                        Label(aiCons,audio)
                        try:    
                            queryspeak = r.recognize_google(audio)
                            return queryspeak                   
                            break
                        except:
                            Label(aiCons,text = "Try Again")

    
            speak("Quick    and    easy    medical    solutions    by    quick doc") #Started
            ("Would you like to type or speak? (T/S)")
            mode=input(" ")
            while True:
                if (mode=="T"):
                    ("1. View details of your illness")
                    ("2. View symptoms of your illness")
                    ("3. View preventive measures for your illness")
                    opt=int(input(" "))       
                    if opt==1:
                        qtext=input("Please enter your illness or condition: ")
                        qtext=qtext.lower()
                        ("\n")
                        (wk.summary(qtext,5))
                        speak(wk.summary(qtext,5)) 
                    elif opt==2:
                        qtext=input("Please enter your illness or condition: ")      
                        qtext=qtext.lower()
                        pagepy=wiki_wiki.page(qtext)
                        symptoms = pagepy.section_by_title('Signs and symptoms') 
                        stringstring=symptoms.full_text().split('\n')
                        symp=' '.join(stringstring[1].split()[0:150])
                        (symp)
                        ("\n")
                    elif opt==3:
                        qtext=input("Please enter your illness or condition: ")
                        pagepy=wiki_wiki.page(qtext)
                        symptoms = pagepy.section_by_title('Prevention') 
                        stringstring=symptoms.full_text().split('\n')
                        symp=' '.join(stringstring[1].split()[0:150])
                        (symp)
                        ("\n")



                    elif (mode=="S"):
                        ("1. View details of your illness")
                        speak("View details of your illness")
                        ("2. View symptoms of your illness")
                        speak("View symptoms of your illness")
                        ("3. View preventive measures for your illness")
                        speak("View preventive measures for your illness")
                        tm.sleep(2)
                        speak("What would you like to do?")
                        opt=int(input(" "))       
                    if opt==1:
                        ("Please enter your illness or condition: ")
                        speak("Please enter your illness or condition: ")
                        qspeak=getQuery()
                        ("\n")
                        (wk.summary(qspeak,5))
                        speak(wk.summary(qspeak,5)) 
                    elif opt==2:
                        ("Please enter your illness or condition: ") 
                        speak("Please enter your illness or condition: ")
                        qspeak=getQuery()    
                        pagepy=wiki_wiki.page(qspeak)
                        symptoms = pagepy.section_by_title('Signs and symptoms') 
                        stringstring=symptoms.full_text().split('\n')
                        symp=' '.join(stringstring[1].split()[0:150])
                        (symp)
                        speak(symp)
                        ("\n")
                    elif opt==3:
                        ("Please enter your illness or condition: ")
                        speak("Please enter your illness or condition: ")
                        qspeak=getQuery()
                        pagepy=wiki_wiki.page(qspeak)
                        symptoms = pagepy.section_by_title('Prevention') 
                        stringstring=symptoms.full_text().split('\n')
                        symp=' '.join(stringstring[1].split()[0:150])
                        (symp)
                        speak(symp)
                        ("\n")

            
        Button(main,text = "AI consultant", command = aiConsultant).grid(column=6, row = 1)

    home_page = tk.Button(master, text ="Create account", command = main_page ).grid(row = 30, column= 1)    


    master.mainloop()


create_account = tk.Button(gui, text ="Create Account", command =createAccountPage, activebackground="Green", activeforeground="Orange", bd="5", bg="Red", fg="White", width="12", height="5", cursor="plus")
create_account.config(text='Create Account', bg='red', font='Verdana 8 bold')

create_account.place(x=100)
B.place(x=0)
gui.mainloop()

