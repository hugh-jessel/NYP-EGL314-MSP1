# Huats 2024 oscstarterkit
# This python script allow the raspberry pi to act as an OSC server and control the switching of 3 x 2 channels relay
# ywfu-20240521
# To be deployed to respective slave pis

from pythonosc import osc_server, dispatcher
import RPi.GPIO as GPIO

# GPIO pin setup
r1_c1 = 21
r1_c2 = 20
r2_c1 = 26
r2_c2 = 19
r3_c1 = 3
r3_c2 = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(r1_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r1_c2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r2_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r2_c2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r3_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r3_c2, GPIO.OUT, initial=GPIO.HIGH)

# Change the receiver_ip value to your RPi's IP address
receiver_ip = "IP Address" # IP address of your Pi
receiver_port = 2003 # Team C: 2001, Team E: 2002, Team B: 2003, Team F: 2004

# This function handles the received OSC messages and controls the GPIO pins
def control_relay(addr, *args):
    if addr == "/trigger":
        msg = args[0].split(',')
        spk = int(msg[0].strip())
        channel = int(msg[1].strip())
        value = int(msg[2].strip())
        
        print(f"The spk {spk} controlling channel {channel} and the value is {value}")
        if spk == 1: # Change according to spk number (refer to S536 drawing)
            if channel == 1:
                if value == 1:
                    GPIO.output(r1_c1, GPIO.LOW)
                    print("Relay 1 channel 1 turned ON")
                elif value == 0:
                    GPIO.output(r1_c1, GPIO.HIGH)
                    print("Relay 1 channel 1 turned OFF")
            elif channel == 2:
                if value == 1:
                    GPIO.output(r1_c2, GPIO.LOW)
                    print("Relay 1 channel 2 turned ON")
                elif value == 0:
                    GPIO.output(r1_c2, GPIO.HIGH)
                    print("Relay 1 channel 2 turned OFF")

        elif spk == 2: # Change according to spk number (refer to S536 drawing)
            if channel == 1:
                if value == 1:
                    GPIO.output(r2_c1, GPIO.LOW)
                    print("Relay 2 channel 1 turned ON")
                elif value == 0:
                    GPIO.output(r2_c1, GPIO.HIGH)
                    print("Relay 2 channel 1 turned OFF")
            elif channel == 2:
                if value == 1:
                    GPIO.output(r2_c2, GPIO.LOW)
                    print("Relay 2 channel 2 turned ON")
                elif value == 0:
                    GPIO.output(r2_c2, GPIO.HIGH)
                    print("Relay 2 channel 2 turned OFF")

        elif spk == 3: # Change according to spk number (refer to S536 drawing)
            if channel == 1:
                if value == 1:
                    GPIO.output(r3_c1, GPIO.LOW)
                    print("Relay 3 channel 1 turned ON")
                elif value == 0:
                    GPIO.output(r3_c1, GPIO.HIGH)
                    print("Relay 3 channel 1 turned OFF")
            elif channel == 2:
                if value == 1:
                    GPIO.output(r3_c2, GPIO.LOW)
                    print("Relay 3 channel 2 turned ON")
                elif value == 0:
                    GPIO.output(r3_c2, GPIO.HIGH)
                    print("Relay 3 channel 2 turned OFF")

# Catches OSC messages
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/trigger", control_relay) 

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on {}".format(server.server_address))

try:
    server.serve_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Server stopped and GPIO cleaned up")
