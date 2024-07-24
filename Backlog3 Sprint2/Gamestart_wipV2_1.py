#Imports
import mido 
import reaper_markers
import sys
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import time
import random
import threading
import definitions

def North_check():
    global tracker1
    tracker1 += 1
    if tracker1 == 4:
        definitions.nextstage()
        timing_count_stop(count_timing)
    else:
        definitions.North()
    
def South_check():
    global tracker1
    tracker1 += 1
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.South()

def East_check():
    global tracker1
    tracker1 += 1
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.East()

def West_check():
    tracker1 += 1
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.West()

def game_time_counter():  #Run with main code in StartGame.py
    time.sleep(0.5)                            
    count_game += 0.5
    print(f"The game has been going for {count_game} seconds")
    
def timing_count_start(count_timing): #Used to time participant reaction speed
    print("count_timing start")
    count = 0
    count += 0.5
    print(count)
    return count

def timing_count_stop(count_timing): #Used to stop previous funtion 
    print("count_timing Stopped")
    count = 0
    print(count)
    return count

def reactionTime(reactionTiming):
    global x
    z = 0
    while z in x <= reactionTiming:    
        z += 0.5
        print(f"Projectile was fired {z} seconds ago")
        x = z
        return x
def gameTimeCounter(counting):
    global gameCount
    while counting == "True":
        time.sleep(0.5)
        gameCount += 0.5
        print(f"The game has been going for {gameCount} seconds")
    return gameCount

""" def countToSG2(tracker1):  #Used to count number of projectiles before sending to next stage
    count = 0
    count += 1
    return count """

count_game = 0
NorthPressed = "False"
SouthPressed = "False"
EastPressed = "False"
WestPressed = "False"

game_fail = "False"
directional_Var = 0
tracker1 = 0
count_timing = 0
        
def launchpad_listen():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name")
        return
    with mido.open_input(LaunchpadPro_Name) as inport,mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages" )
        global count_game
        global NorthPressed
        global SouthPressed
        global EastPressed
        global WestPressed
        global game_fail
        global reactionTiming
        
        counting = "True"
        gameTimeCounter(counting)
        try:
            while True:
                #for msg in inport:
                for msg in inport.iter_pending():
                    if msg.type == "note_on":
                        print(f"Note On:Note={msg.note}")
                     
                        
                                
                    else:
                        print(f"Note Off: Note={msg.note}")
        except KeyboardInterrupt:
            print("stopped listening to MIDI messages.")


if __name__ == "__main__":
    
    launchpad_listen()