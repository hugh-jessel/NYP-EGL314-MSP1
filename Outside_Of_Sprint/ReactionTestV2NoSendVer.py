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
# North = 60
# South = 65
# East =  62
# West = 64
# #################################
# Others
# #################################
# NorthPressed  || Variables to check
# SouthPressed  || if a buton has 
# EastPressed   || been pressed
# WestPressed   ||
# (Boolean)     ||

#IP Address and Port for sending messages
LR_ADD = "192.168.254.30"  #IP Address of Laptop with L-isa & Reaper(Same Laptop)
R_PORT = 6800             #Port of Reaper

L_PORT = 8880             #Port of L-isa
L_MSG = ""                #Message to be sent to L-isa

G_ADD = "192.168.254.229"
G_PORT = 8888
G_ADDR = "/gma3/cmd"

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
# Global variables
gameCount = 0
timeCount = 0
game_fail = False
direction = None
buttonPressed = False
last_button_press_time = 0
last_note_on_time = time.time()
game_active = False
successful_deflects = 0

# Constants
button_press_delay = 4
note_timeout_threshold = 5
win_threshold = 4
LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"

#Functions
##########Send Messaages function
def reaperSendMessage(addr):
    send_message(LR_ADD,R_PORT,addr,float(1))
def lisaSendMessage(addr):
    send_message(LR_ADD,R_PORT,addr,L_MSG)
def grandMa3SendMessage(msg):
    send_message(G_ADD,G_PORT,G_ADDR,msg)
    
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
		# Send an OSC message to the receiver
		client.send_message(address, message)
		#print("Message sent successfully.")
	except:
		print("Message not sent")
def stage_pass():
    print("Stage Cleared!")
    gameTimeCounter(False)
    reaperSendMessage(R_FullVictoru_ADD)
    grandMa3SendMessage(G_stagePass_MSG)
    #gameTimeCounter(True)
    time.sleep(11) #Delay to allow AI voice to finish
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_gameLights_MSG)
    reaperSendMessage(R_PlayStop_ADD)
    exit()
def stage_fail():
    print("Game Over!")
    gameTimeCounter(False)
    reaperSendMessage(R_gameOver_ADD)
    grandMa3SendMessage(G_stageFail_MSG)
    time.sleep(8) #Replace with length of fail audio
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_centerSpotlight_MSG)
    reaperSendMessage(R_PlayStop_ADD)
    exit()
    game_fail = True
def stage_fail_Restart():
    global game_fail
    print("Game Over! Restart?")
    reaperSendMessage(R_gameOver_ADD)
    grandMa3SendMessage(G_stageFail_MSG)
    time.sleep(8) #Replace with length of fail audio
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_clearAll_MSG)
    grandMa3SendMessage(G_centerSpotlight_MSG)
    reaperSendMessage(R_PlayStop_ADD)
    grandMa3SendMessage(G_centerSpotlight_MSG)

def gameRestart():
    global gameCount
    global timeCount
    global game_fail
    global direction
    global buttonPressed
    global last_button_press_time
    global last_note_on_time
    global game_active
    global successful_deflects

    gameCount = 0
    timeCount = 0
    game_fail = False
    buttonPressed = False
    last_button_press_time = 0
    last_note_on_time = time.time()
    game_active = False
    successful_deflects = 0
    snapshotRandom()  # Reset the initial direction

def gameTimeCounter(gameTime):
    global gameCount
    while gameTime == True:
        time.sleep(0.5)
        gameCount += 0.5
        return gameCount
    else:
        pass
def reactionTimeCounter(reactionB,reaction):
    global timeCount
    while reactionB == True:
        for i in range(1,reaction+1):
            time.sleep(0.5)
            timeCount += 0.5
            print(f"Projectile was fired {timeCount} seconds ago")
            return timeCount
def snapshotRandom():
    global direction
    random_number = random.randint(1,10)
    SequenceRandom = {
        1: (reaperSendMessage(L_Snap21_ADD), "North"),
        2: (reaperSendMessage(L_Snap21_ADD), "West"),
        3: (reaperSendMessage(L_Snap21_ADD), "East"),
        4: (reaperSendMessage(L_Snap21_ADD), "South"),
        5: (reaperSendMessage(L_Snap21_ADD), "East"),
        6: (reaperSendMessage(L_Snap21_ADD), "West"),
        7: (reaperSendMessage(L_Snap21_ADD), "North"),
        8: (reaperSendMessage(L_Snap21_ADD), "South"),
        9: (reaperSendMessage(L_Snap21_ADD), "North"),
        10: (reaperSendMessage(L_Snap21_ADD), "South")
    }
    function, direction = SequenceRandom[random_number]
    print(f"Snapshot has been sent to the {direction}")
def randomProjectiles(projectileList,projectileAmount):
    random_number = random.randint(1,projectileAmount)
    projectileList[random_number]()
    print(f"For {projectileAmount}, Projectile {random_number} is firing")
def stage1Projectile():
    projectiles = {
        1: (reaperSendMessage(R_S1Proj2_ADD)),
        2: (reaperSendMessage(R_S1Proj3_ADD)),
        3: (reaperSendMessage(R_S1Proj4_ADD))
    }
    randomProjectiles(projectiles, 3)
    # projectiles = [reaperSendMessage(R_S1Proj2_ADD),
    #                reaperSendMessage(R_S1Proj3_ADD),
    #                reaperSendMessage(R_S1Proj4_ADD)]
def stage2Projectile():
    projectiles = {
        1: (reaperSendMessage(R_S2Proj2_ADD)),
        2: (reaperSendMessage(R_S2Proj3_ADD)),
        3: (reaperSendMessage(R_S2Proj4_ADD)),
        4: (reaperSendMessage(R_S2Proj5_ADD)),
        5: (reaperSendMessage(R_S2Proj6_ADD))
    }
    randomProjectiles(projectiles, 5)
    # projectiles = [reaperSendMessage(R_S2Proj2_ADD),
    #                reaperSendMessage(R_S2Proj3_ADD),
    #                reaperSendMessage(R_S2Proj4_ADD),
    #                reaperSendMessage(R_S2Proj5_ADD),
    #                reaperSendMessage(R_S2Proj6_ADD)]
   
def deflect(direction):
    reaperSendMessage(R_Deflect_ADD)
    # if direction in pressedDirection:
    #     pressedDirection = pressedDirection[direction]
    #     globals()[pressedDirection] = True
    print(f"Deflected from the {direction}")
    print(f"{direction} has been pressed! True!")
    # else:
    #     print(f"Error: {direction} is not a valid direction.")
def varaReset():
    resettedDirection = {
        "NorthPressed": False,
        "SouthPressed": False,
        "EastPressed": False,
        "WestPressed": False
    }
    global NorthPressed, SouthPressed, EastPressed, WestPressed
    NorthPressed, SouthPressed, EastPressed, WestPressed = resettedDirection.values()     
def nextstage(count):
    global stageNo
    if stageNo == 1:
        if count < 5:
            count + 1
            return count
        else:
            stageNo += 1
            return stageNo
    elif stageNo == 2:
        if count < 6:
            count + 1
            return count
        else:
            stageNo + 1
            return stageNo
    elif stageNo == 3:
        if count < 8:
            count + 1
            return count
        else:
            pass #win
direction_map = {
    "North": 60,
    "South": 65,
    "East": 62,
    "West": 64
}

def reactionTest():
    global gameCount
    global game_fail
    global direction
    global buttonPressed
    global last_button_press_time
    global last_note_on_time
    global game_active
    global successful_deflects
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name")
        return
    with mido.open_input(LaunchpadPro_Name) as inport, mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages")
        snapshotRandom()  # Set the initial direction
        try:
            while True:
                gameTimeCounter(True)
                print(f"The game has been going for {gameCount} seconds")
                current_time = time.time()  # Get the current timestamp
                
                # Reset buttonPressed if the delay has passed
                if buttonPressed and (current_time - last_button_press_time >= button_press_delay):
                    buttonPressed = False
                    print(f"Button press reset after {button_press_delay} seconds")
                    
                # Check for game over due to inactivity, only if the game is active
                if game_active and (current_time - last_note_on_time >= note_timeout_threshold):
                    print(f"Game over due to inactivity. Time since last note_on: {current_time - last_note_on_time:.2f} seconds")
                    game_fail = True
                    stage_fail_Restart()  # Handle game over and restart
                    gameRestart()  # Reset game state for restart
                    print("Game has been reset. Waiting for next start...")
                    continue  # Continue to the next iteration to wait for a restart
                
                # Ensure game is active after gameCount reaches 5
                if gameCount >= 5:
                    if not game_active:
                        last_note_on_time = current_time
                        game_active = True  # Set the game as active once gameCount reaches 5
                        print("Game is now active")
                for msg in inport.iter_pending():
                    if msg.type == "note_on" and game_active == True:
                        print(f"Note On: Note={msg.note}")

                        last_note_on_time = current_time  # Update the timestamp for the last note_on message

                        if not buttonPressed:
                            buttonPressed = True
                            if direction and msg.note == direction_map[direction]:
                                print(f"Successful deflect: Direction {direction}, Note {msg.note}")
                                deflect(direction)
                                successful_deflects += 1  # Increment the successful deflect counter
                                print(f"Total successful deflects: {successful_deflects}")

                                if successful_deflects >= win_threshold:
                                    print(f"Congratulations! You've won the game with {successful_deflects} successful deflects!")
                                    game_fail = False
                                    stage_pass()  # Call a function to handle the win scenario
                                    break  # Exit the loop, ending the game

                                time.sleep(0.5)
                                snapshotRandom()  # Determine the next projectile direction
                                # Send appropriate message based on the game state
                            else:
                                print(f"Failed deflect: Note {msg.note} does not match direction {direction}")
                                game_fail = True
                                stage_fail_Restart()  # Handle game over and restart
                                gameRestart()  # Reset game state for restart
                                print("Game has been reset. Waiting for next start...")
                                break  # Exit the loop to wait for restart
                    elif msg.note == 67:  # Check if restart note is pressed
                        if game_fail == True:
                            print("Restarting game...")
                            gameRestart()  # Reset game state for restart
                            continue  # Continue to the next iteration to wait for the restart
                    else:
                        print(f"Ignoring input: Note={msg.note} before gameCount reaches 5")
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")