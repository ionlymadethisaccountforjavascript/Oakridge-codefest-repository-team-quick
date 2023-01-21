


from tkinter import *

master = Tk() # initialization
master.title("Registration")
master.geometry("400x400") # size of window
Label(master, text = "First name").grid(row = 0) #positioning of first column text
Label(master, text = "Last name").grid(row = 1)

# input part

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

#subheading
Label(master, text = "Gender select").grid(row = 2, column = 1)
#checkbox part
#first checkbox
var1 = IntVar
Checkbutton(master, text = "Male", variable=var1).grid(row = 3, sticky = W)
#second checkbox
var2 = IntVar
Checkbutton(master, text = "Female", variable=var2).grid(row =4, sticky = W)
#third checkbox
var3 = IntVar
Checkbutton(master, text = "Other", variable=var3).grid(row =5, sticky = W)
#fourth checkbox
var4 = IntVar
Checkbutton(master, text = "Rather not say", variable=var4).grid(row =6, sticky = W)

#Aadhar card pin
Label(master, text = "Enter your Aadhar card pin").grid(row = 7)
e3 = Entry(master)
e3.grid(row = 7, column = 1)

mainloop()


