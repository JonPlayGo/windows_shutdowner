import os
from tkinter import *
import re
import tkinter as tk
import sys

root = Tk()
root.geometry("210x100")
root.title("shutdowner")
root.resizable(width=False, height=False)

def is_valid_input(input_value):
    return re.match("^[0-9]*$", input_value) is not None
reg = root.register(is_valid_input) 

def get_shutdown_time():
    global hours,result,minutes,seconds
    hours = int(hour_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    result = str(hours * 3600 + minutes * 60 + seconds)
    print("Общее количество секунд: ", result)

def input_config():
    get_shutdown_time()
    with open("config.txt", "w") as file:
        text = f"{str(hours)} {str(minutes)} {str(seconds)}"
        file.write(text)

def get_config():
    with open("config.txt", "r") as file:
        text = file.read()
        global hours,minutes,seconds
        hours,minutes,seconds = text.split()

def shutdown_start():
    get_shutdown_time()
    if result == "0":
        print("sdfsfsdf")
    else:
        print("ok")
        os.system(f"shutdown -s -t {result}")

def shutdown_cancel():
    os.system("shutdown -a")

try:
    get_config()
except:
    hours,minutes,seconds = "00","00","00"

hour_label = Label(root, text="hours")
hour_label.place(x=10,y=4)

minutes_label = Label(root, text="minutes")
minutes_label.place(x=60,y=4)

seconds_label = Label(root, text="seconds")
seconds_label.place(x=110,y=4)

hour_entry = Entry(root,width=6, validate="key", validatecommand=(reg, '%P'))
hour_entry.insert(0, hours)
hour_entry.place(x=10,y=24)

minutes_entry = Entry(root,width=6, validate="key", validatecommand=(reg, '%P'))
minutes_entry.insert(0, minutes)
minutes_entry.place(x=60,y=24)

seconds_entry = Entry(root,width=6, validate="key", validatecommand=(reg, '%P'))
seconds_entry.insert(0, seconds)
seconds_entry.place(x=110,y=24)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

config_button_image = tk.PhotoImage(file=resource_path("clip.png"))
config_button = Button(root,width=15,height=15,image=config_button_image,command=input_config)
config_button.place(x=180,y=24)

shutdown_button = Button(root,text="shutdown",width=10,height=1,command=shutdown_start)
shutdown_button.place(x=10,y=54)

shutdown_cancel_button = Button(root,text="shutdown cancel",width=13,height=1,command=shutdown_cancel)
shutdown_cancel_button.place(x=100,y=54)

root.mainloop()