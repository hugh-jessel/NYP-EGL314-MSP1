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

def sequence1_osc():
	receiver_ip1 = "192.168.254.94" 
	receiver_port1 = 8000
	address1 = "/print"
	message1 = "OSC Sequence 1 from pi"	
	send_message(receiver_ip1, receiver_port1, address1, message1)
def sequence2_osc():
	receiver_ip1 = "192.168.254.94" 
	receiver_port1 = 8000
	address1 = "/print"
	message1 = "OSC Sequence 1 from pi"	
	send_message(receiver_ip1, receiver_port1, address1, message1)
def pause_osc():
	receiver_ip1 = "192.168.254.94" 
	receiver_port1 = 8000
	address1 = "/print"
	message1 = "OSC Sequence 1 from pi"	
	send_message(receiver_ip1, receiver_port1, address1, message1)
def oops_osc():
	receiver_ip1 = "192.168.254.94" 
	receiver_port1 = 8000
	address1 = "/print"
	message1 = "OSC Sequence 1 from pi"	
	send_message(receiver_ip1, receiver_port1, address1, message1)

# FOR INFO: IP address and port of the receiving Raspberry Pi
# PI_A_ADDR = "127.0.0.1"		# wlan ip
# PORT = 8111

# addr = "/print"
# msg = "Message from pi client"

# send_message(PI_A_ADDR, PORT, addr, msg)