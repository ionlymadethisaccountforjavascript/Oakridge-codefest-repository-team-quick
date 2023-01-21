


from tkinter import *

master = Tk() # initialization
master.title("Registration")
master.geometry("400x400") # size of window
Label(master, text = "First name").grid(row = 0, column = 0) #positioning of first column text
Label(master, text = "Last name").grid(row = 1, column = 0)

# input part

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

#subheading
Label(master, text = "Gender select").grid(row = 2, column = 0)
#checkbox part
#first checkbox
var1 = IntVar
Checkbutton(master, text = "Male", variable=var1).grid(row = 3,column = 1, sticky = W)
#second checkbox
var2 = IntVar
Checkbutton(master, text = "Female", variable=var2).grid(row =4, column = 1,sticky = W)
#third checkbox
var3 = IntVar
Checkbutton(master, text = "Other", variable=var3).grid(row =5, column = 1,sticky = W)
#fourth checkbox
var4 = IntVar
Checkbutton(master, text = "Rather not say", variable=var4).grid(row =6, column = 1,sticky = W)

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

Button(master, text ="Create account", command = "" ).grid(row = 30, column= 1)


mainloop()


