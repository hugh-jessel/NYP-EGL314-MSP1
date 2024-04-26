# Huats 2023 oscstarterkit
from pythonosc import udp_client
import gui

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

'''def startupmsg():
	global PI_A_ADDR
	global PORT
	global addr
	msg = "Client pi is online"
	send_message(PI_A_ADDR, PORT, addr, msg)'''

# convert GUI values to yamaha values
def rangeconvert1():
	OldValue = gui.var1
	OldMax = 100
	OldMin = 0
	NewMax = 1000
	NewMin = -32768
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	global NewValue1
	NewValue1 = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

def rangeconvert2():
	OldValue = gui.var2
	OldMax = 100
	OldMin = 0
	NewMax = 1000
	NewMin = -32768
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	global NewValue2
	NewValue2 = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

def rangeconvert3():
	OldValue = gui.var3
	OldMax = 100
	OldMin = 0
	NewMax = 1000
	NewMin = -32768
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	global NewValue3
	NewValue3 = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

def yamahafader1Up():
	rangeconvert1()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 0 0 {NewValue1} "	
	print(NewValue1)
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader1Down():
	rangeconvert1()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 0 0 {NewValue1} "	
	print(NewValue1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def yamahafader2Up():
	rangeconvert2()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 1 0 {NewValue2} "
	print(NewValue2)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def yamahafader2Down():
	rangeconvert2()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 1 0 {NewValue2} "
	print(NewValue2)
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader3Up():
	rangeconvert3()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 2 0 {NewValue3} "	
	print(NewValue3)
	send_message(PI_A_ADDR, PORT, addr, msg)

def yamahafader3Down():
	rangeconvert3()
	global PI_A_ADDR
	global PORT
	global addr
	msg = "set MIXER:Current/InCh/Fader/Level 2 0 {NewValue3} "	
	print(NewValue3)
	send_message(PI_A_ADDR, PORT, addr, msg)

#startupmsg()
