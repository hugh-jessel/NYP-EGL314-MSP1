import mido
import midi
import play_stop
import reaper_markers
import Lisa_GrandMa3_Functions

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
                    print(f'Note On: Note={msg.note}')
                    if msg.note == 67: #start
                        print ('Game Start')
                        play_stop.play_stop()
                        Lisa_GrandMa3_Functions.clear_all()
                        Lisa_GrandMa3_Functions.clear_all()
                        Lisa_GrandMa3_Functions.playing()
                        reaper_markers.startMk()
                        midi.Midi_LaunchPad_MK3()
                        
                elif msg.type == 'note_off':
                    # Note off messages represent pad releases
                    print(f'Note Off: Note={msg.note}')
                    #print(f'Note Off: Note={msg.note} Velocity={msg.velocity}')
        except KeyboardInterrupt:
                print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()