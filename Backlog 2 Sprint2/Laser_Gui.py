import tkinter as tk
import laser_on
import laser_off

main = tk.Tk()
main.title("Laser GUI")
main.geometry('360x220')
fontL = "helvetica 14 bold"
fontM = "helvetica 12 bold"
fontS = "helvetica 12"

# set up page window
pageWindow = tk.Frame(main)
pageWindow.grid(row=0, column=1)

# clear page function
def pageclear(object):
    rdmshit = object.grid_slaves()
    for x in rdmshit:
        x.destroy()

# buttons on different menus
def page1():
    pageclear(pageWindow)
    tk.Label(pageWindow, text="Laser Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=3, pady=(0, 10))

    buttonLaser_On = tk.Button(pageWindow, text="Laser On", font=fontM, bg="black", fg="white", command=laser_On, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))
    buttonFLaser_Off = tk.Button(pageWindow, text="Laser Off", font=fontM, bg="black", fg="white", command=laser_Off, height= 2, width=5).grid(row=3, column=0, padx=(20, 0))

    buttonSlow = tk.Button(pageWindow, text="Slow BPM", font=fontM, bg="black", fg="white", command=laser_Slow, height= 2, width=5).grid(row=1, column=1, padx=(20, 0))
    buttonFast = tk.Button(pageWindow, text="-", font=fontM, bg="black", fg="white", command=laser_Fast, height= 2, width=5).grid(row=3, column=1, padx=(20, 0))

# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# volume control function
var1 = 0
var2 = 0
var3 = 0


def laser_On():
    laser_on

def laser_Off():
    laser_off
    
def laser_Slow():
    global var2

def laser_Fast():
    global var2

#default page on start-up
page1()
main.mainloop()
