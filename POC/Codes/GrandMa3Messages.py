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

PI_A_ADDR = "192.168.254.229"		# ip of GrandMA3 ras pi (When swapping network please check)

PORT = 8888

addr = "/gma3/cmd"



def stagePass():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 68"	

	send_message(PI_A_ADDR, PORT, addr, msg)



def stageFail():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 69"	

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def directions():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 70"	

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def murugunLight():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 71"	

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def directToCTR():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 72"	

	send_message(PI_A_ADDR, PORT, addr, msg)



def playing():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+: Sequence 73"	

	send_message(PI_A_ADDR, PORT, addr, msg)



def pause_osc():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Pause"	

	send_message(PI_A_ADDR, PORT, addr, msg)



def clear_all():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Off MyRunningSequence"

	send_message(PI_A_ADDR, PORT, addr, msg)





def go():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Go+"	

	send_message(PI_A_ADDR, PORT, addr, msg)

	

def clear():

	global PI_A_ADDR

	global PORT

	global addr

	msg = "Clear"	

	send_message(PI_A_ADDR, PORT, addr, msg)
