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
PI_A_ADDR = "192.168.254.18"		# wlan ip
PORT = 6800

#addr = "/action/40161" # Jump to Marker One

msg = float(1) # Trigger TRUE Value

#send_message(PI_A_ADDR, PORT, addr, msg)

def startMk():
	global PI_A_ADDR
	global port
	addr = "/action/40161" # Jump to Marker One
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Start")

def projectile1():
	global PI_A_ADDR
	global port
	addr = "/action/40162" # Jump to Marker Two
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 1")
	
def projectile2():
	global PI_A_ADDR
	global port
	addr = "/action/40165" # Jump to Marker Five
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 2")
	
def projectile3():
	global PI_A_ADDR
	global port
	addr = "/action/40166" # Jump to Marker Six
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 3")

def projectile4():
	global PI_A_ADDR
	global port
	addr = "/action/40167" # Jump to Marker Seven
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Projectile 4")

def deflect():
	global PI_A_ADDR
	global port
	addr = "/action/40163" # Jump to Marker Three
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("deflect")

def fail():
	global PI_A_ADDR
	global port
	addr = "/action/40164" # Jump to Marker Four
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Fail")

def victory():
	global PI_A_ADDR
	global port
	addr = "/action/40168" # Jump to Marker Eight
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)
	print("Pass")
