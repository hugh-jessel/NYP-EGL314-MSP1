import tkinter as tk

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
        
def page1():

    pageclear(pageWindow)

    button_active(pageNavButton1)

    tk.Label(pageWindow, text="L-ISA Snapshots", font="helvetica 12 bold").grid(row=0, column=0, columnspan=5, pady=(0, 10))
    
    buttonRelay1On = tk.Button(pageWindow, text="21", font=fontS, bg="black", fg="white", command=snapshot21, height= 2, width=5).grid(row=1, column=0, padx=(20, 0))

    buttonRelay1Off = tk.Button(pageWindow, text="22", font=fontS, bg="black", fg="white", command=snapshot22, height= 2, width=5).grid(row=1, column=1, padx=(0, 0))

    buttonRelay2On = tk.Button(pageWindow, text="23", font=fontS, bg="black", fg="white", command=snapshot23, height= 2, width=5).grid(row=1, column=2, padx=(0, 0))

    buttonRelay2Off = tk.Button(pageWindow, text="24", font=fontS, bg="black", fg="white", command=snapshot24, height= 2, width=5).grid(row=1, column=3, padx=(0, 0))
    
    buttonRelay3On = tk.Button(pageWindow, text="25", font=fontS, bg="black", fg="white", command=snapshot25, height= 2, width=5).grid(row=1, column=4, padx=(0, 0))

    buttonRelay3Off = tk.Button(pageWindow, text="26", font=fontS, bg="black", fg="white", command=snapshot26, height= 2, width=5).grid(row=2, column=0, padx=(20,0))

    buttonRelay4On = tk.Button(pageWindow, text="27", font=fontS, bg="black", fg="white", command=snapshot27, height= 2, width=5).grid(row=2, column=1, padx=(0, 0))

    buttonRelay4Offf = tk.Button(pageWindow, text="28", font=fontS, bg="black", fg="white", command=snapshot28, height= 2, width=5).grid(row=2, column=2, padx=(0, 0))

    buttonRelay5On = tk.Button(pageWindow, text="29", font=fontS, bg="black", fg="white", command=snapshot29, height= 2, width=5).grid(row=2, column=3, padx=(0, 0))

    buttonRelay5Off = tk.Button(pageWindow, text="30", font=fontS, bg="black", fg="white", command=snapshot30, height= 2, width=5).grid(row=2, column=4, padx=(0, 0))
    
    buttonRelay6On = tk.Button(pageWindow, text="29", font=fontS, bg="black", fg="white", command=snapshot29, height= 2, width=5).grid(row=2, column=3, padx=(0, 0))

    buttonRelay6Off = tk.Button(pageWindow, text="30", font=fontS, bg="black", fg="white", command=snapshot30, height= 2, width=5).grid(row=2, column=4, padx=(0, 0))