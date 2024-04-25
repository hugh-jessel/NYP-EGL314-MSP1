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
# send_message(PI_A_ADDR, PORT, addr, msg)

def startupmsg():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Client pi is online"
	send_message(PI_A_ADDR, PORT, addr, msg)

def sequence1_osc():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 1 from pi"
	msg = "Go+ Exec 201 Executor 202 At 0 "	
	send_message(PI_A_ADDR, PORT, addr, msg)
	

def sequence2_osc():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "Go+ Exec 202 Executor 201 At 0 "
	send_message(PI_A_ADDR, PORT, addr, msg)
	

def pause_osc():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "Pause "	
	send_message(PI_A_ADDR, PORT, addr, msg)

def oops_osc():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Oops from pi"
	msg = "Oof "
	send_message(PI_A_ADDR, PORT, addr, msg)
	
startupmsg()
