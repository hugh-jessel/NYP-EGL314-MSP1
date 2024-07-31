import mido
import sys
from pythonosc import osc_server,dispatcher,udp_client
import time

LR_ADD = "192.168.254.30"
L_PORT = 8880             #Port of L-isa
L_MSG = ""   

L_Snap21_ADD = "/ext/snap/21/f"    
L_Snap22_ADD = "/ext/snap/22/f"
L_Snap23_ADD = "/ext/snap/23/f"
L_Snap24_ADD = "/ext/snap/24/f"
L_Snap25_ADD = "/ext/snap/25/f"
L_Snap26_ADD = "/ext/snap/26/f"
L_Snap27_ADD = "/ext/snap/27/f"
L_Snap28_ADD = "/ext/snap/28/f"
L_Snap29_ADD = "/ext/snap/29/f"
L_Snap30_ADD = "/ext/snap/30/f"

        # 1: (lambda: lisaSendMessage(L_Snap21_ADD), "North"),
        # 2: (lambda: lisaSendMessage(L_Snap21_ADD), "West"),
        # 3: (lambda: lisaSendMessage(L_Snap21_ADD), "East"),
        # 4: (lambda: lisaSendMessage(L_Snap21_ADD), "South"),
        # 5: (lambda: lisaSendMessage(L_Snap21_ADD), "East"),
        # 6: (lambda: lisaSendMessage(L_Snap21_ADD), "West"),
        # 7: (lambda: lisaSendMessage(L_Snap21_ADD), "North"),
        # 8: (lambda: lisaSendMessage(L_Snap21_ADD), "South"),
        # 9: (lambda: lisaSendMessage(L_Snap21_ADD), "North"),
        # 10: (lambda: lisaSendMessage(L_Snap21_ADD), "South")
        
def lisaSendMessage(addr):
    send_message(LR_ADD,L_PORT,addr,L_MSG)
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
		# Send an OSC message to the receiver
		client.send_message(address, message)
		#print("Message sent successfully.")
	except:
		print("Message not sent")

def SnapTest():
	Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
	with mido.open_input(Name) as inport, mido.open_output(Name) as outport:
		print(f"Listening to {Name} for note messages....")
		try:
			for msg in inport:
				if msg.type == 'note_on':
					print (msg.note)
					if msg.note == 60:
						lisaSendMessage(L_Snap27_ADD)
					elif msg.note == 65:
						lisaSendMessage(L_Snap24_ADD)
					elif msg.note == 62:
						lisaSendMessage(L_Snap23_ADD)
					elif msg.note == 64:
						lisaSendMessage(L_Snap22_ADD)
		except KeyboardInterrupt:
			print("Stopped listening to MIDI messages.")
            
if __name__ == "__main__":
    SnapTest()