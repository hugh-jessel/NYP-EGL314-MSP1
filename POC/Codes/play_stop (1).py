# Huats 2023 oscstarterkit
# This python script demonstrate controlling Reaper (trigger play/stop playback) using a Raspberry Pi through the
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
PI_A_ADDR = "192.168.254.18"		# Laptop with Reaper's Ip Address
PORT = 6800

def play_stop():
	global PI_A_ADDR
	global port
	addr = "/action/40044" # Start Stop
	msg = float(1) # Trigger TRUE Value

	send_message(PI_A_ADDR, PORT, addr, msg)

