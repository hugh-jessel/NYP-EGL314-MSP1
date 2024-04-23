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
PI_A_ADDR = "127.0.0.1"		# wlan ip
PORT = 22
addr = "/print"
# send_message(PI_A_ADDR, PORT, addr, msg

def sequence1_osc():
	msg = "OSC Sequence 1 from pi"	
	send_message(PI_A_ADDR, PORT, addr, msg)
def sequence2_osc():
	msg = "OSC Sequence 2 from pi"	
	send_message(PI_A_ADDR, PORT, addr, msg)
def pause_osc():
	msg = "OSC Pause from pi"	
	send_message(PI_A_ADDR, PORT, addr, msg)
def oops_osc():
	msg = "OSC Oops from pi"	
	send_message(PI_A_ADDR, PORT, addr, msg)