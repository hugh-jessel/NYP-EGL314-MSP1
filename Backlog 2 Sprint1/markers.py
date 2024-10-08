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
PI_A_ADDR = "192.168.254.18"		# Laptop With L-isa's IP Address
PORT = 6800
msg = float(1) # Trigger TRUE Value

def marker_1():
	global PI_A_ADDR
	global port
	addr = "/action/40161" # Jump to Marker One
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)

def marker_2():
	global PI_A_ADDR
	global port
	addr = "/action/40162" # Jump to Marker Two
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)

def marker_3():
	global PI_A_ADDR
	global port
	addr = "/action/40163" # Jump to Marker Three
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)

def marker_4():
	global PI_A_ADDR
	global port
	addr = "/action/40164" # Jump to Marker Four
	global msg
	send_message(PI_A_ADDR, PORT, addr, msg)