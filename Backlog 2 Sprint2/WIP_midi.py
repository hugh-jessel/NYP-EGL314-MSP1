import mido
import Repear_markers
import play_stop
import time

start_time = time.time()

def game_over():
    print ('Too slow')
    Repear_markers.startMk()                                #Send back to the start
    play_stop.play_stop()                              #To pause / not let the game immediately repeat
    exit()                                  #Stop midi.py
    
def deflect_success():
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    
    #Send to deflect marker
    count_aftDef = 0
    count = 0
    count_aftDef += 0.5
    if count_aftDef == 0.5:
        count == 0

def Midi_LaunchPad_MK3():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name.")
        return

    with mido.open_input(LaunchpadPro_Name) as inport:
        print(f"Listening to {LaunchpadPro_Name} for note messages...")
        count = 0
        try:
            while True: 
                for msg in inport:
                    count += 1
                    print(count)
                    time.sleep(0.5)
                    if msg.type == 'note_on':                                  # Note on messages represent pad presses
                        print(f'Note On: Note={msg.note}')
                        if msg.note == 60 and count <= 5:                      #Red;60;North
    
                            print ('North pressed')
    
                            deflect_success()
    
                            #Send to attack marker
    
                        elif msg.note == 60 and count >= 5:
                            game_over()
    
    
                        elif msg.note == 65 and count <= 7:                                   #Green;65;South
    
                            print ('South')
                            deflect_success()
                            #Send to attack marker
    
                        elif msg.note == 65 and count >= 7:
    
                            game_over()
    
                        elif msg.note == 62 and count <= 9:                                  #Blue;62;East
                            print ("East")
                            deflect_success()
                            #send to attack marker
    
                        elif msg.note == 62 and count >= 9:
    
                            game_over()
    
                        elif msg.note == 64 and count <= 13:                                #Yellow;64;West
                            print ("West")
                            deflect_success()
                            #Send to attack marker
    
                        elif msg.note == 64 and count >= 13:
    
                            game_over()
            
            # try:
                # for msg in inport:
                    # if msg.type == 'note_on':
                        # print(f'Note On: Note={msg.note}')
                        # if msg.note == 60:                   #North ,Red
                            # print('North pressed')
                            # Repear_markers.startMk()
                        # elif msg.note == 65:                 #South ,Green
                            # print('South pressed')
                            # Repear_markers.startMk()
                        # elif msg.note == 62:                 #East ,Yellow
                            # print('East pressed')
                            # Repear_markers.startMk()
                        # elif msg.note == 64:                 #West , Blue
                            # print('West pressed')
                            # Repear_markers.startMk()
                
                        
                    elif msg.type == 'note_off':                         # Note off messages represent pad releases
                        
                        print(f'Note Off: Note={msg.note}')
                                
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")
        
#if __name__ == "__main__":
#Midi_LaunchPad_MK3()

# while True:
    # count += 1
    # print (count)
    # time.sleep(.7)