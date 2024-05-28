import mido
import markers
import play_stop

def Midi_LaunchPad_MK3():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"

    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return

    with mido.open_input(LaunchpadPro_Name) as inport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")
        try:
            for msg in inport:
                
                if msg.type == 'note_on':
                    # Note on messages represent pad presses
                    print(f'Note On: Note={msg.note}')
                    if msg.note == 60:#Red;60;North 
                        print ('North')
                        markers.marker_1()
                        play_stop.play_stop()
                    elif msg.note == 65:#Green;65;South
                        print ('South')
                        markers.marker_2()
                        play_stop.play_stop()
                    elif msg.note == 62:#Blue;62;East
                        print ("East")
                        markers.marker_3()
                        play_stop.play_stop()
                    elif msg.note == 64:#Yellow;64;West
                        print ("West")
                        markers.marker_4()
                        play_stop.play_stop()
                    #print(f'Note On: Note={msg.note} Velocity={msg.velocity}')
                elif msg.type == 'note_off':
                    # Note off messages represent pad releases
                    print(f'Note Off: Note={msg.note}')
                    #print(f'Note Off: Note={msg.note} Velocity={msg.velocity}')
        except KeyboardInterrupt:
                print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()



     