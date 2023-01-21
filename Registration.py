import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image


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
    Label(master, text = "First name").grid(row = 0, column = 0) #positioning of first column text
    Label(master, text = "Last name").grid(row = 1, column = 0)
    e1 = Entry(master)
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

    Label(master, text = "Unique ID generator").grid(row = 8)
    Label(master, text = "").grid(row = 8)
    Button(master, text = "Generate", command = PasswordGenerator).grid(row =9)

    def  main_page():
        master.destroy()
        main = Tk() # initialization
        main.title("Dashboard")
        main.geometry("400x400") # size of window
        
        def upload_files():
            main.destroy()
            upld_fles = Tk()# initialization of upload files section
            upld_fles.title("Upload files")
            upld_fles.geometry("400x400") # size of window
            def upld_fls_pg():
                upld_fles.destroy()
                upld_fls = Tk()# initialization of upload files section
                upld_fls.title("Upload files")
                upld_fls.geometry("400x400") # size of window
            img = Button(upld_fles, text = "Upload your files here", command = askopenfile()).grid(row = 9, column = 1)
            #Frame for image display
            frame = Frame(upld_fles, width = 800, height =600)
            frame.grid(row=2, column=1)
            frame.place(anchor = 'center', relx= 0.5, rely=0.5)
            img1 = ImageTk.PhotoImage(Image.open("Prisoner.png"))
            label = Label(frame, image=img1, )
            label.pack()
        
        upload_files = Button(main, text = "upload files", command = upload_files).grid(row =15)
            
        main.mainloop()

    home_page = tk.Button(master, text ="Create account", command = main_page ).grid(row = 30, column= 1)    


    master.mainloop()


create_account = tk.Button(gui, text ="Create Account", command =createAccountPage, activebackground="Green", activeforeground="Orange", bd="5", bg="Red", fg="White", width="12", height="5", cursor="plus")
create_account.config(text='Create Account', bg='red', font='Verdana 8 bold')

create_account.place(x=100)
B.place(x=0)
gui.mainloop()

