import tkinter as tk
import osc_client

main = tk.Tk()
main.title
var = 0

# set up the page sections
pageNavTitle = tk.Label(main, text="Device", font="30")
pageNavTitle.grid(row=0, column=0, columnspan=2)

pageNav = tk.Frame(main)
pageNav.grid (row=0, column=0)
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
    tk.Label(pageWindow, text="Controls", font="30").grid(row=0, column=0, columnspan=3)
    buttonFaderUp1 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda m=1:volume_change(m)).grid(row=1, column=1)
    buttonFaderDown1 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda m=0:volume_change(m)).grid(row=2, column=1)
    buttonFaderUp2 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda m=1:volume_change(m)).grid(row=1, column=2)
    buttonFaderDown2 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda m=0:volume_change(m)).grid(row=2, column=2)
    buttonFaderUp2 = tk.Button(pageWindow, text="Fader +", font="20", command=lambda m=1:volume_change(m)).grid(row=1, column=3)
    buttonFaderDown2 = tk.Button(pageWindow, text="Fader -", font="20", command=lambda m=0:volume_change(m)).grid(row=2, column=3)


def page2():
    pageclear(pageWindow)
    tk.Label(pageWindow, text="Controls", font="30").grid(row=0, column=0, columnspan=2)
    buttonSequence1 = tk.Button(pageWindow, text="Sequence 1 GO", font="20").grid(row=1, column=0)
    buttonSequence2 = tk.Button(pageWindow, text="Sequence 2 GO", font="20").grid(row=1, column=1)
    buttonPause = tk.Button(pageWindow, text="Pause", font="20").grid(row=2, column=0)
    buttonOops = tk.Button(pageWindow, text="Oops", font="20").grid(row=2, column=1)

# volume control button
def volume_change(x):   
    global var
    if x >= 1:
        if var >= 100:
            var = 100
        else: var = var + 1
    elif var <= 0:
        var = 0
    else: var = var - 1
    print(var)
       
# page navigation buttons
pageNavButton1 = tk.Button(pageNav, text="Yamaha QL1", font ="30", command=page1).grid(row=1, column=0)
pageNavButton2 = tk.Button(pageNav, text="GrandMA3", font ="30", command=page2).grid(row=3, column=0)

page1()
main.mainloop()