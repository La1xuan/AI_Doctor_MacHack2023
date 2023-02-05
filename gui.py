import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import pandas as pd
from src.main import diagnose
import time

def processData(event=None):
    if finished:
        return
    beforeStart.after(0, beforeStart.destroy())
    userInput = e1.get()
    chat.insert(END, '(You):\n', '(You)')
    chat.insert(END, userInput, 'yourword')
    chat.insert(END, '\n')
    chat.see(tk.END)
    checkingSymptoms()
    e1.delete(0, END)

def AISolution():
    global finished
    finished = True
    result = diagnose(record)
    chat.insert(END, 'Doc:\n', 'Doc')
    chat.insert(END, "Ok. It seems you've got " + str(result), 'Docword')
    chat.insert(END, '\n')
    chat.see(tk.END)
    return 
    
def checkingSymptoms():
    if finished:
        return
    global loc
    for i in range(len(record)):
        if record[i] == -1:
            chat.insert(END, 'Doc:\n', 'Doc')
            chat.insert(END, "Got it, did you feel " + symptoms[i] + " recently?", 'Docword')
            chat.insert(END, '\n')
            chat.see(tk.END)
            YesButton = ttk.Button(gui, text="Yes I have that feeling", bootstyle=SUCCESS, command=makeTrue)
            YesButton.place(x=100, y=415)
            NoButton = ttk.Button(gui, text="No, I don't have that feeling", bootstyle=FLAT, command=makeFalse)
            NoButton.place(x=250, y=415)
            loc = i
            return
    AISolution()
    

            
def makeTrue():
    if finished:
        return
    chat.insert(END, '(You):\n', '(You)')
    chat.insert(END, "Yes I have that feeling", 'yourword')
    chat.insert(END, '\n')
    chat.see(tk.END)
    record[loc] = 1
    checkingSymptoms()
def makeFalse():
    if finished:
        return
    chat.insert(END, '(You):\n', '(You)')
    chat.insert(END, "No, I don't have that feeling", 'yourword')
    chat.insert(END, '\n')
    chat.see(tk.END)
    record[loc] = 0
    checkingSymptoms()
    

symptoms = ['arm pain', 'back pain', 'leg pain', 'ankle pain', 'inner thigh pain', 'back thigh pain', 'shoulder pain', 'tendon pain', 'swelling','headache', 'weakness', 'stiffness', 'difficulty moving/straightening ','nausea', 'bruising ', 'tenderness', 'numbness','difficulty putting weight on', 'dizziness or blurry vision', 'spasms','elbow pain', 'difficulty balancing ', 'light and sound irritation',' Trouble controlling bowels or bladder', 'injury']
record = []
cur = 0
loc = 0
finished = False
for _ in symptoms:
    record.append(-1)
print(symptoms)
print(record)
print(len(symptoms))
print(len(record))
gui = tk.Tk()
gui.title('HealAI')
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

chat = ScrolledText(gui, padding=30, height=24, width=70, autohide=True)
chat.place(x=0, y=0)
chat.tag_config('(You)', foreground='blue')
chat.tag_config('yourword', foreground='grey')
chat.tag_config('Doc', foreground='green')
chat.tag_config('Docword', foreground='black')



beforeStart = tk.Label(gui, text="Please describe your symptom below:")
beforeStart.place(x=120, y=425)



gui.bind('<Return>', processData)

gui.mainloop()
