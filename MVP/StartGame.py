#Imports
import mido 
import reaper_markers
import sys
import Lisa_GrandMa3_Functions
import Gamestart_wipV2
from pythonosc import osc_server, dispatcher
import time

def Midi_LaunchPad_MK3():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return

    with mido.open_input(LaunchpadPro_Name) as inport, mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")
        try:
            for msg in inport:
                
                if msg.type == 'note_on':
                    # Note on messages represent pad presses
                    print(f'For Game Start Note On: Note={msg.note}')
                    if msg.note == 67: #start
                        print ('Game Start')
                        
                        reaper_markers.play_stop() # Stop any currently playing track 
                        
                        Lisa_GrandMa3_Functions.clear_all()   
                        Lisa_GrandMa3_Functions.clear_all()
                        Lisa_GrandMa3_Functions.playing()
                        Lisa_GrandMa3_Functions.playing()
                        reaper_markers.startMk()
                        Gamestart_wipV2.launchpad_listen()
                    
                    else:
                        pass
                elif msg.type == 'note_off':
                    # Note off messages represent pad releases
                    print(f'For Game Start Note Off: Note={msg.note}')
        except KeyboardInterrupt:
                print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()
