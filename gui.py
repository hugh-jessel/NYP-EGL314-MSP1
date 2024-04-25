import tkinter as tk
import osc_client_Grandma3
import osc_client_Yamaha

main = tk.Tk()
main.title

# set up page sections
pageNav = tk.Frame(main)
pageNav.grid(row=0, column=0)
pageNavTitle = tk.Label(pageNav, text="Devices", font="40").grid(row=0, column=0)

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
    tk.Label(pageWindow, text="Controls", font="40").grid(row=0, column=0, columnspan=3)
    tk.Label(pageWindow, text="Fader 1", font="30").grid(row=1, column=0, padx=(20, 0))
    tk.Label(pageWindow, text="Fader 2", font="30").grid(row=1, column=1, padx=(20, 0))
    tk.Label(pageWindow, text="Fader 3", font="30").grid(row=1, column=2, padx=(20, 0))
    buttonFaderUp1 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda x=1:volume_change1(x), height= 2, width=8).grid(row=2, column=0, padx=(20, 0))
    buttonFaderDown1 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda x=0:volume_change1(x), height= 2, width=8).grid(row=4, column=0, padx=(20, 0))
    buttonFaderUp2 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda x=1:volume_change2(x), height= 2, width=8).grid(row=2, column=1, padx=(20, 0))
    buttonFaderDown2 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda x=0:volume_change2(x), height= 2, width=8).grid(row=4, column=1, padx=(20, 0))
    buttonFaderUp2 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda x=1:volume_change3(x), height= 2, width=8).grid(row=2, column=2 ,padx=(20, 0))
    buttonFaderDown2 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda x=0:volume_change3(x), height= 2, width=8).grid(row=4, column=2, padx=(20, 0))

def page2():
    pageclear(pageWindow)
    tk.Label(pageWindow, text="Controls", font="30").grid(row=0, column=0, columnspan=2)
    buttonSequence1 = tk.Button(pageWindow, text="Sequence 1 GO", font="20", command=sequence1, height= 2, width=15).grid(row=1, column=0, padx=(20, 0))
    buttonSequence2 = tk.Button(pageWindow, text="Sequence 2 GO", font="20", command=sequence2, height= 2, width=15).grid(row=1, column=1)
    buttonPause = tk.Button(pageWindow, text="Pause", font="20", command=pause, height= 2, width=8).grid(row=2, column=0, padx=(20, 0))
    buttonOops = tk.Button(pageWindow, text="Oops", font="20", command=oops, height= 2, width=8).grid(row=2, column=1)

# volume control function
var1 = 50
var2 = 50
var3 = 50

def volume_change1(x):   
    global var1
    if x >= 1:
        if var1 >= 100:
            var1 = 100
        else: var1 = var1 + 1
        osc_client_Yamaha.yamahafader1Up()
    elif var1 <= 0:
        var1 = 0
    else: var1 = var1 - 1
    osc_client_Yamaha.yamahafader1Down()
    print(var1)
    

def volume_change2(x):   
    global var2
    if x >= 1:
        if var2 >= 100:
            var2 = 100
        else: var2 = var2 + 1
        osc_client_Yamaha.yamahafader2Up()
    elif var2 <= 0:
        var2 = 0
    else: var2 = var2 - 1
    osc_client_Yamaha.yamahafader2Down()
    print(var2)

def volume_change3(x):   
    global var3
    if x >= 1:
        if var3 >= 100:
            var3 = 100
        else: var3 = var3 + 1
        osc_client_Yamaha.yamahafader3Up()
    elif var3 <= 0:
        var3 = 0
    else: var3 = var3 - 1
    osc_client_Yamaha.yamahafader3Down()
    print(var3)
       
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

# page navigation buttons
pageNavButton1 = tk.Button(pageNav, text="Yamaha QL1", font ="30", command=page1, height= 2, width=10).grid(row=1, column=0)
pageNavButton2 = tk.Button(pageNav, text="GrandMA3", font ="30", command=page2, height= 2, width=10).grid(row=3, column=0)

page1()
main.mainloop()