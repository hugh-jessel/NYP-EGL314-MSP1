import mido 
import sys
import play_stop
import reaper_markers
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import threading
import definitions
import time
receiver_ip = "0.0.0.0"
receiver_port = 7131

#Definitions
    
def launchpad(): #Main Chunk of Game Code
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return
    with mido.open_input(LaunchpadPro_Name) as inport,mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")
        global count
        
        definitions.resetVar()
        NorthVal = float(0.25318267941474915)
        SouthVal = float(0.5)
        EastVal = float(0.75)
        WestVal = float(1)
        
        game_start = 'False'
        directional_Var = 0
        try:
            while True:
                for msg in inport:
                    for msg in inport.iter_pending():
                        if msg.type == 'note_on':
                            print(f'For game code Note On: Note={msg.note}')
                            
                            if msg.note == 67 and game_start == 'False':
                                print ('Game Start')
                                play_stop.play_stop()
                                Lisa_GrandMa3_Functions.clear_all()
                                Lisa_GrandMa3_Functions.clear_all()
                                time.sleep(0.1)
                                Lisa_GrandMa3_Functions.playing()
                                Lisa_GrandMa3_Functions.playing()
                                reaper_markers.startMk()
                                game_start = 'True'
                                tracker1 = 0
                                
                                if directional_Var == NorthVal and NorthPressed == 'False' and game_start == 'True':
                                    definitions.count_start()
                                    definitions.resetVar()
                                    if msg.note == 60 and count < 3:
                                        definitions.count_stop()
                                        print ("North deflected")
                                        definitions.countToSG2(tracker1)
                                        if tracker1 == 4:
                                            reaper_markers.victory()
                                        else:
                                            definitions.deflect_success()
                                            NorthPressed = 'True'
                                            definitions.projectiles()
                                    else:
                                        definitions.game_over()
                                elif directional_Var == NorthVal and NorthPressed == 'True':
                                    pass #do nothing
                                elif directional_Var == SouthVal and SouthPressed == 'False' and game_start == 'True':
                                    definitions.count_start()
                                    definitions.resetVar()
                                    if msg.note == 62 and count < 3:
                                        print("South deflected")
                                        definitions.count_stop()
                                        definitions.countToSG2(tracker1)
                                        if tracker1 == 4:
                                            definitions.nextstage()
                                        else:
                                            definitions.deflect_success()
                                            NorthPressed = 'True'
                                            definitions.projectiles()
                                        SouthPressed = 'True'
                                    else:
                                        definitions.game_over()
                                elif directional_Var == SouthVal and SouthPressed == 'True':
                                    pass
                                elif directional_Var == EastVal and EastPressed == 'False' and game_start == 'True':
                                    definitions.count_start()
                                    definitions.resetVar()
                                    if msg.note == 62 and count < 3:
                                        print("East deflected")
                                        definitions.countToSG2(tracker1)
                                        definitions.count_stop()
                                        if tracker1 == 4:
                                            definitions.nextstage()
                                        else:
                                            definitions.deflect_success()
                                            EastPressed = 'True'
                                            definitions.projectiles()
                                        EastPressed = 'True'
                                    else:
                                        definitions.game_over()
                                elif directional_Var == EastVal and EastPressed == 'True':
                                    pass
                                elif directional_Var == WestVal and WestPressed == 'False' and game_start == 'True':
                                    definitions.count_start()
                                    definitions.resetVar()
                                    if msg.note == 64 and count < 3:
                                        print("West deflected")
                                        definitions.count_stop()
                                        definitions.countToSG2(tracker1)
                                        if tracker1 == 4:
                                            definitions.nextstage()
                                        else:
                                            definitions.deflect_success()
                                            WestPressed = 'True'
                                            definitions.projectiles()
                                    else:
                                        definitions.game_over()
                                elif directional_Var == WestVal and WestPressed == 'True':
                                    pass
                        elif msg.type == 'note_off':
                            print(f'For game code Note Off: Note={msg.note}')
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    
    
    LP = threading.Thread(target=launchpad)
    #LL = threading.Thread(target=fromLisa)
    #LL.start()
    LP.start()
    #server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
    #print("Serving on{}".format(server.server_address))
    #server.serve_forever()