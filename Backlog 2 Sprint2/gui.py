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



    buttonSnapshot21 = tk.Button(pageWindow, text="North", font=fontS, bg="black", fg="white", command=snapshot21, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))

    buttonSnapshot22 = tk.Button(pageWindow, text="West", font=fontS, bg="black", fg="white", command=snapshot22, height= 2, width=5).grid(row=1, column=1, padx=(0, 0))

    buttonSnapshot23 = tk.Button(pageWindow, text="East", font=fontS, bg="black", fg="white", command=snapshot23, height= 2, width=5).grid(row=1, column=2, padx=(0, 0))

    buttonSnapshot24 = tk.Button(pageWindow, text="South", font=fontS, bg="black", fg="white", command=snapshot24, height= 2, width=5).grid(row=1, column=3, padx=(0, 0))

    # buttonSnapshot5 = tk.Button(pageWindow, text="5", font=fontS, bg="black", fg="white", command=snapshot5, height= 2, width=5).grid(row=1, column=4, padx=(0, 20))

    # buttonSnapshot6 = tk.Button(pageWindow, text="6", font=fontS, bg="black", fg="white", command=snapshot6, height= 2, width=5).grid(row=2, column=0, padx=(20, 0))

    # buttonSnapshot7 = tk.Button(pageWindow, text="7", font=fontS, bg="black", fg="white", command=snapshot7, height= 2, width=5).grid(row=2, column=1, padx=(0, 0))

    # buttonSnapshot8 = tk.Button(pageWindow, text="8", font=fontS, bg="black", fg="white", command=snapshot8, height= 2, width=5).grid(row=2, column=2, padx=(0, 0))

    # buttonSnapshot9 = tk.Button(pageWindow, text="9", font=fontS, bg="black", fg="white", command=snapshot9, height= 2, width=5).grid(row=2, column=3, padx=(0, 0))

    # buttonSnapshot10 = tk.Button(pageWindow, text="10", font=fontS, bg="black", fg="white", command=snapshot10, height= 2, width=5).grid(row=2, column=4, padx=(0, 20))



def page2():

    pageclear(pageWindow)

    button_active(pageNavButton2)

    button_inactive(pageNavButton1)



    tk.Label(pageWindow, text="GrandMA3 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))



    buttonSequence1 = tk.Button(pageWindow, text="Spotlight", font=fontS, bg="black", fg="white", command=spotlightMA3, height= 2, width=12).grid(row=1, column=0, padx=(20, 0))

    buttonSequence2 = tk.Button(pageWindow, text="Stage Failed", font=fontS, bg="black", fg="white", command=stageFailedMa3, height= 2, width=12).grid(row=2, column=0, padx=(20, 0))

    buttonSequence3 = tk.Button(pageWindow, text="Stage Passed", font=fontS, bg="black", fg="white", command=stagePassedMa3, height= 2, width=12).grid(row=3, column=0, padx=(20, 0))

    buttonSequence4 = tk.Button(pageWindow, text="Station Marker", font=fontS, bg="black", fg="white", command=stationMarkerMa3, height= 2, width=12).grid(row=4, column=0, padx=(20, 0))

    buttonSequence5 = tk.Button(pageWindow, text="Game Light", font=fontS, bg="black", fg="white", command=gamelightsMa3, height= 2, width=12).grid(row=5, column=0, padx=(20, 0))

    buttonPause = tk.Button(pageWindow, text="Pause", font=fontS, bg="black", fg="white", command=pause, height= 2, width=10).grid(row=1, column=1, padx=(20, 20))

    buttonOops = tk.Button(pageWindow, text="Clear", font=fontS, bg="black", fg="white", command=clear, height= 2, width=10).grid(row=2, column=1, padx=(20, 20))

    buttonClear = tk.Button(pageWindow, text="Clear All", font=fontS, bg="black", fg="white", command=clear_all, height= 2, width=10).grid(row=3, column=1, padx=(20, 20))



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

def snapshot21():

    print("Snapshot 1 pressed")

    osc_client_LISA.North()



def snapshot22():

    print("Snapshot 2 pressed")

    osc_client_LISA.West()



def snapshot23():

    print("Snapshot 3 pressed")

    osc_client_LISA.East()



def snapshot24():

    print("Snapshot 4 pressed")

    osc_client_LISA.South()



# def snapshot5():

    # print("Snapshot 5 pressed")

    # osc_client_LISA.snapshot5_osc()



# def snapshot6():

    # print("Snapshot 6 pressed")

    # osc_client_LISA.snapshot6_osc()



# def snapshot7():

    # print("Snapshot 7 pressed")

    # osc_client_LISA.snapshot7_osc()



# def snapshot8():

    # print("Snapshot 8 pressed")

    # osc_client_LISA.snapshot8_osc()



# def snapshot9():

    # print("Snapshot 9 pressed")

    # osc_client_LISA.snapshot9_osc()



# def snapshot10():

    # print("Snapshot 10 pressed")

    # osc_client_LISA.snapshot10_osc()



# GrandMA3 button functions



def spotlightMA3():

    print("spotlightMA3 pressed")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.directToCTR()



def stageFailedMa3():

    print("stageFailedMa3 pressed")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.stageFail()

    

def stagePassedMa3():

    print("stagePassedMa3 pressed")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.stagePass()



def stationMarkerMa3():

    print("stationMarkerMa3 pressed")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.murugunLight()



def gamelightsMa3():

    print("gamelightsMa3 pressed")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.playing()



def pause():

    print("Pause pressed")

    osc_client_Grandma3.pause_osc()



def clear():

    print("clear pressed")

    osc_client_Grandma3.clear()



def clear_all():

    print("clear all")

    osc_client_Grandma3.clear_all()

    osc_client_Grandma3.clear_all()



#default page on start-up

page1()

main.mainloop()