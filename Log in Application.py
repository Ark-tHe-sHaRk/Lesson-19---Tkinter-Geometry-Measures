# Importing Necessary Libraries
from tkinter import *

# Create a Window
root = Tk()
root.title('Log In')
root.geometry('400x400')

# Create a frame to organize elements together
frame = Frame(master=root, height=200, width=360, bg='#d0efff')
frame.place(x=20, y=0)  # Place the frame

# Adding widgets and labels
lbl1 = Label(frame, text='Full Name', bg='#3895D3', fg='white', width=12)
lbl1.place(x=20, y=20)

name_entry = Entry(frame)
name_entry.place(x=150, y=20)

lbl2 = Label(frame, text='Email ID', bg='#3895D3', fg='white', width=12)
lbl2.place(x=20, y=80)

email_entry = Entry(frame)
email_entry.place(x=150, y=80)

lbl3 = Label(frame, text='Password', bg='#3895D3', fg='white', width=12)
lbl3.place(x=20, y=140)

pass_entry = Entry(frame, show='unknwon')
pass_entry.place(x=150, y=140)

# Function to display message
def display():
    name = name_entry.get()
    greet = 'Hey ' + name
    message = '\nCongratulations for your new account. It has been successfully created.'
    textbox.insert(END, greet)
    textbox.insert(END, message)

# Text box to display the message
textbox = Text(root, bg='#BEBEBE', fg='black', height=5, width=40)  # Added dimensions
textbox.place(x=20, y=250)

# Adding a button, when pressed, message will be displayed
btn = Button(root, text='Create Account', command=display, bg='red')
btn.place(x=130, y=210)  # Corrected placement

# Start the main event loop
root.mainloop()
