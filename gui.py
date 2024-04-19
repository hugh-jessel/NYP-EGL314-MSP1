import tkinter as tk
import osc_client

def function1():
    print("This is function 1")

def function2():
    print("This is function 2")

def function3():
    print("This is function 3")

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
       
def  osc_call():
    osc_client.shitass()

main = tk.Tk()
var = 0

title = tk.Label(main, text="NYPOSC DEMO CLASS", font="20")
title.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(main, text="Function 1", font ="20", command=function1)
button2 = tk.Button(main, text="Function 2", font ="20", command=function2)
button3 = tk.Button(main, text="Function 3", font ="20", command=function3)
buttonosc = tk.Button(main, text="OSC", font="20", command=osc_call)
volumeup = tk.Button(main, text="Volume +", font="20", command=lambda m=1:volume_change(m))
volumedown = tk.Button(main, text="Volume -", font="20", command=lambda m=0:volume_change(m))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonosc.grid(row=3, column=1)
volumeup.grid(row=2, column=0)
volumedown.grid(row=2, column=2)

main.mainloop()