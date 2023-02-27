#Repository Owner = ABleasdale1
#####################################
from tkinter import *
import sys
import os
import time
import random as rand
from characters import Enemies, Hero, Item
from game import menu, Start, forestWalks, path1, path2, path3, store, lokiFight, helFight, freyaFight
#####################################
root = Tk()
root.title('Norse Game')
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.configure(background="grey")
#####################################
os.system('cls') 
#####################################
def myClick():
    myLabel=Label(root, Start())
    myLabel.pack
def myClick1():
    myLabel=Label(root, )
    myLabel.pack
def myClick2():
    myLabel=Label(root, sys.exit())
    myLabel.pack

myButton=Button(root, text="Start", command=myClick, bg='black', fg='white', height='2', width='15')
myButton.grid(row=0, column=0)

myButton1=Button(root, text="Instructions", command=myClick1, bg='black', fg='white', height='2', width='15')
myButton1.grid(row=0, column=1)

myButton2=Button(root, text="Exit", command=myClick2, bg='black', fg='white', height='2', width='5')
myButton2.grid(row=5, column=5)

root.mainloop()