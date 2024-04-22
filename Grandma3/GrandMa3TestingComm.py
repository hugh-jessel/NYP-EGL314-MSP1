from pythonosc import udp_client
import time

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)   

		print("Message sent successfully.")
	except:
		print("Message not sent")

#change the below values
if __name__ == "__main__":
    LAPTOP_IP = "192.168.1.61"		# send to laptop w grandMA3
    PORT = 8000                     # laptop w grandMA3 port number
    addr = "/gma3/Page1/Fader201"

    send_message(LAPTOP_IP, PORT, addr, "Go to Sequence 1")
	