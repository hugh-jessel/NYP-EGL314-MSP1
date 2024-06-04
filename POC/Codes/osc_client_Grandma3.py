# Huats 2023 oscstarterkit
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
PI_A_ADDR = "192.168.254.137"		# ip of GrandMA3 ras pi (When swapping network please check)
PORT = 23
addr = "/print"

def sequence1_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Go+ Exec 201 At 1"	
	send_message(PI_A_ADDR, PORT, addr, msg)

def sequence2_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Go+ Exec 202 At 1"	
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def sequence3_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Go+ Exec 203 At 1"	
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def sequence4_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Go+ Exec 204 At 1"	
	send_message(PI_A_ADDR, PORT, addr, msg)

def sequence5_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Go+ Exec 205 At 1"	
	send_message(PI_A_ADDR, PORT, addr, msg)

def pause_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Pause"	
	send_message(PI_A_ADDR, PORT, addr, msg)

def oops_osc():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Oops"
	send_message(PI_A_ADDR, PORT, addr, msg)