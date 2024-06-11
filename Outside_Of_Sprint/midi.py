import mido
import reaper_markers
import play_stop
import time
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import server_for_Lisa

global count
global directional_var
start_time = None  # Initialize start_time as None

# Reset game variable
North_pressed = 'False'
South_pressed = 'False'
East_pressed  = 'False'
West_pressed  = 'False' 

def process_directional_var(directional_var):
    print(f"Received directional value: {directional_var}")

def game_over():                       
    print('Game over')    
    Lisa_GrandMa3_Functions.stageFail() # Plays 'fail' light sequence
    reaper_markers.fail()  # Jumps to 'fail' soundcue
    time.sleep(8)
    play_stop.play_stop()
    Lisa_GrandMa3_Functions.clear_all()   
    Lisa_GrandMa3_Functions.clear_all()
    exit()  

def deflect_success():
    #show how fast they press button
    global start_time
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(f"{elapsed_time:.2f}")  # Format elapsed time to 2 decimal places
    
    reaper_markers.deflect()  #jumps to 'deflect' audio cue
    
    time.sleep(1)  #lets sound cue playout before jumping 

def Midi_LaunchPad_MK3():           #Main game code
    
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
                server_for_Lisa.catcher()
                server_for_Lisa.server_run()
                # Increment count and sleep for 0.5 seconds|| Starts count for game
                time.sleep(0.5)                            
                count += 0.5
                print(count)
                
                # Check for new MIDI messages
                for msg in inport.iter_pending():
                    global North_pressed
                    global South_pressed
                    global East_pressed
                    global West_pressed
                    
                    if msg.type == 'note_on':  # Note on messages represent pad presses
                        print(f'Note On: Note={msg.note}')
                        
#STAGE1 START          
                        
                        if msg.note == 60 and 0.5 > directional_var > 0.25 and North_pressed == 'False':  
                            # msg.note 60 is the pad for North||Red;60;North      #1
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print('North')
                            deflect_success()
                            
                            North_pressed = 'True'
                            
                            reaper_markers.projectile1()
                            print('Back to projectile')
                        
                        elif msg.note == 60 and 0.5 > directional_var > 0.25 and North_pressed == 'True':
                            
                            pass
                            
                        elif msg.note == 60 and directional_var > 0.26: 
                            # North is pressed but after the timing for reaction,
                            # thus causing a game over
            
                            
                            game_over()
                        
                        elif msg.note == 64 and  1 > directional_var > 0.5 and West_pressed == 'False':  
                            # msg.note 64 is the pad for West||Yellow;64;West    #2
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print("West")
                            deflect_success()
                            West_pressed = 'True'
                            
                            reaper_markers.projectile2()
                        
                        elif msg.note == 64 and  31 >= count >= 29 and West_pressed == 'True':  
                            
                            pass
                            
                        elif msg.note == 64 and (count >= 32 or count in range(24, 28)):
                            
                            game_over()
                        
                        elif msg.note == 62 and 33 >= count >= 29.5 and East_pressed == 'False':  
                            # msg.note 62 is the pad for East||Blue;62;East             #3
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print("East")
                            deflect_success()
                            East_pressed = 'True'
                            
                            reaper_markers.projectile3()
                        
                        elif msg.note == 62 and 33 >= count >= 29.5 and East_pressed == 'True': 
                            
                            pass
                            
                        elif msg.note == 62 and (count >= 34 or count in range(24, 29)):
                            
                            game_over()
                        
                        elif msg.note == 65 and 36 >= count >= 32 and South_pressed == 'False':  
                            # msg.note 65 is the pad for South||Green;65;South        #4
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print('South')
                            deflect_success()
                            South_pressed = 'True'
                        
                        elif msg.note == 65 and 36 >= count >= 33 and South_pressed == 'True':
                            
                            pass
                        
                        elif msg.note == 65 and (count in range(24, 32)):
                            
                        # count more than/equal to 36 or count is between 21 and 30 (inclusive)
                        
                            game_over()

#STAGE1 DONE

#STAGE2 START  
                        
                        elif 53 >= count >= 52:   #Add msg.note condition after
                             
                            print ('deflected')
                            deflect_success()
                            reaper_markers.victory()
                            time.sleep(8)
                            play_stop.play_stop()
                            time.sleep(4)
                            Lisa_GrandMa3_Functions.clear_all()   
                            Lisa_GrandMa3_Functions.clear_all()
                            
                            exit()  
                            #send to next projectile marker
                        
                        elif count >= 54:
                            
                            print ('Failed')
                            game_over() 
                            
                        # ~ elif count 53 >= 52:   #Add msg.note condition after
                             
                            # ~ print ('deflected')
                            # ~ deflect_success()
                            # ~ #send to next projectile marker
                        
                        # ~ elif 54 >= count:
                            
                            # ~ print ('Failed')
                            # ~ game_over() 
                            
                        # ~ elif count 53 >= 52:   #Add msg.note condition after
                             
                            # ~ print ('deflected')
                            # ~ deflect_success()
                            # ~ #send to next projectile marker
                        
                        # ~ elif 54 >= count:
                            
                            # ~ print ('Failed')
                            # ~ game_over() 
                            
                        # ~ elif count 53 >= 52:   #Add msg.note condition after
                                 
                                # ~ print ('deflected')
                                # ~ deflect_success()
                                # ~ #send to next projectile marker
                            
                            # ~ elif 54 >= count:
                                
                                # ~ print ('Failed')
                                # ~ game_over() 
                    
                        # ~ elif count 53 >= 52:   #Add msg.note condition after
                             
                            # ~ print ('deflected')
                            # ~ deflect_success()
                            # ~ #send to next projectile marker
                        
                        # ~ elif 54 >= count:
                            
                            # ~ print ('Failed')
                            # ~ game_over() 
                            
                        # ~ elif count 53 >= 52:   #Add msg.note condition after
                             
                            # ~ print ('deflected')
                            # ~ deflect_success()
                            # ~ #send to next projectile marker
                        
                        # ~ elif 54 >= count:
                            
                            # ~ print ('Failed')
                            # ~ game_over() 
                        
#STAGE2 DONE                     
                    elif msg.type == 'note_off':  # Note off messages represent pad releases
                        
                        print(f'Note Off: Note={msg.note}')
                        
                if count == 41 and South_pressed == 'True': 
                    print('Victory')
                    reaper_markers.victory()
                    Lisa_GrandMa3_Functions.stagePass()
                    time.sleep(6)
                    Lisa_GrandMa3_Functions.clear_all()   
                    # Lisa_GrandMa3_Functions.playing()
                    # Lisa_GrandMa3_Functions.playing()
                    exit()
                    
                elif count >= 27 and North_pressed == 'False':      #If no buttons are pressed after count 25
                    
                    game_over()
                    
                elif count >= 32 and West_pressed == 'False':       #If no buttons are pressed after count 29
                    
                    game_over()
                    
                elif count >= 37 and East_pressed == 'False':       #If no buttons are pressed after count 31
                    
                    game_over()     
                       
                elif count >= 41 and South_pressed == 'False':      #If no buttons are pressed after count 35
                    
                    game_over()
                    
        except KeyboardInterrupt:
            
            print("Stopped listening to MIDI messages.")
        
if __name__ == "__main__":
    Midi_LaunchPad_MK3()
    



    
