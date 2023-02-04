import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import time

def processData(event=None):
    beforeStart.after(0, beforeStart.destroy())
    userInput = e1.get()
    chat.insert(END, '(You):\n', '(You)')
    chat.insert(END, userInput, 'yourword')
    chat.insert(END, '\n')
    chat.insert(END, 'Doc:\n', 'Doc')
    chat.insert(END, AISolution(userInput), 'Docword')
    chat.insert(END, '\n')
    e1.delete(0, END)

def AISolution(inputVal):

    return "TODO: Doc returned that " + inputVal

gui = tk.Tk()
gui.title('AI Doctor')
gui.geometry("500x500")
style = ttk.Style("minty")


e1 = tk.Entry(gui, width=50)
e1.insert(0, "")

e1.grid(row=0, column=1)
e1.place(x=115, y=455)

quitButton = ttk.Button(gui, text="End Chat", bootstyle=(INFO, OUTLINE), command=gui.quit)
quitButton.place(x=25, y=450)

sentButton = ttk.Button(gui, text="|>", bootstyle=(SUCCESS, OUTLINE), command=processData)
sentButton.place(x=440, y=450)

chat = ScrolledText(gui, padding=30, height=25, width=70, autohide=True)
chat.place(x=0, y=0)
chat.tag_config('(You)', foreground='blue')
chat.tag_config('yourword', foreground='grey')
chat.tag_config('Doc', foreground='green')
chat.tag_config('Docword', foreground='black')

beforeStart = tk.Label(gui, text="Please describe your symptom below:")
beforeStart.place(x=120, y=425)
gui.bind('<Return>', processData)

gui.mainloop()
