#Imports
import mido
import sys
import time
import random
from pythonosc import udp_client

#### Variables used ####
#################################
# L-ISA Sequences
# (L-R,T-B)
# #################################
# North-
# Sequence  29
# Sequence 21
# Sequence 27
# South-
# Sequence 28
# Sequence - 24
# Sequence - 30
# East-
# Sequence 25
# Sequence 23
# Sequence
# West-
# Sequence 
# Sequence 22
# Sequence 26
# #################################
# msg.note for each direction
# #################################
North = 60
South = 65
East =  62
West = 64

#IP Address and Port for sending messages
LR_ADD = "192.168.254.30"  #IP Address of Laptop with L-isa & Reaper(Same Laptop)
R_PORT = 6800             #Port of Reaper

L_PORT = 8880             #Port of L-isa
L_MSG = ""                #Message to be sent to L-isa

G_ADD = "192.168.254.229"
G_PORT = 8888
G_ADD = "/gma3/cmd"

#Address definitions
## Reaper definitions ##
R_PlayStop_ADD = "/action/40044"  #Play/Stop toggle on reaper
R_StartGame_ADD = "/action/41261" #marker for game start
#No Projectile 1 since it runs after the start naturally
R_S1Proj2_ADD = "/action/41265"   #marker for stage 1 projectile 2
R_S1Proj3_ADD = "/action/41266"   #marker for stage 1 projectile 3
R_S1Proj4_ADD = "/action/41267"   #marker for stage 1 projectile 4
R_StageTrans_ADD = "/action/41268" #marker for stage 1 transition to stage 2/2 to 3
R_Deflect_ADD = "/action/41263"   #marker for deflect
R_gameOver_ADD = "/action/41264"  #marker for game over
R_FullVictoru_ADD = "/marker/27"  #marker for victory
R_Restart_ADD = "/marker/9"       #marker for restart;after tutorial message
R_S2Proj2_ADD = "/marker/14"      #marker for stage 2 projectile 2
R_S2Proj3_ADD = "/marker/15"      #marker for stage 2 projectile 3
R_S2Proj4_ADD = "/marker/16"      #marker for stage 2 projectile 4
R_S2Proj5_ADD = "/marker/17"      #marker for stage 2 projectile 5
R_S2Proj6_ADD = "/marker/18"      #marker for stage 2 projectile 6
## L-isa definitions ##
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
## GrandMa3 definitons ##
G_stagePass_MSG = "Go+: Sequence 68"   #stage pass/win
G_stageFail_MSG = "Go+: Sequence 69"   #game over
G_directions_MSG = "Go+: Sequence 70"  #direction showcase during explanation
G_murugunLights_MSG = "Go+: Sequence 71"  #Station marker;lead people to station
G_centerSpotlight_MSG = "Go+: Sequence 72" #game area spotlight
G_gameLights_MSG = "Go+: Sequence 73"   #game lights
G_AIsaac_MSG = "Go+: Sequence 74"    #spotlight for artifact holder       
G_clearAll_MSG = "Off MyRunningSequence"  #clear sequences
#Other definitions
pressed_flag = {directions: False for directions in ["North","South","East","West"]}
projectile_direction = {
    "North": 60,
    "South": 65,
    "East": 62,
    "West": 64
}
#Initializing variables
projCount = 0
gameCount = 0
game_fail = False
direction = ""
stageNo = 1
x = 0.0
#Functions
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
		# Send an OSC message to the receiver
		client.send_message(address, message)
		print("Message sent successfully.")
	except:
		print("Message not sent")
def stage_pass():
    print("Stage Cleared!")
    send_message(LR_ADD,R_PORT,R_StageTrans_ADD,float(1))
    send_message(G_ADD,G_PORT,G_ADD,G_stagePass_MSG)
    time.sleep(13) #Delay to allow AI voice to finish
    send_message(G_ADD,G_PORT,G_ADD,G_clearAll_MSG)
    send_message(G_ADD,G_PORT,G_ADD,G_clearAll_MSG)
    send_message(G_ADD,G_PORT,G_ADD,G_gameLights_MSG)
def stage_fail():
    print("Game Over!")
    send_message(LR_ADD,R_PORT,R_gameOver_ADD,float(1))
    send_message(G_ADD,G_PORT,G_ADD,G_stageFail_MSG)
    time.sleep(0) #Replace with length of fail audio
    send_message(G_ADD,G_PORT,G_ADD,G_clearAll_MSG)
    send_message(G_ADD,G_PORT,G_ADD,G_clearAll_MSG)
    send_message(G_ADD,G_PORT,G_ADD,G_centerSpotlight_MSG)
    game_fail = True