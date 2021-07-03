import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import webbrowser

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*!(`)"
def pas(len):
    password1 = ""
    for  lenw in range(0,len):
        password = random.choice(chars)
        password1 = password1 + password
    return password1

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
            return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    if  getInputBoxValue() != None and getInputBoxValue() != 0:
        password_len = getInputBoxValue()
        if getInputBoxValuetwo() == None or getInputBoxValuetwo() == 0:
            password_count = 1
        else:
            password_count = getInputBoxValuetwo()
        #print(type(password_count))
        passs = []
        for n_of_run in range(0,password_count):
            #passs.append(pas(password_len)+ '\n')
            tInout.config(state=tk.NORMAL)
            tInout.insert(END,pas(password_len)+'\n')
            tInout.config(state=tk.DISABLED)
        #print(passs)
        
# this is a function to get the user input from the text input box
def getInputBoxValueout():
	userInput = tInout.get()
	return userInput

def callback(url):
    webbrowser.open_new(url)



root = Tk()

# This is the section of code which creates the main window
root.geometry('430x450')
root.configure(background='#0f7699')
root.title('Password generator')

# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=300, y=50,width=125)

# This is the section of code which creates a text input box
tlnputtwo=Entry(root)
tlnputtwo.place(x=300, y=75,width=125)


# This is the section of code which creates a button
Button(root, text='Generator', bg='#ffe161', fg='#0f7699', font=('Cooper', 12, 'normal'), command=btnClickFunction).place(x=5, y=115,width=420,height=40)
Label(root, text='Password generator', bg='#0f7699', fg='#ffffff', font=('Goudy Stout', 14, 'normal')).place(x=5, y=5)


# This is the section of code which creates the a label
Label(root, text='What length password to be:', bg='#0f7699', fg='#ffffff', font=('Arial Rounded MT', 12, 'normal')).place(x=5, y=50)


# This is the section of code which creates the a label
Label(root, text='How many passwords would you like:', bg='#0f7699', fg='#ffffff', font=('Arial Rounded MT', 12, 'normal')).place(x=5, y=75)


# This is the section of code which creates a text input box
tInout=Text(root,state='normal')
tInout.place(x=5, y=170,width=420,height=200)

Label(root, text='GPL-3.0 License', bg='#0f7699', fg='#ffffff', font=('arial', 12, 'normal')).place(x=5, y=400)
link2 = Label(root, text=r'alij.cc', bg='#0f7699', fg='#ffffff', font=('arial', 12, 'normal'), cursor="hand2")

#link2.place(relx=315, rely=400)
link2.place(x = 350 ,y = 400)
#link2.pack()
link2.bind("<Button-1>", lambda e: callback("https://www.alij.cc"))
Button(root, text='QUIT', bg='#ffe161', fg='#0f7699', font=('arial', 12, 'normal'), command=quit).place(x=200, y=400,width=50)

root.mainloop()
