import tkinter as tk
import RPi.GPIO as GPIO
import time
import Slow_Creep
import Fast_Violin

main = tk.Tk()
main.title("Laser GUI")
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

    buttonLaserOn = tk.Button(pageWindow, text="Laser On", font=fontM, bg="black", fg="white", command=laser_on).grid(row=1, column=0, padx=(20, 0))
    buttonLaserOff = tk.Button(pageWindow, text="Laser Off", font=fontM, bg="black", fg="white", command=laser_off).grid(row=1, column=1, padx=(20, 0))
    buttonLaserSlow = tk.Button(pageWindow, text="Laser Slow", font=fontM, bg="black", fg="white", command=laser_Slow).grid(row=2, column=0, padx=(20, 0))
    buttonLaserFast = tk.Button(pageWindow, text="Laser Fast", font=fontM, bg="black", fg="white", command=laser_Fast).grid(row=2, column=1, padx=(20, 0))

# def page2():
#     pageclear(pageWindow)
#     button_active(pageNavButton2)
#     button_inactive(pageNavButton1)
#     tk.Label(pageWindow, text="Page 2", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))

# page navigation buttons
# pageNavButton1 = tk.Button(pageNav, text="Laser", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)
# pageNavButton1.grid(row=1, column=0)
# pageNavButton2 = tk.Button(pageNav, text="Page 2", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)
# pageNavButton2.grid(row=2, column=0)

# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# laser button functions
def laser_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    GPIO.output(21, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    GPIO.output(21, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()
    
def laser_Slow():
    print("Laser slow")
    counter = Slow_Creep.counter(bpm, duration)
    counter

def laser_Fast():
    print("Laser fast")
    counter = Fast_Violin.counter(bpm, duration)
    counter

#default page on start-up
page1()
main.mainloop()
