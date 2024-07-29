# Huats 2023 oscstarterkit

from pythonosc import udp_client

def send_messageLISA(receiver_ip, receiver_PORT_LISA, address, message):

	try:

		# Create an OSC client to send messages

		client = udp_client.SimpleUDPClient(receiver_ip, receiver_PORT_LISA)



		# Send an OSC message to the receiver

		client.send_message(address, message)



		print("Message sent successfully.")

	except:

		print("Message not sent")

def send_messageGrandMa3(receiver_ip, receiver_PORT_LISA, address, message):

	try:

		# Create an OSC client to send messages

		client = udp_client.SimpleUDPClient(receiver_ip, receiver_PORT_LISA)



		# Send an OSC message to the receiver

		client.send_message(address, message)



		print("Message sent successfully.")

	except:

		print("Message not sent")



#LISA

PI_A_ADDR_LISA = "192.168.254.30"		# ip of L-ISA controller(When swapping network please check)

PORT_LISA = 8880

msg_LISA = ""


#LISA functions
def Seq21():

	global PI_A_ADDR_LISA

	global PORT_LISA

	addr_GrandMa3 = "/ext/snap/21/f"	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq22():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/22/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq23():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/23/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)

	
def Seq24():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/24/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq25():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/25/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq26():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/26/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq27():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/27/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)


def Seq28():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/28/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)

	
def Seq29():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/29/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)

	
def Seq30():

	global PI_A_ADDR_LISA

	global PORT_LISA

	global addr_GrandMa3

	addr_GrandMa3 = "/ext/snap/30/f "	

	msg_LISA = ""

	send_messageLISA(PI_A_ADDR_LISA, PORT_LISA, addr_GrandMa3, msg_LISA)

#GrandMa3

PI_A_ADDR_GrandMa3 = "192.168.254.229"		# ip of GrandMA3 ras pi (When swapping network please check)

PORT_GrandMa3 = 8888

addr_GrandMa3 = "/gma3/cmd"


#GrandMa3 Funtions

def stagePass():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 68"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)


def stageFail():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 69"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)


def directions():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 70"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)

	
def murugunLight():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 71"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)

	
def directToCTR():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 72"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)
 
def AIssac():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 74"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)

def facelight(): #75
    
	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 75"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)
def playing():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+: Sequence 73"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)

def LightShow():
	global PI_A_ADDR_GrandMa3
	global PORT_GrandMa3
	global addr_GrandMa3

	msg = "Go+: Sequence 76"

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)


def pause_osc():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Pause"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)


def clear_all():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Off MyRunningSequence"

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)


def go():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Go+"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)

	
def clear():

	global PI_A_ADDR_GrandMa3

	global PORT_GrandMa3

	global addr_GrandMa3

	msg = "Clear"	

	send_messageGrandMa3(PI_A_ADDR_GrandMa3, PORT_GrandMa3, addr_GrandMa3, msg)
