import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
chars = "abcdefghijklmnopqrstuv@wxyzABCDEFGHIJ#KLMNOPQRSTUVWXYZ1234567890@#$%^&*!(`)"
def pas(len):
    password1 = ""
    for  lenw in range(0,len):
        password = random.choice(chars)
        password1 = password1 + password
    return password1+" "

# this is a function to get the user input from the text input box
def getInputBoxValue():
    if tInput.get() != "":
        try:
            userInput = int(tInput.get())
            return userInput        
        except ValueError:
            userInput = None
            print ("What length password to be Invalid input")
            return userInput


# this is a function to get the user input from the text input box
def getInputBoxValuetwo():
    if tlnputtwo.get() != "":
        try:
            userInput = int(tlnputtwo.get())
            return userInput
        except ValueError:
            userInput = int(1)
            print("How many passwords would you like text Invalid input")
            return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    if  getInputBoxValue() != None:
        password_len = getInputBoxValue()
        if getInputBoxValuetwo() == None:
            password_count = 1
        else:
            password_count = getInputBoxValuetwo()
        #print(type(password_count))
        passs = []
        for n_of_run in range(0,password_count):
            passs.append(pas(password_len))
            tInout.insert(INSERT,passs)
        print(passs)
        
# this is a function to get the user input from the text input box
def getInputBoxValueout():
	userInput = tInout.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('764x536')
root.configure(background='#F0F8FF')
root.title('Password generator')


# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=324, y=177)


# This is the section of code which creates a text input box
tlnputtwo=Entry(root)
tlnputtwo.place(x=324, y=215)


# This is the section of code which creates a button
Button(root, text='Generator', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=335, y=257)


# This is the section of code which creates the a label
Label(root, text='What length password to be:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=112, y=176)


# This is the section of code which creates the a label
Label(root, text='How many passwords would you like:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=52, y=215)


# This is the section of code which creates a text input box
tInout=Text(root)
tInout.place(x=223, y=300,width=282,height=200)



root.mainloop()
