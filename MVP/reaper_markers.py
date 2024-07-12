# Huats 2023 oscstarterkit
# This python script demonstrate controlling Reaper (Jump to Marker 1) using a Raspberry Pi through the
# OSC messaging protocol
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.30"		# wlan ip
PORT = 6800

#addr = "/action/40161" # Jump to Marker One

msg = float(1) # Trigger TRUE Value

#send_message(PI_A_ADDR, PORT, addr, msg)


def play_stop():
	global PI_A_ADDR
	global port
	addr = "/action/40044" # Start Stop
	msg = float(1) # Trigger TRUE Value
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def startMk():
	global PI_A_ADDR
	global port
	addr = "/action/41261" # Jump to Marker 21
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Start")

def projectile1():
	global PI_A_ADDR
	global port
	addr = "/action/41265" # Jump to Marker 25
	#addr = "GOTO_MARKER i/marker t/marker/5" # Jump to Marker Five
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 1")
	
def projectile2():
	global PI_A_ADDR
	global port
	addr = "/action/41266" # Jump to Marker 26
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 2")
	
def projectile3():
	global PI_A_ADDR
	global port
	addr = "/action/41267" # Jump to Marker 27 
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 3")

def tut_stagepass():
	global PI_A_ADDR
	global port
	addr = "/action/41268" # Jump to Marker 28
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Tutorial Stage Passed")

def deflect():
	global PI_A_ADDR
	global port
	addr = "/action/41263" # Jump to Marker 23
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("deflect")

def fail():
	global PI_A_ADDR
	global port
	addr = "/action/41264" # Jump to Marker 24
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Fail")

def victory():
	global PI_A_ADDR
	global port
	addr = "/marker/27" # Jump to Marker 63
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Beaten Game!")
	
def restart():
	global PI_A_ADDR
	global port
	addr = "/marker/9" # Jump to Marker 63
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Game Restarted!")

def lasershow():
	global PI_A_ADDR
	global PORT
	addr = "/marker/64"
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Laser Show Starting!")