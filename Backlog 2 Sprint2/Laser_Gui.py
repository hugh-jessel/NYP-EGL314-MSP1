import tkinter as tk
import laser_on
import laser_off
import RPi.GPIO as GPIO
import time

main = tk.Tk()
main.title("Laser GUI")
main.geometry('360x220')
fontL = "helvetica 14 bold"
fontM = "helvetica 12 bold"
fontS = "helvetica 12"

# set up page sections
pageNav = tk.Frame(main)
pageNav.grid(row=0, column=0, sticky='N')
pageNavTitle = tk.Label(pageNav, text="Devices", font="helvetica 12 bold").grid(row=0, column=0)

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

    buttonLaserOn = tk.Button(pageWindow, text="Laser On", font=fontM, bg="black", fg="white", command=laser_on, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))
    buttonLaserOff = tk.Button(pageWindow, text="Laser On", font=fontM, bg="black", fg="white", command=laser_off, height= 2, width=5).grid(row=1, column=1, padx=(20, 0))
    buttonLaserSlow = tk.Button(pageWindow, text="Laser Slow", font=fontM, bg="black", fg="white", command=laser_Slow, height= 2, width=5).grid(row=2, column=0, padx=(20, 0))
    buttonLaserFast = tk.Button(pageWindow, text="Laser Fast", font=fontM, bg="black", fg="white", command=laser_Fast, height= 2, width=5).grid(row=2, column=1, padx=(20, 0))

def page2():
    pageclear(pageWindow)
    button_active(pageNavButton2)
    button_inactive(pageNavButton1)
    tk.Label(pageWindow, text="Page 2", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))

# page navigation buttons
pageNavButton1 = tk.Button(pageNav, text="Laser", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)
pageNavButton1.grid(row=1, column=0)
pageNavButton2 = tk.Button(pageNav, text="Page 2", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)
pageNavButton2.grid(row=2, column=0)

# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# laser button functions
def laser_Slow():
    print("Laser slow")

def laser_Fast():
    print("Laser fast")

#default page on start-up
page1()
main.mainloop()
