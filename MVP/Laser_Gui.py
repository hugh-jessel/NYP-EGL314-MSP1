from pythonosc import osc_server, dispatcher

from pythonosc import udp_client

import tkinter as tk

import reaper_markers

import Lisa_GrandMa3_Functions 

# import RPi.GPIO as GPIO

import time

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)
		print("Message sent successfully.")

	except:
		print("Message not sent")

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

    buttonLaser1On = tk.Button(pageWindow, text="Laser1 On", font=fontM, bg="black", fg="white", command=laser1_on).grid(row=1, column=0, padx=(20, 0))
    buttonLaser1Off = tk.Button(pageWindow, text="Laser1 Off", font=fontM, bg="black", fg="white", command=laser1_off).grid(row=1, column=1, padx=(20, 0))

    buttonLaser2On = tk.Button(pageWindow, text="Laser2 On", font=fontM, bg="black", fg="white", command=laser2_on).grid(row=2, column=0, padx=(20, 0))
    buttonLaser2Off = tk.Button(pageWindow, text="Laser2 Off", font=fontM, bg="black", fg="white", command=laser2_off).grid(row=2, column=1, padx=(20, 0))

    buttonLaser3On = tk.Button(pageWindow, text="Laser3 On", font=fontM, bg="black", fg="white", command=laser3_on).grid(row=3, column=0, padx=(20, 0))
    buttonLaser3Off = tk.Button(pageWindow, text="Laser3 Off", font=fontM, bg="black", fg="white", command=laser3_off).grid(row=3, column=1, padx=(20, 0))

    buttonLaser4On = tk.Button(pageWindow, text="Laser4 On", font=fontM, bg="black", fg="white", command=laser4_on).grid(row=4, column=0, padx=(20, 0))
    buttonLaser4Off = tk.Button(pageWindow, text="Laser4 Off", font=fontM, bg="black", fg="white", command=laser4_off).grid(row=4, column=1, padx=(20, 0))

    buttonLaser5On = tk.Button(pageWindow, text="Laser5 On", font=fontM, bg="black", fg="white", command=laser5_on).grid(row=5, column=0, padx=(20, 0))
    buttonLaser5Off = tk.Button(pageWindow, text="Laser5 Off", font=fontM, bg="black", fg="white", command=laser5_off).grid(row=5, column=1, padx=(20, 0))

    buttonLaser6On = tk.Button(pageWindow, text="Laser6 On", font=fontM, bg="black", fg="white", command=laser6_on).grid(row=6, column=0, padx=(20, 0))
    buttonLaser6Off = tk.Button(pageWindow, text="Laser6 Off", font=fontM, bg="black", fg="white", command=laser6_off).grid(row=6, column=1, padx=(20, 0))

    buttonLaserSeq = tk.Button(pageWindow, text="Laser Show", font=fontM, bg="black", fg="white", command=lasersequence).grid(row=7, column=0, padx=(20, 0))

def page2():

    pageclear(pageWindow)

    button_active(pageNavButton2)

    button_inactive(pageNavButton1)

    tk.Label(pageWindow, text="Page 2", font="helvetica 12 bold").grid(row=0, column=0, columnspan=2, pady=(0, 10))

    """ buttonLaser1OnS = tk.Button(pageWindow, text="Laser1 On", font=fontM, bg="black", fg="white", command=laser1_onS).grid(row=1, column=0, padx=(20, 0))
    buttonLaser1OffS = tk.Button(pageWindow, text="Laser1 Off", font=fontM, bg="black", fg="white", command=laser1_offS).grid(row=1, column=1, padx=(20, 0))

    buttonLaser2OnS = tk.Button(pageWindow, text="Laser2 On", font=fontM, bg="black", fg="white", command=laser2_onS).grid(row=2, column=0, padx=(20, 0))
    buttonLaser2OffS = tk.Button(pageWindow, text="Laser2 Off", font=fontM, bg="black", fg="white", command=laser2_offS).grid(row=2, column=1, padx=(20, 0))

    buttonLaser3OnS = tk.Button(pageWindow, text="Laser3 On", font=fontM, bg="black", fg="white", command=laser3_onS).grid(row=3, column=0, padx=(20, 0))
    buttonLaser3OffS = tk.Button(pageWindow, text="Laser3 Off", font=fontM, bg="black", fg="white", command=laser3_offS).grid(row=3, column=1, padx=(20, 0))

    buttonLaser4OnS = tk.Button(pageWindow, text="Laser4 On", font=fontM, bg="black", fg="white", command=laser4_onS).grid(row=4, column=0, padx=(20, 0))
    buttonLaser4OffS = tk.Button(pageWindow, text="Laser4 Off", font=fontM, bg="black", fg="white", command=laser4_offS).grid(row=4, column=1, padx=(20, 0))

    buttonLaser5OnS = tk.Button(pageWindow, text="Laser5 On", font=fontM, bg="black", fg="white", command=laser5_onS).grid(row=5, column=0, padx=(20, 0))
    buttonLaser5OffS = tk.Button(pageWindow, text="Laser5 Off", font=fontM, bg="black", fg="white", command=laser5_offS).grid(row=5, column=1, padx=(20, 0))

    buttonLaser6OnS = tk.Button(pageWindow, text="Laser6 On", font=fontM, bg="black", fg="white", command=laser6_onS).grid(row=6, column=0, padx=(20, 0))
    buttonLaser6OffS = tk.Button(pageWindow, text="Laser6 Off", font=fontM, bg="black", fg="white", command=laser6_offS).grid(row=6, column=1, padx=(20, 0)) """

#page navigation buttons

pageNavButton1 = tk.Button(pageNav, text="Laser w/ Server", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page1, height= 2, width=10)

pageNavButton1.grid(row=1, column=0)

pageNavButton2 = tk.Button(pageNav, text="Laser w/o Server", font ="30", bg="#1f2a70", fg="white", activebackground="#545e9c", command=page2, height= 2, width=10)

pageNavButton2.grid(row=2, column=0)

# button colour change on press

def button_active(x):
    x.config(bg="#7d8adb")

def button_inactive(x):
    x.config(bg="#1f2a70")

send_addr = "192.168.254.49"
send_port = 2000
addr = "/print"

# laser button functions

def laser1_on():
    msg = ["7, 1, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser1_off():
    msg = ["7, 1, 0"]
    send_message(send_addr, send_port, addr, msg)

def laser2_on():
    msg = ["7, 2, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser2_off():
    msg = ["7, 2, 0"]
    send_message(send_addr, send_port, addr, msg)

def laser3_on():
    msg = ["8, 1, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser3_off():
    msg = ["8, 1, 0"]
    send_message(send_addr, send_port, addr, msg)

def laser4_on():
    msg = ["8, 2, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser4_off():
    msg = ["8, 2, 0"]
    send_message(send_addr, send_port, addr, msg)

def laser5_on():
    msg = ["9, 1, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser5_off():
    msg = ["9, 1, 0"]
    send_message(send_addr, send_port, addr, msg)

def laser6_on():
    msg = ["9, 2, 1"]
    send_message(send_addr, send_port, addr, msg)

def laser6_off():
    msg = ["9, 2, 0"]
    send_message(send_addr, send_port, addr, msg)

def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

PI_Truss_Pixel = "192.168.254.242"  # Change to your RPi's IP address
PORT_Truss_Pixel = 2005
client_Truss_Pixel = udp_client.SimpleUDPClient(PI_Truss_Pixel, PORT_Truss_Pixel)

# Truss Neopixel
def send_color_array(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client_Truss_Pixel.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

def send_brightness(brightness):
    client_Truss_Pixel.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

def send_off():
    client_Truss_Pixel.send_message("/off", [])
    print("Sent off message")

PI_Balloon_Pixel = "192.168.254.102"
PORT_Balloon_Pixel = 2006
client_Balloon_Pixel = udp_client.SimpleUDPClient(PI_Balloon_Pixel, PORT_Balloon_Pixel)

# Ballon Neopixel
def send_color_array2(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client_Balloon_Pixel.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

def send_brightness2(brightness):
    client_Balloon_Pixel.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

def send_off2():
    client_Balloon_Pixel.send_message("/off", [])
    print("Sent off message")

# Laser Functions

def crossfire():
    msg = ["2,1,1", "2,2,1",
           "5,1,1", "5,2,1",
           "8,1,1", "8,2,1",
           "11,1,1", "11,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break
    
def crossfireOff():
    msg = ["2,1,0", "2,2,0",
           "5,1,0", "5,2,0",
           "8,1,0", "8,2,0",
           "11,1,0", "11,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def Laser_SequenceRP():

    print("Laser Sequence")

    #play_stop.play_stop()

    reaper_markers.play_stop()
    reaper_markers.lasershow()

def GrandMA3_Sequence():
    Lisa_GrandMa3_Functions.LightShow()

def GrandMa3_Go():
    Lisa_GrandMa3_Functions.go()

def GrandMa3_Clear():
    Lisa_GrandMa3_Functions.clear_all()

def lasersequence():
    try:
        Laser_SequenceRP()
    except Exception as e:
        print(f"Error in Laser_SequenceRP: {e}")
        return

    print("test")

    beat_gap = 60 / 101  # Time interval between beats
    count = 0
    start_time = time.time()

    try:
        while time.time() - start_time < 30:
            time.sleep(beat_gap)

            # Using a dictionary to map counts to functions
            actions = {
                0: crossfireOff,
            }

            if count in actions:
                try:
                    actions[count]()
                except Exception as e:
                    print(f"Error executing action for count {count}: {e}")

            print(count)
            count += 1

    except Exception as e:
        print(f"Error in main loop: {e}")

    try:
        crossfireOff()
        GrandMa3_Clear()
        send_off()
        send_off2()
        reaper_markers.play_stop()
        print(f"Counted {count} beats in 30 seconds.")  # max Count = 73/72
    except Exception as e:
        print(f"Error during cleanup: {e}")

#default page on start-up

page1()
main.mainloop()