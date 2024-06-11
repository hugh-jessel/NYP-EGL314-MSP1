# Huats 2023 oscstarterkit

from pythonosc import udp_client

def send_messageLISA(receiver_ip, receiver_port, address, message):

	try:

		# Create an OSC client to send messages

		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)



		# Send an OSC message to the receiver

		client.send_message(address, message)



		print("Message sent successfully.")

	except:

		print("Message not sent")

def send_messageGrandMa3(receiver_ip, receiver_port, address, message):

	try:

		# Create an OSC client to send messages

		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)



		# Send an OSC message to the receiver

		client.send_message(address, message)



		print("Message sent successfully.")

	except:

		print("Message not sent")



#LISA

PI_A_ADDR = "192.168.254.30"		# ip of L-ISA controller(When swapping network please check)

PORT = 8880

# addr = "/print"



def Seq21():

	global PI_A_ADDR

	global PORT

	addr = "/ext/snap/21/f"	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def Seq22():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/22/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def Seq23():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/23/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def Seq24():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/24/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)



def Seq25():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/25/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)



def Seq26():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/26/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)



def Seq27():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/27/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)



def Seq28():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/28/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def Seq29():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/29/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def Seq30():

	global PI_A_ADDR

	global PORT

	global addr

	addr = "/ext/snap/30/f "	

	msg = ""

	send_message(PI_A_ADDR, PORT, addr, msg)
