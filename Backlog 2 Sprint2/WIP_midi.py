import mido
import reaper_markers
import play_stop
import time

global count
start_time = None  # Initialize start_time as None

North_pressed = 'False'
South_pressed = 'False'
East_pressed  = 'False'
West_pressed  = 'False' 

def game_over():
    print('Game over')
    reaper_markers.fail()  # Send back to the start
    exit()  # Stop midi.py

def deflect_success():
    #show how fast they press button
    global start_time
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(f"{elapsed_time:.2f}")  # Format elapsed time to 2 decimal places
    
    reaper_markers.deflect()  #play deflect audio cue
    time.sleep(1)

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
                # Increment count and sleep for 1 seconds
                time.sleep(1)
                count += 1
                print(count)
                
                # Check for new MIDI messages
                for msg in inport.iter_pending():
                    global North_pressed
                    global South_pressed
                    global East_pressed
                    global West_pressed
                    if msg.type == 'note_on':  # Note on messages represent pad presses
                        print(f'Note On: Note={msg.note}')
                        #North
                        if msg.note == 60 and 24 >= count >= 21:  # Red;60;North      #1
                            # count more than/equal to 21 or less than/equal to 24
                            print('North pressed')
                            deflect_success()
                            
                            North_pressed = 'True'
                            
                            reaper_markers.projectile2()
                            print('Back to projectile')
                        
                        elif msg.note == 60 and 25 <= count <= 35:
                            # count more than/equal to 25 or less than/equal to 37
                            game_over()
                        #North last
                        
                        #South
                        elif msg.note == 65 and 29 <= count <= 33:  # Green;65;South        #4
                            # count more than/equal to 29 or less than/equal to 36
                            print('South')
                            deflect_success()
                            South_pressed = 'True'
                        
                        elif msg.note == 65 and (count >= 36 or count in range(21, 34)):
                        # count more than/equal to 36 or count is between 21 and 30 (inclusive)
                            game_over()
                        #south last
                        
                        #East
                        elif msg.note == 62 and 27 <= count <= 30:  # Blue;62;East             #3
                            # count more than/equal to 27 or less than/equal to 32
                            print("East")
                            deflect_success()
                            East_pressed = 'True'
                            
                            reaper_markers.projectile4()
                        
                        elif msg.note == 62 and (34 >= count >= 31 or count in range(21, 26)):
                            game_over()
                        #east last
                        
                        #west
                        elif msg.note == 64 and 23 <= count <= 28:  # Yellow;64;West    #2
                            # count more than/equal to 23 or less than/equal to 28
                            print("West")
                            deflect_success()
                            West_pressed = 'True'
                            
                            reaper_markers.projectile3()
                        
                        elif msg.note == 64 and (34 >= count >= 28 or count in range(21, 27)):
                            # count more than/equal to 37 or less than/equal to 29
                            game_over()
                            
                            #west last
                            
                    elif msg.type == 'note_off':  # Note off messages represent pad releases
                        print(f'Note Off: Note={msg.note}')
                        
                if count >= 35:
                    print('Victory')
                    reaper_markers.victory()
                    exit()
                elif count >= 25 and North_pressed == 'False':      #If no buttons are pressed after count 25
                    game_over()
                elif count >= 29 and West_pressed == 'False':       #If no buttons are pressed after count 29
                    game_over()
                elif count >= 31 and East_pressed == 'False':       #If no buttons are pressed after count 31
                    game_over()        
                elif count >= 34 and South_pressed == 'False':      #If no buttons are pressed after count 35
                    game_over()
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()