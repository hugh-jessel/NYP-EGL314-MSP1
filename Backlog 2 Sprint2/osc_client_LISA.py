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
PI_A_ADDR = "192.168.254.18"		# ip of L-ISA controller(When swapping network please check)
PORT = 8880
# addr = "/print"

def snapshot1_osc():
	global PI_A_ADDR
	global PORT
	addr = "/ext/snap/1/f"	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def snapshot2_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/2/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def snapshot3_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/3/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def snapshot4_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/4/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)

def snapshot5_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/5/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)

def snapshot6_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/6/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)

def snapshot7_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/7/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)

def snapshot8_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/8/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def snapshot9_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/9/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def snapshot10_osc():
	global PI_A_ADDR
	global PORT
	global addr
	addr = "/ext/snap/10/f "	
	msg = ""
	send_message(PI_A_ADDR, PORT, addr, msg)