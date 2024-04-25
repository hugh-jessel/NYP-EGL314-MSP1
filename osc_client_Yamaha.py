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
PI_A_ADDR = "192.168.254.72"		# ip of GrandMA3 ras pi (When swapping network please check)
PORT = 23
addr = "/print"
# send_message(PI_A_ADDR, PORT, addr, msg

def startupmsg():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Client pi is online"
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader1Up():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 1 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 0 0 1000 "	
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader1Down():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 1 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 0 0 500 "	
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def yamahafader2Up():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 1 0 1000 "
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def yamahafader2Down():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 1 0 500 "
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader3Up():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 2 0 1000 "	
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader3Down():
	global PI_A_ADDR
	global PORT
	global addr
	#msg = "OSC Sequence 2 from pi"
	msg = "set MIXER:Current/InCh/Fader/Level 2 0 500 "	
	send_message(PI_A_ADDR, PORT, addr, msg)

startupmsg()
yamahafader1Up()
