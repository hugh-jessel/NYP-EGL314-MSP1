#Imports
import mido 
import play_stop
import reaper_markers
import sys
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import time
import random
import threading
import definitions

def North():
    global tracker1
    countToSG2(tracker1)
    if tracker1 == 4:
        definitions.nextstage()
        countT_stop(count_timing)
    else:
        definitions.North()
    
def South():
    global tracker1
    countToSG2(tracker1)
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.South()

def East():
    global tracker1
    countToSG2(tracker1)
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.East()

def West():
    countToSG2(tracker1)
    if tracker1 == 4:
        definitions.nextstage()
    else:
        definitions.West()

def countT_start(count_timing):
    print('count_timing start')
    count = 0
    count += 0.5
    print(count)
    return count

def countT_stop(count_timing):
    print('count_timing Stopped')
    count = 0
    print(count)
    return count

def countToSG2(tracker1):
    count = 0
    count += 1
    return count

def launchpad_listen():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name")
        return
    with mido.open_input(LaunchpadPro_Name) as inport,mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages" )
        global count_timing
        count_game = 0
        NorthPressed = 'False'
        SouthPressed = 'False'
        EastPressed = 'False'
        WestPressed = 'False'
        
        game_fail = 'False'
        directional_Var = 0
        tracker1 = 0
        count_timing = 0
        try:
            while True:
                #for msg in inport:
                time.sleep(0.5)                            
                count_game += 0.5
                print(f"The game has been going for {count_game} seconds")
                for msg in inport.iter_pending():
                    if msg.type == 'note_on':
                        print(f"Note On:Note={msg.note}")
                        if count_game == 37: #28 is when tutorial ends
                            Lisa_GrandMa3_Functions.Seq21()
                            #################Projectile 1 (Hardcoded)################
                        elif 40 >= count_game >= 38: #Count for first projectile
                            count_game2 = 0  
                            
                            
                            time.sleep(0.5)            
                            count_timing += 0.5
                            print(f"How many seconds has it been since the projectile has been fired {count_timing}")
                            if count_timing <= 3: #if they react under 4 sec
                                if msg.note == 60 and NorthPressed == 'False': #actual snapshot coresponding to north
                                    countToSG2(tracker1)
                                    print(f"How many projectiles have been fired:{tracker1}")
                                    if tracker1 == 4:
                                        definitions.nextstage()
                                    else:
                                        NorthPressed = 'True'
                                        print(NorthPressed)
                                        print("North deflected")
                                        countT_stop(count_timing)
                                        definitions.North()
                                        break
                                elif msg.note != 60 and NorthPressed == 'False':
                                    definitions.game_over()
                                    #trigger for restart
                                    game_fail = 'True'
                                    exit()
                                         
                                           
                                elif count_timing > 4 and NorthPressed == 'False':
                                    definitions.game_over()
                                    #trigger for restart
                                    game_fail = 'True'
                                    exit() 
                                    
                                    
                        elif 40 >= count_game >= 38  and NorthPressed == 'True':
                            pass
                        
                        elif count_game == 41:
                            definitions.resetVar()
                            Lisa_GrandMa3_Functions.Seq24()
                        elif count_game >= 40: #Second Projectiles
                            if msg.note == 65:
                                definitions.deflect_success()
                                definitions.nextstage()
                                time.sleep(5)
                                exit()
                            exit()
                            countT_start(count_timing)
                            if count_timing <= 3:
                                if msg.note == 60 and directional_Var == 'North':
                                    North()
                                elif msg.note == 65 and directional_Var == 'South':
                                    South()
                                elif msg.note == 62 and directional_Var == 'East':
                                    East()
                                elif msg.note == 64 and directional_Var == 'West':
                                    West()
                            elif count_timing > 4 and (NorthPressed and SouthPressed and EastPressed and WestPressed) == 'False' :
                                        definitions.game_over()
                                        #trigger for restart
                                        game_fail = 'True'
                                        exit()
                                         
                                
                        elif 47 >= count_game >= 44 and SouthPressed == 'True':
                            pass
                        elif count_game == 48:
                            definitions.resetVar()
                        
                                
                    else:
                        print(f'Note Off: Note={msg.note}')
        except KeyboardInterrupt:
            print("stopped listening to MIDI messages.")

if __name__ == "__main__":
    
    launchpad_listen()
