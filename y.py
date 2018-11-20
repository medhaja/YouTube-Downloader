#	Coded by Medhaja H L on 06-07-2018
#	this script is coded to run on Python 3.6.1 |Anaconda 4.4.0 (64-bit) if you have python is 2.7 or Lower,this script doesnt work unless
#	some minor changes
#	Tested on Windows 10 64-bit machine

import subprocess
import os
import sys
from tkinter import *
from tkinter import messagebox
import threading


def click():
    entered_text= mystring.get()
    if (entered_text == ""):
        messagebox.showerror("Error", "PLEASE ENTER THE CORRECT ADDRESS OF THE VIDEO TO BE DOWNLOADED")
    print(entered_text)
    youtubeFuntion(entered_text)
    return

def youtubeFuntion(x):
    command=("youtube-dl "+str(x))
    if (command == "youtube-dl "):
        messagebox.showerror("Error", "PLEASE ENTER THE CORRECT IMAGE NAME WITH EXTENTION")
    print (command)
    y=subprocess.call(command, shell=True)
    #print("the output of y")
    #print(y)	
    #Entry(window, text=str(y)).grid(row=40, column=1)
    return


def playList():
    entered_text= mystring.get()
    if (entered_text == ""):
        messagebox.showerror("Error", "PLEASE ENTER THE CORRECT ADDRESS OF THE VIDEO TO BE DOWNLOADED")
    command = ("youtube-dl --yes-playlist --audio-format best --audio-quality 0 " + str(entered_text))
    print(command)
    y = subprocess.call(command, shell=True)
    #Entry(window, text="THE VIDEO IS BEING DOWNLOADED" % (y)).grid(row=40, column=1)
    return

def only_audio():
    entered_text= mystring.get()
    if (entered_text == ""):
        messagebox.showerror("Error", "PLEASE ENTER THE CORRECT ADDRESS OF THE VIDEO TO BE DOWNLOADED")
    command = ("youtube-dl -f bestaudio " + str(entered_text))
    print(command)
    y = subprocess.call(command, shell=True)
    #Entry(window, text="THE VIDEO IS BEING DOWNLOADED" % (y)).grid(row=40, column=1)
    return


def playList1():
    t = threading.Thread(target=playList)
    t.start()

def only_audio1():
    t = threading.Thread(target=only_audio)
    t.start()
def click1():
    t = threading.Thread(target=click)
    t.start()

window = Tk()
window.title("Youtube Videos Download")
window.geometry("1300x1300")
mystring=StringVar()
w = Label(window, text="Enter the address:",bg="blue",fg="white",font="none 12 bold").grid(row=4,column=0)
textentry=Entry(window,textvariable=mystring).grid(row=4,column=1)
button=Button(window,text="DOWNLOAD!!",width=23,command=click1).grid(row=6,column=0)
button2=Button(window,text="EXIT!!",width=17,command=window.destroy).grid(row=15,column=12)
button3=Button(window,text="DOWNLOAD THE PLAYLIST!!",width=24,command=playList1).grid(row=6,column=1)
button4=Button(window,text="DOWNLOAD ONLY THE AUDIO!!",width=24,command=only_audio1).grid(row=6,column=12)
window.mainloop()
