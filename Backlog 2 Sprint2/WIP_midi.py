import mido
import reaper_markers
import play_stop
import time

start_time = None  # Initialize start_time as None

def game_over():
    print('Too slow')
    reaper_markers.fail()  # Send back to the start
    #play_stop.play_stop()  # To pause / not let the game immediately repeat
    exit()  # Stop midi.py

def deflect_success():
    global start_time
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(f"{elapsed_time:.2f}")  # Format elapsed time to 2 decimal places
    reaper_markers.deflect()
    time.sleep(1.2)

def Midi_LaunchPad_MK3():
    global start_time
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return

    with mido.open_input(LaunchpadPro_Name) as inport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")
        count = 0
        start_time = time.time()  # Set start_time when the loop starts
        try:
            while True:
                # Increment count and sleep for 0.5 seconds
                time.sleep(1)
                count += 1
                print(count)
                
                # Check for new MIDI messages
                for msg in inport.iter_pending():
                    if msg.type == 'note_on':  # Note on messages represent pad presses
                        print(f'Note On: Note={msg.note}')
                        if msg.note == 60 and count <= 15:  # Red;60;North
                            print('North pressed')
                            deflect_success()
                            
                            time.sleep(.5)
                            
                            reaper_markers.attackMk()
                        
                        elif msg.note == 60 and count >= 16:
                            game_over()
                        elif msg.note == 65 and count <= 20:  # Green;65;South
                            print('South')
                            ddeflect_success()
                            
                            time.sleep(.5)
                            
                            reaper_markers.attackMk()
                        
                        elif msg.note == 65 and count >= 21:
                            game_over()
                        elif msg.note == 62 and count <= 30:  # Blue;62;East
                            print("East")
                            deflect_success()
                            
                            time.sleep(.5)
                            
                            reaper_markers.attackMk()
                        
                        elif msg.note == 62 and count >= 31:
                            game_over()
                        elif msg.note == 64 and count <= 40:  # Yellow;64;West
                            print("West")
                            deflect_success()
                            
                            time.sleep(.5)
                            
                            reaper_markers.attackMk()
                        
                        elif msg.note == 64 and count >= 41:
                            game_over()
                        elif count == 50:
                            print("Victory")
                            #send to win marker
                    elif msg.type == 'note_off':  # Note off messages represent pad releases
                        print(f'Note Off: Note={msg.note}')
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()