import mido
import markers
import play_stop

'''
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
                        #play_stop.play_stop()
                    elif msg.note == 65:#Green;65;South
                        print ('South')
                        markers.marker_2()
                        #play_stop.play_stop()
                    elif msg.note == 62:#Blue;62;East
                        print ("East")
                        markers.marker_3()
                        #play_stop.play_stop()
                    elif msg.note == 64:#Yellow;64;West
                        print ("West")
                        markers.marker_4()
                        #play_stop.play_stop()
                    #print(f'Note On: Note={msg.note} Velocity={msg.velocity}')
                elif msg.type == 'note_off':
                    # Note off messages represent pad releases
                    print(f'Note Off: Note={msg.note} Page={}')
                    #print(f'Note Off: Note={msg.note} Velocity={msg.velocity}')
        except KeyboardInterrupt:
                print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()
'''
# Define custom mode program number (e.g., program 10 for custom mode)
custom_mode_program = 7
custom_mode_channel = 7

CUSTOM_MODE_MESSAGES = [
    [0xF0, 0x00, 0x20, 0x29, 0x02, 0x0D, 0x03, 0x00, 0xF7],  # Custom Mode 0
    [0xF0, 0x00, 0x20, 0x29, 0x02, 0x0D, 0x03, 0x01, 0xF7],  # Custom Mode 1
    # Add messages for Custom Modes 2-7 here
]
def Midi_LaunchPad_MK3():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"

    outport = mido.open_output(LaunchpadPro_Name)
    
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
                    if msg.type == 'note_on' and msg.note == 67:
                        program_change_msg = mido.Message('program_change', program=custom_mode_program)
                        print (program_change_msg)
                        outport.send(mido.Message('sysex', data=byte_data)
                        print("Switching to Custom Mode...")
                    elif msg.note == 60:#Red;60;North 
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
    #Midi_LaunchPad_MK3()