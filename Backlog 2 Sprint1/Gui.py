import tkinter as tk

main = tk.Tk()
main.title("OSC Control GUI")
fontL = "helvetica 14 bold"
fontM = "helvetica 12 bold"
fontS = "helvetica 12"

# set up page sections
pageNav = tk.Frame(main)
pageNav.grid(row=0, column=0, sticky='N')


# set up page window
pageWindow = tk.Frame(main)
pageWindow.grid(row=0, column=1)

# buttons on different menus
def page1():

    tk.Label(pageWindow, text="Gui Page", font="helvetica 12 bold").grid(row=0, column=1, columnspan=3, pady=(0, 10))

    PlayStopBTN = tk.Button(pageWindow, text="Play/Stop", font=fontM, bg="black", fg="white", height= 2, width=8).grid(row=1, column=1, padx=(20, 0), pady=(20, 0))
    Marker1 = tk.Button(pageWindow, text="Marker1", font=fontM, bg="black", fg="white", height= 2, width=8).grid(row=1, column=3, padx=(0, 20), pady=(20, 0))
    Marker2 = tk.Button(pageWindow, text="Marker2", font=fontM, bg="black", fg="white", height= 2, width=8).grid(row=2, column=1, padx=(20, 0), pady=(20, 0))
    Marker3 = tk.Button(pageWindow, text="Marker3", font=fontM, bg="black", fg="white", height= 2, width=8).grid(row=2, column=3, padx=(0, 20), pady=(20, 0))
    Marker4 = tk.Button(pageWindow, text="Marker4", font=fontM, bg="black", fg="white", height= 2, width=8).grid(row=3, column=2, padx=(20, 0), pady=(20, 0))


# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# Yamaha QL1 button functions

def PlayStopBTN():
    print("Play/Stop Press")

def Marker1():
    print("marker1 Press")

def Marker2():
    print("marker2 Press")

def Marker3():
    print("marker3 Press")

def Marker4():

    print("marker4 Press")

#default page on start-up
page1()
main.mainloop()