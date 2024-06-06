import mido
import reaper_markers
import play_stop
import time
import GrandMa3Messages

global count
start_time = None  # Initialize start_time as None

North_pressed = 'False'
South_pressed = 'False'
East_pressed  = 'False'
West_pressed  = 'False' 

def game_over():                       
    print('Game over')    
    GrandMa3Messages.stageFail() # Plays 'fail' light sequence
    reaper_markers.fail()  # Jumps to 'fail' soundcue
    time.sleep(8)
    play_stop.play_stop()
    GrandMa3Messages.clear_all()   
    GrandMa3Messages.clear_all()
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
                        
#####################################################################################################################
              ################################ STAGE1 START #######################################            
                        
                        if msg.note == 60 and 24 >= count >= 26:  
                            # msg.note 60 is the pad for North||Red;60;North      #1
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print('North')
                            deflect_success()
                            
                            North_pressed = 'True'
                            
                            reaper_markers.projectile1()
                            print('Back to projectile')
                        
                        elif msg.note == 60 and 27 >= count >= 28: 
                            # North is pressed but after the timing for reaction,
                            # thus causing a game over
            
                            
                            game_over()
                        
                        elif msg.note == 64 and 27.5 >= count >= 31:  
                            # msg.note 64 is the pad for West||Yellow;64;West    #2
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print("West")
                            deflect_success()
                            West_pressed = 'True'
                            
                            reaper_markers.projectile2()
                        
                        elif msg.note == 64 and (count >= 32 or count in range(24, 27)):
                            
                            game_over()
                        
                        elif msg.note == 62 and 29.5 >= count >= 33:  
                            # msg.note 62 is the pad for East||Blue;62;East             #3
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print("East")
                            deflect_success()
                            East_pressed = 'True'
                            
                            reaper_markers.projectile3()
                        
                        elif msg.note == 62 and (count >= 34 or count in range(24, 29)):
                            
                            game_over()
                        
                        elif msg.note == 65 and 33 >= count >= 36:  
                            # msg.note 65 is the pad for South||Green;65;South        #4
                            
                            # Count range is for when participant should be pressing the pad to deflect; 
                            
                            # pressing it anytime after should  result in a fail
                            
                            print('South')
                            deflect_success()
                            South_pressed = 'True'
                        
                        elif msg.note == 65 and (count in range(24, 32)):
                            
                        # count more than/equal to 36 or count is between 21 and 30 (inclusive)
                        
                            game_over()

              ################################ STAGE1 DONE #######################################              
#####################################################################################################################

#####################################################################################################################
              ################################ STAGE2 START #######################################           
                        
                        elif 52 >= count >= 53:   #Add msg.note condition after
                             
                            print ('deflected')
                            deflect_success()
                            reaper_markers.victory()
                            time.sleep(8)
                            play_stop.play_stop()
                            time.sleep(4)
                            GrandMa3Messages.clear_all()   
                            GrandMa3Messages.clear_all()
                            
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
                        
              ################################ STAGE2 DONE #######################################              
#####################################################################################################################                        
                    elif msg.type == 'note_off':  # Note off messages represent pad releases
                        
                        print(f'Note Off: Note={msg.note}')
                        
                if count == 38 and South_pressed == 'True':
                    
                    print('Victory')
                    reaper_markers.victory()
                    GrandMa3Messages.stagePass()
                    time.sleep(4)
                    GrandMa3Messages.clear_all()   
                    GrandMa3Messages.playing()
                    GrandMa3Messages.playing()
                    
                elif count >= 26 and North_pressed == 'False':      #If no buttons are pressed after count 25
                    
                    game_over()
                    
                elif count >= 31 and West_pressed == 'False':       #If no buttons are pressed after count 29
                    
                    game_over()
                    
                elif count >= 35 and East_pressed == 'False':       #If no buttons are pressed after count 31
                    
                    game_over()     
                       
                elif count >= 39 and South_pressed == 'False':      #If no buttons are pressed after count 35
                    
                    game_over()
                    
        except KeyboardInterrupt:
            
            print("Stopped listening to MIDI messages.")

if __name__ == "__main__":
    Midi_LaunchPad_MK3()



    
