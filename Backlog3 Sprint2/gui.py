import tkinter as tk

import Lisa_GrandMa3_Functions

import reaper_markers

import play_stop



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

    button_inactive(pageNavButton3)



    tk.Label(pageWindow, text="L-ISA Snapshots", font="helvetica 12 bold").grid(row=0, column=0, columnspan=5, pady=(0, 10))



    buttonSnapshot21 = tk.Button(pageWindow, text="21", font=fontS, bg="black", fg="white", command=snapshot21, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))

    buttonSnapshot22 = tk.Button(pageWindow, text="22", font=fontS, bg="black", fg="white", command=snapshot22, height= 2, width=5).grid(row=1, column=1, padx=(0, 0))

    buttonSnapshot23 = tk.Button(pageWindow, text="23", font=fontS, bg="black", fg="white", command=snapshot23, height= 2, width=5).grid(row=1, column=2, padx=(0, 0))

    buttonSnapshot24 = tk.Button(pageWindow, text="24", font=fontS, bg="black", fg="white", command=snapshot24, height= 2, width=5).grid(row=1, column=3, padx=(0, 0))
    
    buttonSnapshot25 = tk.Button(pageWindow, text="25", font=fontS, bg="black", fg="white", command=snapshot25, height= 2, width=5).grid(row=1, column=4, padx=(0, 0))

    buttonSnapshot26 = tk.Button(pageWindow, text="26", font=fontS, bg="black", fg="white", command=snapshot26, height= 2, width=5).grid(row=2, column=0, padx=(20,0))

    buttonSnapshot27 = tk.Button(pageWindow, text="27", font=fontS, bg="black", fg="white", command=snapshot27, height= 2, width=5).grid(row=2, column=1, padx=(0, 0))

    buttonSnapshot28 = tk.Button(pageWindow, text="28", font=fontS, bg="black", fg="white", command=snapshot28, height= 2, width=5).grid(row=2, column=2, padx=(0, 0))

    buttonSnapshot29 = tk.Button(pageWindow, text="29", font=fontS, bg="black", fg="white", command=snapshot29, height= 2, width=5).grid(row=2, column=3, padx=(0, 0))

    buttonSnapshot30 = tk.Button(pageWindow, text="30", font=fontS, bg="black", fg="white", command=snapshot30, height= 2, width=5).grid(row=2, column=4, padx=(0, 0))
    
"""     buttonTest0 = tk.Button(pageWindow, text="Test0", font=fontS, bg="black", fg="white", command=test0, height= 2, width=5).grid(row=3, column=0, padx=(20,0))

    buttonTest1 = tk.Button(pageWindow, text="Test1", font=fontS, bg="black", fg="white", command=test1, height= 2, width=5).grid(row=3, column=1, padx=(0,0)) """

def page2():

    pageclear(pageWindow)

    button_active(pageNavButton2)

    button_inactive(pageNavButton1)

    button_inactive(pageNavButton3)

    tk.Label(pageWindow, text="GrandMA3 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))



    buttonSequence1 = tk.Button(pageWindow, text="Spotlight", font=fontS, bg="black", fg="white", command=spotlightMA3, height= 2, width=12).grid(row=1, column=0, padx=(20, 0))

    buttonSequence2 = tk.Button(pageWindow, text="Stage Failed", font=fontS, bg="black", fg="white", command=stageFailedMa3, height= 2, width=12).grid(row=2, column=0, padx=(20, 0))

    buttonSequence3 = tk.Button(pageWindow, text="Stage Passed", font=fontS, bg="black", fg="white", command=stagePassedMa3, height= 2, width=12).grid(row=3, column=0, padx=(20, 0))

    buttonSequence4 = tk.Button(pageWindow, text="Station Marker", font=fontS, bg="black", fg="white", command=stationMarkerMa3, height= 2, width=12).grid(row=4, column=0, padx=(20, 0))

    buttonSequence5 = tk.Button(pageWindow, text="Game Light", font=fontS, bg="black", fg="white", command=gamelightsMa3, height= 2, width=12).grid(row=5, column=0, padx=(20, 0))

    buttonDirections = tk.Button(pageWindow, text="Directions", font=fontS, bg="black", fg="white", command=directions, height= 2, width=10).grid(row=1, column=1, padx=(20, 20))
    
    buttonPause = tk.Button(pageWindow, text="Pause", font=fontS, bg="black", fg="white", command=pause, height= 2, width=10).grid(row=2, column=1, padx=(20, 20))

    buttonOops = tk.Button(pageWindow, text="Clear", font=fontS, bg="black", fg="white", command=clear, height= 2, width=10).grid(row=3, column=1, padx=(20, 20))

    buttonClear = tk.Button(pageWindow, text="Clear All", font=fontS, bg="black", fg="white", command=clear_all, height= 2, width=10).grid(row=4, column=1, padx=(20, 20))

def page3():

    pageclear(pageWindow)

    button_active(pageNavButton3)

    button_inactive(pageNavButton1)

    button_inactive(pageNavButton2)

    tk.Label(pageWindow, text="GrandMA3 Controls", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))



    buttonGameStart = tk.Button(pageWindow, text="GameStart", font=fontS, bg="black", fg="white", command=gameStartRp, height= 2, width=12).grid(row=1, column=0, padx=(20, 0))

    buttonProjectile1 = tk.Button(pageWindow, text="Projectile1", font=fontS, bg="black", fg="white", command=Projectile1Rp, height= 2, width=12).grid(row=2, column=0, padx=(20, 0))

    buttonProjectile2 = tk.Button(pageWindow, text="Projectile2", font=fontS, bg="black", fg="white", command=Projectile2Rp, height= 2, width=12).grid(row=3, column=0, padx=(20, 0))

    buttonProjectile3 = tk.Button(pageWindow, text="Projectile3", font=fontS, bg="black", fg="white", command=Projectile3Rp, height= 2, width=12).grid(row=4, column=0, padx=(20, 0))

    buttonDeflect = tk.Button(pageWindow, text="Deflect", font=fontS, bg="black", fg="white", command=DeflectRp, height= 2, width=12).grid(row=5, column=0, padx=(20, 0))

    buttonFail = tk.Button(pageWindow, text="Fail", font=fontS, bg="black", fg="white", command=FailRp, height= 2, width=10).grid(row=1, column=1, padx=(20, 20))

    buttonVictory = tk.Button(pageWindow, text="Victory", font=fontS, bg="black", fg="white", command=VictoryRp, height= 2, width=10).grid(row=2, column=1, padx=(20, 20))

    buttonStart_Pause = tk.Button(pageWindow, text="Start/Pause", font=fontS, bg="black", fg="white", command=StartPauseRp, height= 2, width=10).grid(row=2, column=1, padx=(20, 20))

# page navigation buttons

pageNavButton1 = tk.Button(pageNav, text="L-ISA Studio", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)

pageNavButton1.grid(row=1, column=0, padx=(20, 0))

pageNavButton2 = tk.Button(pageNav, text="GrandMA3", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)

pageNavButton2.grid(row=2, column=0, padx=(20, 0))

pageNavButton3 = tk.Button(pageNav, text="Reaper", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page3, height= 2, width=10)

pageNavButton3.grid(row=3, column=0, padx=(20, 0))



# button colour change on press

def button_active(x):

    x.config(bg="#7d8adb")



def button_inactive(x):

    x.config(bg="#1f2a70")



# L-ISA button functions

def snapshot21():

    print("Snapshot 21 pressed")

    Lisa_GrandMa3_Functions.Seq21()



def snapshot22():

    print("Snapshot 22 pressed")

    Lisa_GrandMa3_Functions.Seq22()



def snapshot23():

    print("Snapshot 23 pressed")

    Lisa_GrandMa3_Functions.Seq23()



def snapshot24():

    print("Snapshot 24 pressed")

    Lisa_GrandMa3_Functions.Seq24()

def snapshot25():

    print("Snapshot 25 ")

    Lisa_GrandMa3_Functions.Seq25()



def snapshot26():

    print("Snapshot 26 pressed")

    Lisa_GrandMa3_Functions.Seq26()



def snapshot27():

    print("Snapshot 27 pressed")

    Lisa_GrandMa3_Functions.Seq27()



def snapshot28():

    print("Snapshot 28 pressed")

    Lisa_GrandMa3_Functions.Seq28()



def snapshot29():

    print("Snapshot 29 pressed")

    Lisa_GrandMa3_Functions.Seq29()



def snapshot30():

    print("Snapshot 30 pressed")

    Lisa_GrandMa3_Functions.Seq30()

def test0():
    
    print("Test 0 pressed")
    
    Lisa_GrandMa3_Functions.Test0()
    
def test1():
    
    print("Test 1 pressed")
    
    Lisa_GrandMa3_Functions.Test1()
0
# GrandMA3 button functions



def spotlightMA3():

    print("spotlightMA3 pressed")

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.directToCTR()



def stageFailedMa3():

    print("stageFailedMa3 pressed")

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.stageFail()

    

def stagePassedMa3():

    print("stagePassedMa3 pressed")

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.stagePass()



def stationMarkerMa3():

    print("stationMarkerMa3 pressed")

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.murugunLight()



def gamelightsMa3():

    print("gamelightsMa3 pressed")

    # Lisa_GrandMa3_Functions.clear_all()

    # Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.playing()

def directions():

    print("directions pressed")

    Lisa_GrandMa3_Functions.directions()

def pause():

    print("Pause pressed")

    Lisa_GrandMa3_Functions.pause_osc()



def clear():

    print("clear pressed")

    Lisa_GrandMa3_Functions.clear()



def clear_all():

    print("clear all")

    Lisa_GrandMa3_Functions.clear_all()

    Lisa_GrandMa3_Functions.clear_all()

#Reaper button functions

def gameStartRp():

    print("game start")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.startMk()

def Projectile1Rp():

    print("Projectile 1")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.projectile1()

def Projectile2Rp():

    print("Projectile 2")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.projectile2()

def Projectile3Rp():

    print("Projectile 3")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.projectile3()

def DeflectRp():

    print("Deflect")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.deflect()

def FailRp():

    print("Fail")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.fail()

def VictoryRp():

    print("Victory")

    #play_stop.play_stop()
    
    reaper_markers.play_stop()
    
    reaper_markers.victory()

def StartPauseRp():
    
    print("Pause")
    
    #play_stop.play_stop()
    
    reaper_markers.play_stop()

#default page on start-up

page1()

main.mainloop()
