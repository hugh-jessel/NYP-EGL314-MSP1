from pythonosc import osc_server, dispatcher

from pythonosc import udp_client

import tkinter as tk

import reaper_markers

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

PI_B_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT2 = 2005

def AllOff():
    msg = ["1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0",
           "4,1,0", "4,2,0", "5,1,0", "5,2,0", "6,1,0", "6,2,0",
           "7,1,0", "7,2,0", "8,1,0", "8,2,0", "9,1,0", "9,2,0",
           "10,1,0", "10,2,0", "11,1,0", "11,2,0", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def AllOn():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1",
           "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1",
           "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1",
           "10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def OddSpk():
    msg = ["1,1,1", "1,2,1", "2,1,0", "2,2,0", "3,1,1", "3,2,1",
           "4,1,0", "4,2,0", "5,1,1", "5,2,1", "6,1,0", "6,2,0",
           "7,1,1", "7,2,1", "8,1,0", "8,2,0", "9,1,1", "9,2,1",
           "10,1,0", "10,2,0", "11,1,1", "11,2,1", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def EvenSpk():
    msg = ["1,1,0", "1,2,0", "2,1,1", "2,2,1", "3,1,0", "3,2,0",
           "4,1,1", "4,2,1", "5,1,0", "5,2,0", "6,1,1", "6,2,1",
           "7,1,0", "7,2,0", "8,1,1", "8,2,1", "9,1,0", "9,2,0",
           "10,1,1", "10,2,1", "11,1,0", "11,2,0", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def crossfire():
    msg = ["1,1,0", "1,2,0", "2,1,1", "2,2,1", "3,1,0", "3,2,0",
           "4,1,0", "4,2,0", "5,1,1", "5,2,1", "6,1,0", "6,2,0",
           "7,1,0", "7,2,0", "8,1,1", "8,2,1", "9,1,0", "9,2,0",
           "10,1,0", "10,2,0", "11,1,1", "11,2,1", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def AllOnOneByOne():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1",
           "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1",
           "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1",
           "10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def AllOffOneByOne():
    msg = ["1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0",
           "4,1,0", "4,2,0", "5,1,0", "5,2,0", "6,1,0", "6,2,0",
           "7,1,0", "7,2,0", "8,1,0", "8,2,0", "9,1,0", "9,2,0",
           "10,1,0", "10,2,0", "11,1,0", "11,2,0", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def crossfireOpp():
    msg = ["1,1,1", "1,2,1", "2,1,0", "2,2,0", "3,1,1", "3,2,1",
           "4,1,1", "4,2,1", "5,1,0", "5,2,0", "6,1,1", "6,2,1",
           "7,1,1", "7,2,1", "8,1,0", "8,2,0", "9,1,1", "9,2,1",
           "10,1,1", "10,2,1", "11,1,0", "11,2,0", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def OneToThreeOn():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def FourToSixOn():
    msg = ["4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def SevenToNineOn():
    msg = ["7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1
        
        if y == len(msg):
            break

def TenToTwelveOn():
    msg = ["10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
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

def TopHalf():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,0", "3,2,0",
           "4,1,0", "4,2,0", "5,1,0", "5,2,0", "6,1,0", "6,2,0",
           "7,1,0", "7,2,0", "8,1,1", "8,2,1", "9,1,1", "9,2,1",
           "10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def BottomHalf():
    msg = ["1,1,0", "1,2,0", "2,1,1", "2,2,1", "3,1,1", "3,2,1",
           "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1",
           "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,0", "9,2,0",
           "10,1,0", "10,2,0", "11,1,0", "11,2,0", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def LeftHalf():
    msg = ["1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0",
           "4,1,0", "4,2,0", "5,1,1", "5,2,1", "6,1,1", "6,2,1",
           "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1",
           "10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,0", "12,2,0"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break
        
def RightHalf():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1",
           "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,0", "6,2,0",
           "7,1,0", "7,2,0", "8,1,0", "8,2,0", "9,1,0", "9,2,0",
           "10,1,0", "10,2,0", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def OneToThreeOnOneByOne():
    msg = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def FourToSixOnOneByOne():
    msg = ["4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

def SevenToNineOnOneByOne():
    msg = ["7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1
        
        if y == len(msg):
            break
    
def TenToTwelveOnOneByOne():
    msg = ["10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    y = int(0)
    while y < len(msg):
        time.sleep(0.03)
        send_message(send_addr, send_port, addr, msg[y])
        print(msg[y])
        y += 1

        if y == len(msg):
            break

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

            if count % 2 == 0:
                send_color(PI_B_ADDR, PORT2, 0, 0, 0)
                send_brightness(PI_B_ADDR, PORT2, 0)
            else:
                send_color(PI_B_ADDR, PORT2, 255, 0, 0)
                send_brightness(PI_B_ADDR, PORT2, 0.3)

            # Using a dictionary to map counts to functions
            actions = {
                0: AllOff,
                1: AllOn,
                2: OddSpk,
                3: AllOff,
                4: AllOnOneByOne,
                5: AllOffOneByOne,
                6: crossfire,
                7: crossfireOpp,
                8: AllOff,
                9: AllOn,
                10: AllOffOneByOne,
                11: OneToThreeOn,
                12: FourToSixOn,
                13: SevenToNineOn,
                14: TenToTwelveOn,
                15: AllOff,
                16: OddSpk,
                17: EvenSpk,
                18: AllOff,
                19: OneToThreeOn,
                20: AllOff,
                21: AllOn,
                22: AllOff,
                23: OddSpk,
                24: EvenSpk,
                25: AllOnOneByOne,
                26: crossfire,
                27: crossfireOpp,
                28: TopHalf,
                29: BottomHalf,
                30: AllOffOneByOne,
                31: LeftHalf,
                32: RightHalf,
                33: AllOffOneByOne,
                34: AllOn,
                35: AllOff,
                36: OneToThreeOnOneByOne,
                37: SevenToNineOnOneByOne,
                38: AllOffOneByOne,
                39: AllOnOneByOne,
                40: AllOnOneByOne,
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
        AllOff()
        send_color(PI_B_ADDR, PORT2, 0, 0, 0)
        send_brightness(PI_B_ADDR, PORT2, 0)
        reaper_markers.play_stop()
        print(f"Counted {count} beats in 30 seconds.")  # max Count = 73/72
    except Exception as e:
        print(f"Error during cleanup: {e}")

""" without server

def laser1_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser1_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()

def laser2_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser2_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()

def laser3_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser3_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()

def laser4_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser4_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()

def laser5_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser5_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()

def laser6_onS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.LOW)
    print('Relay ON - The relay will stay on until the program is terminated')

def laser6_offS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup() """

#default page on start-up

page1()
main.mainloop()