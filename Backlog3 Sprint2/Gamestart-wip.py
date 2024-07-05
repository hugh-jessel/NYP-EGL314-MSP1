import mido
import play_stop
import reaper_markers
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import time
import threading

global count
global directional_var

receiver_ip = "0.0.0.0"                                                                              #Initializing OSC Server
receiver_port = 7123
    
def game_over():                       
    print('Game over')    
    Lisa_GrandMa3_Functions.stageFail() # Plays 'fail' light sequence
    reaper_markers.fail()  # Jumps to 'fail' soundcue
    time.sleep(8)
    play_stop.play_stop()
    Lisa_GrandMa3_Functions.clear_all()   
    Lisa_GrandMa3_Functions.clear_all()
    exit()  


## e.g North = 0.25318267941474915
## when directional_var = North, look for note press = 60
## Function for count / count stop
#
# How to send marker on reaper back to next projectile without hard coding?
# Assign markers with incremental values and call based on increasing numbers? 
# ^ but what if I need to reuse markers? randomize?



def print_args(addr, *args):

        if addr == "/ext/src/72/p":
            print(args[0])
            directional_var = args[0]
            print("Doing task here...")
                    
def count_start():
    print('Count start')
    time.sleep(0.5)                            
    count += 0.5
    print(count)
    
def count_stop():
    print('Count stop')
    count = 0
    print(count)

def deflect_success():
    #show how fast they press button
    global start_time
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(f"{elapsed_time:.2f}")  # Format elapsed time to 2 decimal places
    
    reaper_markers.deflect()  #jumps to 'deflect' audio cue
    
    time.sleep(1)  #lets sound cue playout before jumping 

def launchpad():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"                                  #Initializing Launchpad
    
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return
        
    with mido.open_input(LaunchpadPro_Name) as inport, mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")                
        while True:
            for msg in inport:
            
                for msg in inport.iter_pending():
                
                    global game_start
                    North_pressed = 'False'
                    South_pressed = 'False'
                    East_pressed = 'False'
                    West_pressed = 'False'
                    
                    # global NorthVal
                    # global SouthVal
                    # global EastVal
                    # global WestVal
                    
                    NorthVal = float(0.25318267941474915)
                    SouthVal = float(0.5)
                    EastVal = float(0.75)
                    WestVal = float(1)
                    
                    game_start = 'True'
                    
                    if msg.type == 'note_on':  # Note on messages represent pad presses
                        print(f'Note On: Note={msg.note}')

                        if msg.note == 67:            #Start
                            print ('Game Start')
                            
                            play_stop.play_stop() # Stop any currently playing track 
                            Lisa_GrandMa3_Functions.clear_all()     
                            Lisa_GrandMa3_Functions.clear_all()
                            time.sleep(0.1)
                            Lisa_GrandMa3_Functions.playing()
                            Lisa_GrandMa3_Functions.playing()
                            reaper_markers.startMk()
                        
                            if directional_var == NorthVal and North_pressed != 'True':
                                count_start()
                                if msg.note == 60 and count < 3:
                                    # msg.note 60 is the pad for North||Red;60;North      #1 
                                    #Directional Var is sent from Lisa and taken to determine which pad was pressed;
                                    # pressing it anytime after should  result in a fail
                                    print('North')
                                    deflect_success()
                                    North_pressed = 'True'
                                    reaper_markers.projectile1()
                                    print('Back to projectile') 
                                    count_stop()
                                else:
                                    game_over()
                            elif directional_var == NorthVal and North_pressed == 'True':
                                pass
                            
                            elif directional_var == SouthVal and South_pressed != 'True':
                                count_start()
                                if msg.note == 65 and count < 3:
                                    
                                    print("South")
                                    deflect_success()
                                    South_pressed = 'True'
                                    count_stop()
                                    
                            elif directional_var == SouthVal and South_pressed == 'True':
                                pass
                            
                            elif directional_var == EastVal and East_pressed != 'True':
                                count_start()
                                if msg.note == 62 and count < 3:
                                    print("East")
                                    deflect_success()
                                    East_pressed = 'True'
                                    reaper_markers.projectile2()
                                    print('Back to projectile') 
                                    count_stop()
                                    
                            elif directional_var == SouthVal and East_pressed == 'True':
                                pass
                            
                            elif directional_var == WestVal and West_pressed != 'True':
                                count_start()
                                if msg.note == 64 and count < 3:
                                    print("West")
                                    deflect_success()
                                    West_pressed = 'True'
                                    reaper_markers.projectile3()
                                    print('Back to projectile') 
                                    count_stop()
                                    
                            elif directional_var == WestVal and West_pressed == 'True':
                                pass
                            
                        elif msg.note == 67 and game_start == 'True':
                            pass
                    elif msg.type == 'note_off' and game_start == 'True' and ((North_pressed,East_pressed,West_pressed,South_pressed) != 'True') and (directional_var ==(NorthVal, SouthVal, EastVal, WestVal)):
                        game_over()
                            
def lisa_listen():
    global dispatcher
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/print" is received, message_handler function will run
    server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
    print("serving on{}".format(server.server_address))
    server.serve_forever()
              

LP = threading.Thread(target=launchpad)
#LL = threading.Thread(target=lisa_listen, args=('directional_var'))
LL = threading.Thread(target=lisa_listen)
LL.start()
LP.start()

    
# ~ if __name__ == "__main__":
	
    # ~ LP = threading.Thread(target=launchpad)
    # ~ #LL = threading.Thread(target=lisa_listen, args=('directional_var'))
    # ~ LL = threading.Thread(target=lisa_listen)
    # ~ LP.start()
    # ~ LL.start()
