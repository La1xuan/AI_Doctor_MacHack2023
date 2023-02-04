"""Learning Page: https://python-course.eu/tkinter/entry-widgets-in-tkinter.php"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time

def processData():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

gui = tk.Tk()
gui.geometry("500x800")
style = ttk.Style("minty")

tk.Label(gui, text="First Name").grid(row=0)
tk.Label(gui, text="Last Name").grid(row=1)

e1 = tk.Entry(gui)
e2 = tk.Entry(gui)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(gui, 
          text='Quit', 
          command=gui.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
b1 = ttk.Button(gui, text="Button 1", bootstyle=SUCCESS)
tk.Button(gui, text='Show', command=processData).grid(row=3, 
                                                               column=10, 
                                                               sticky=tk.W, 
                                                               pady=4)


gui.mainloop()
