import tkinter as tk
from pynput.keyboard import *
import mouse

width = 400
height = 150
loopCond = True


# Dropdown menu options
options = [
    "right",
    "middle",
    "left"
]


def click():
    inputmillis = entryInt.get()
    mousebutton = chosenOption.get()
    if loopCond:
        mouse.click(button=mousebutton)
    root.after(inputmillis, click)


def start():
    global loopCond
    loopCond = True
    root.after(1000, click)


def stop():
    global loopCond
    loopCond = False


# draw the window and give it a min size
root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.minsize(width, height)
entryInt = tk.IntVar()

# draw the input field and place it
timer = tk.Label(root, text = "Time in ms").place(x = 30, y = 50)
entry = tk.Entry(root, textvariable=entryInt).place(x = 100, y = 50)

# draw the dropdown and place it
chosenOption = tk.StringVar()
chosenOption.set("left")
drop = tk.OptionMenu(root, chosenOption, *options)
drop.place(x=250, y=42)

# draw the buttons and place them
startbtn = tk.Button(root, text = "START", command = start, activebackground = "green", activeforeground = "blue").place(x = width/2 - 65, y = height-50)
stopbtn = tk.Button(root, text = "STOP", command = stop, activebackground = "green", activeforeground = "blue").place(x = width/2 + 55, y = height-50)


# start the main loop-di-loop
root.attributes('-topmost', True)
root.mainloop()
