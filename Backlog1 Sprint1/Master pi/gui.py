import tkinter as tk
import osc_client_Grandma3
import osc_client_Yamaha

main = tk.Tk()
main.title("OSC Control GUI")
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
    button_active(pageNavButton1)
    button_inactive(pageNavButton2)
    tk.Label(pageWindow, text="Yamaha QL1 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=3, pady=(0, 10))
    tk.Label(pageWindow, text="Fader 1", font="30").grid(row=4, column=0, padx=(20, 0), pady=(10, 0))
    tk.Label(pageWindow, text="Fader 2", font="30").grid(row=4, column=1, padx=(20, 0), pady=(10, 0))
    tk.Label(pageWindow, text="Fader 3", font="30").grid(row=4, column=2, padx=(20, 0), pady=(10, 0))

    buttonFaderUp1 = tk.Button(pageWindow, text="+", font=fontM, bg="black", fg="white", command=fader1volumeUp, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))
    buttonFaderDown1 = tk.Button(pageWindow, text="-", font=fontM, bg="black", fg="white", command=fader1volumedown, height= 2, width=5).grid(row=3, column=0, padx=(20, 0))
    global faderdisplay1
    faderdisplay1 = tk.Label(pageWindow, text=var1, font=fontS)
    faderdisplay1.grid(row=2, column=0, padx=(20, 0), pady=(5, 5))

    buttonFaderUp2 = tk.Button(pageWindow, text="+", font=fontM, bg="black", fg="white", command=fader2volumeUp, height= 2, width=5).grid(row=1, column=1, padx=(20, 0))
    buttonFaderDown2 = tk.Button(pageWindow, text="-", font=fontM, bg="black", fg="white", command=fader2volumedown, height= 2, width=5).grid(row=3, column=1, padx=(20, 0))
    global faderdisplay2
    faderdisplay2 = tk.Label(pageWindow, text=var2, font=fontS)
    faderdisplay2.grid(row=2, column=1, padx=(20, 0), pady=(5, 5))
    
    buttonFaderUp3 = tk.Button(pageWindow, text="+", font=fontM, bg="black", fg="white", command=fader3volumeUp, height= 2, width=5).grid(row=1, column=2 ,padx=(20, 0))
    buttonFaderDown3 = tk.Button(pageWindow, text="-", font=fontM, bg="black", fg="white", command=fader3volumedown, height= 2, width=5).grid(row=3, column=2, padx=(20, 0))
    global faderdisplay3
    faderdisplay3 = tk.Label(pageWindow, text=var3, font=fontS)
    faderdisplay3.grid(row=2, column=2, padx=(20, 0), pady=(5, 5))

def page2():
    pageclear(pageWindow)
    button_active(pageNavButton2)
    button_inactive(pageNavButton1)
    tk.Label(pageWindow, text="GrandMA3 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))
    buttonSequence1 = tk.Button(pageWindow, text="Sequence \n1 GO", font="20", bg="black", fg="white", command=sequence1, height= 2, width=10).grid(row=1, column=0, padx=(20, 0))
    buttonSequence2 = tk.Button(pageWindow, text="Sequence \n2 GO", font="20", bg="black", fg="white", command=sequence2, height= 2, width=10).grid(row=1, column=1)
    buttonPause = tk.Button(pageWindow, text="Pause", font="20", bg="black", fg="white", command=pause, height= 2, width=10).grid(row=2, column=0, padx=(20, 0))
    buttonOops = tk.Button(pageWindow, text="Oops", font="20", bg="black", fg="white", command=oops, height= 2, width=10).grid(row=2, column=1)

# page navigation buttons
pageNavButton1 = tk.Button(pageNav, text="Yamaha QL1", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)
pageNavButton1.grid(row=1, column=0)
pageNavButton2 = tk.Button(pageNav, text="GrandMA3", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)
pageNavButton2.grid(row=2, column=0)

# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# volume control function
var1 = 0
var2 = 0
var3 = 0

# Yamaha QL1 button functions
def fader1volumeUp():
    global var1
    if var1 >= 100:
        var1 = 100
    else: var1 = var1 + 10
    print(var1)
    osc_client_Yamaha.yamahafader1Up()
    faderdisplay1.config(text=var1)

def fader1volumedown():
    global var1
    if var1 <= 0:
        var1 = 0
    else: var1 = var1 - 10
    print(var1)
    osc_client_Yamaha.yamahafader1Down()
    faderdisplay1.config(text=var1)
    
def fader2volumeUp():
    global var2
    if var2 >= 100:
        var2 = 100
    else: var2 = var2 + 10
    print(var2)
    osc_client_Yamaha.yamahafader2Up()
    faderdisplay2.config(text=var2)

def fader2volumedown():
    global var2
    if var2 <= 0:
        var2 = 0
    else: var2 = var2 - 10
    print(var2)
    osc_client_Yamaha.yamahafader2Down()
    faderdisplay2.config(text=var2)

def fader3volumeUp():
    global var3
    if var3 >= 100:
        var3 = 100
    else: var3 = var3 + 10
    print(var3)
    osc_client_Yamaha.yamahafader3Up()
    faderdisplay3.config(text=var3)

def fader3volumedown():
    global var3
    if var3 <= 0:
        var3 = 0
    else: var3 = var3 - 10
    print(var3)
    osc_client_Yamaha.yamahafader3Down()
    faderdisplay3.config(text=var3)

# GrandMA3 button functions
def sequence1():
    print("Sequence 1 pressed")
    osc_client_Grandma3.sequence1_osc()

def sequence2():
    print("Sequence 2 pressed")
    osc_client_Grandma3.sequence2_osc()

def pause():
    print("Pause pressed")
    osc_client_Grandma3.pause_osc()

def oops():
    print("Oops pressed")
    osc_client_Grandma3.oops_osc()

#default page on start-up
page1()
main.mainloop()
