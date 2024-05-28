import tkinter as tk
import osc_client_Grandma3
import osc_client_LISA

main = tk.Tk()
main.title("OSC Control GUI")
main.geometry("450x300")
fontL = "helvetica 14 bold"
fontM = "helvetica 12 bold"
fontS = "helvetica 12"

# set up page sections
pageNav = tk.Frame(main)
pageNav.grid(row=0, column=0, sticky='N')
pageNavTitle = tk.Label(pageNav, text="Devices", font="helvetica 12 bold").grid(row=0, column=0, pady=(0, 10))

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

    tk.Label(pageWindow, text="L-ISA Snapshots", font="helvetica 12 bold").grid(row=0, column=0, columnspan=5, pady=(0, 10))

    buttonSnapshot1 = tk.Button(pageWindow, text="1", font=fontS, bg="black", fg="white", command=snapshot1, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))
    buttonSnapshot2 = tk.Button(pageWindow, text="2", font=fontS, bg="black", fg="white", command=snapshot2, height= 2, width=5).grid(row=1, column=1, padx=(0, 0))
    buttonSnapshot3 = tk.Button(pageWindow, text="3", font=fontS, bg="black", fg="white", command=snapshot3, height= 2, width=5).grid(row=1, column=2, padx=(0, 0))
    buttonSnapshot4 = tk.Button(pageWindow, text="4", font=fontS, bg="black", fg="white", command=snapshot4, height= 2, width=5).grid(row=1, column=3, padx=(0, 0))
    buttonSnapshot5 = tk.Button(pageWindow, text="5", font=fontS, bg="black", fg="white", command=snapshot5, height= 2, width=5).grid(row=1, column=4, padx=(0, 20))
    buttonSnapshot6 = tk.Button(pageWindow, text="6", font=fontS, bg="black", fg="white", command=snapshot6, height= 2, width=5).grid(row=2, column=0, padx=(20, 0))
    buttonSnapshot7 = tk.Button(pageWindow, text="7", font=fontS, bg="black", fg="white", command=snapshot7, height= 2, width=5).grid(row=2, column=1, padx=(0, 0))
    buttonSnapshot8 = tk.Button(pageWindow, text="8", font=fontS, bg="black", fg="white", command=snapshot8, height= 2, width=5).grid(row=2, column=2, padx=(0, 0))
    buttonSnapshot9 = tk.Button(pageWindow, text="9", font=fontS, bg="black", fg="white", command=snapshot9, height= 2, width=5).grid(row=2, column=3, padx=(0, 0))
    buttonSnapshot10 = tk.Button(pageWindow, text="10", font=fontS, bg="black", fg="white", command=snapshot10, height= 2, width=5).grid(row=2, column=4, padx=(0, 20))

def page2():
    pageclear(pageWindow)
    button_active(pageNavButton2)
    button_inactive(pageNavButton1)

    tk.Label(pageWindow, text="GrandMA3 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))

    buttonSequence1 = tk.Button(pageWindow, text="Spotlight", font=fontS, bg="black", fg="white", command=sequence1, height= 2, width=12).grid(row=1, column=0, padx=(20, 0))
    buttonSequence2 = tk.Button(pageWindow, text="Stage Failed", font=fontS, bg="black", fg="white", command=sequence2, height= 2, width=12).grid(row=2, column=0, padx=(20, 0))
    buttonSequence3 = tk.Button(pageWindow, text="Stage Passed", font=fontS, bg="black", fg="white", command=sequence3, height= 2, width=12).grid(row=3, column=0, padx=(20, 0))
    buttonSequence4 = tk.Button(pageWindow, text="Station Marker", font=fontS, bg="black", fg="white", command=sequence4, height= 2, width=12).grid(row=4, column=0, padx=(20, 0))
    buttonSequence5 = tk.Button(pageWindow, text="Game Light", font=fontS, bg="black", fg="white", command=sequence5, height= 2, width=12).grid(row=5, column=0, padx=(20, 0))
    buttonPause = tk.Button(pageWindow, text="Pause", font=fontS, bg="black", fg="white", command=pause, height= 2, width=10).grid(row=1, column=1, padx=(20, 20))
    buttonOops = tk.Button(pageWindow, text="Oops", font=fontS, bg="black", fg="white", command=oops, height= 2, width=10).grid(row=2, column=1, padx=(20, 20))

# page navigation buttons
pageNavButton1 = tk.Button(pageNav, text="L-ISA Studio", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)
pageNavButton1.grid(row=1, column=0, padx=(20, 0))
pageNavButton2 = tk.Button(pageNav, text="GrandMA3", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)
pageNavButton2.grid(row=2, column=0, padx=(20, 0))

# button colour change on press
def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

# L-ISA button functions
def snapshot1():
    print("Snapshot 1 pressed")
    osc_client_LISA.snapshot1_osc()

def snapshot2():
    print("Snapshot 2 pressed")
    osc_client_LISA.snapshot2_osc()

def snapshot3():
    print("Snapshot 3 pressed")
    osc_client_LISA.snapshot3_osc()

def snapshot4():
    print("Snapshot 4 pressed")
    osc_client_LISA.snapshot4_osc()

def snapshot5():
    print("Snapshot 5 pressed")
    osc_client_LISA.snapshot5_osc()

def snapshot6():
    print("Snapshot 6 pressed")
    osc_client_LISA.snapshot6_osc()

def snapshot7():
    print("Snapshot 7 pressed")
    osc_client_LISA.snapshot7_osc()

def snapshot8():
    print("Snapshot 8 pressed")
    osc_client_LISA.snapshot8_osc()

def snapshot9():
    print("Snapshot 9 pressed")
    osc_client_LISA.snapshot9_osc()

def snapshot10():
    print("Snapshot 10 pressed")
    osc_client_LISA.snapshot10_osc()

# GrandMA3 button functions
def sequence1():
    print("Sequence 1 pressed")
    osc_client_Grandma3.sequence1_osc()

def sequence2():
    print("Sequence 2 pressed")
    osc_client_Grandma3.sequence2_osc()
    
def sequence3():
    print("Sequence 3 pressed")
    osc_client_Grandma3.sequence3_osc()

def sequence4():
    print("Sequence 4 pressed")
    osc_client_Grandma3.sequence4_osc()

def sequence5():
    print("Sequence 5 pressed")
    osc_client_Grandma3.sequence5_osc()

def pause():
    print("Pause pressed")
    osc_client_Grandma3.pause_osc()

def oops():
    print("Oops pressed")
    osc_client_Grandma3.oops_osc()

#default page on start-up
page1()
main.mainloop()