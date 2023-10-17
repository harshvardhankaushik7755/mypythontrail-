from tkinter import *
import pyttsx3

root = Tk()
root.title("I will anaylyze for you")
root.geometry("800x500")

def talk():

    engine = pyttsx3.init()
    engine.runAndWait()
    engine.say("yoo type here")
my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)
my_button = Button(root, text="Speak", command=talk)

root.mainloop()