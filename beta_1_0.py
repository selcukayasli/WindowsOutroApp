import winsound
from tkinter import*
import os

def shutdown():
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    return os.system("shutdown /s /t 15")
    

master = Tk()
master.configure(bg='blue')
Button(master, text='START', command=shutdown).grid(row=0)

mainloop()