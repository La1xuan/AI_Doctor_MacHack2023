"""Learning Page: https://python-course.eu/tkinter/entry-widgets-in-tkinter.php"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time

def processData(event=None):
    print("First Name: %s\nLast Name: " % (e1.get()))

gui = tk.Tk()
gui.geometry("500x500")
style = ttk.Style("minty")

#tk.Label(gui, text="First Name").grid(row=0)

e1 = tk.Entry(gui, width=50)
e1.insert(0, "Please describe your symptom")

e1.grid(row=0, column=1)
e1.place(x=115, y=455)

quitButton = ttk.Button(gui, text="End Chat", bootstyle=(INFO, OUTLINE), command=gui.quit)
quitButton.place(x=25, y=450)

sentButton = ttk.Button(gui, text="|>", bootstyle=(SUCCESS, OUTLINE), command=processData)
sentButton.place(x=440, y=450)

gui.bind('<Return>', processData)

gui.mainloop()
