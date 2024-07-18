# Imports
import mido 
import reaper_markers
import sys
import Lisa_GrandMa3_Functions
from pythonosc import osc_server, dispatcher
import time
import random
import threading

#Variables 
'''
projCount || Track number of projectiles
(int)     || to next stage

gameCount || count for entire game 
(float)           || duration (Used for
           || hard coding)

reactionTiming || count for reaction
(float)      || timing after 
             || projectile is fired

NorthPressed  || Variables to check
SouthPressed  || if a buton has 
EastPressed   || been pressed
WestPressed   ||
(Boolean)     ||

game_fail || variable to check for 
          || game failure; used for
(Boolean) || restarting

direction || for directions
          ||  
          || 
(string)  || 

stageNo || Check for game stage
(int)   ||

#################################
L-ISA Sequences
(L-R,T-B)
#################################
North-
Sequence  29
Sequence 21
Sequence 27
South-
Sequence 28
Sequence - 24
Sequence - 30
East-
Sequence 25
Sequence 23
Sequence
West-
Sequence 
Sequence 22
Sequence 26

#################################
msg.note for each direction
#################################
North = 60
South = 65
East =  62
West = 64
'''
# global variables
projCount = 0
gameCount = 0
NorthPressed = "False"
SouthPressed = "False"
EastPressed = "False"
WestPressed = "False"
game_fail = "False"
direction = ""
stageNo = 1
x = 0.0
#Funtions
def stageClear():
    #global stageNo
    #stageNo += 1
    print("Stage Cleared!")
    reaper_markers.tut_stagepass()
    Lisa_GrandMa3_Functions.stagePass()
    time.sleep(13)
def stageFail():
    global game_fail
    game_fail = "True"
    print("Stage Failed!")
    Lisa_GrandMa3_Functions.stageFail()
    reaper_markers.fail()
    time.sleep(8)
    reaper_markers.play_stop()
    Lisa_GrandMa3_Functions.clear_all()
    Lisa_GrandMa3_Functions.clear_all()
def gameTimeCounter(counting):
    global gameCount
    while counting == "True":
        time.sleep(0.5)
        gameCount += 0.5
        print(f"The game has been going for {gameCount} seconds")
    return gameCount
def reactionTime(reactionTiming):
    global x
    z = 0
    while z in x <= reactionTiming:    
        z += 0.5
        print(f"Projectile was fired {z} seconds ago")
        x = z
        return x
def snapshotsRandom():
    random.randint(1,10)
    if random.randint == 1:
        Lisa_GrandMa3_Functions.Seq21()
        direction = "North"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 2:
        Lisa_GrandMa3_Functions.Seq22()
        direction = "West"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 3:
        Lisa_GrandMa3_Functions.Seq23()
        direction = "East"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 4:
        Lisa_GrandMa3_Functions.Seq24()
        direction = "South"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 5:
        Lisa_GrandMa3_Functions.Seq25()
        direction = "East"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 6:
        Lisa_GrandMa3_Functions.Seq26()
        direction = "West"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 7:
        Lisa_GrandMa3_Functions.Seq27()
        direction = "North"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 8:
        Lisa_GrandMa3_Functions.Seq28()
        direction = "South"
        print(f"Snapshot has been sent to the {direction}")
    elif random.randint == 9:
        Lisa_GrandMa3_Functions.Seq29()
        direction = "North"
        print(f"Snapshot has been sent to the {direction}")
    else:
        Lisa_GrandMa3_Functions.Seq30()
        direction = "South"
        print(f"Snapshot has been sent to the {direction}")
def stg1projectilesRandom():
    if random.randint(1,3) == 1:
        reaper_markers.stg1projectile2()
        print("Stage 1 Projectile 2 is firing")
    elif random.randint(1,3) == 2:
        reaper_markers.stg1projectile3()
        print("Stage 1 Projectile 3 is firing")
    else:
        reaper_markers.stg1projectile4()
        print("Stage 1 Projectile 4 is firing")
def stg2projectilesRandom():
    if random.randint(1,5) == 1:
        reaper_markers.stg2projectile2()
        print("Stage 2 Projectile 2 is firing")
    elif random.randint(1,5) == 2:
        reaper_markers.stg2projectile3()
        print("Stage 2 Projectile 3 is firing")
    elif random.randint(1,5) == 3:
        reaper_markers.stg2projectile4()
        print("Stage 2 Projectile 4 is firing")
    elif random.randint(1,5) == 4:
        reaper_markers.stg2projectile4()
        print("Stage 2 Projectile 4 is firing")
    else:
        reaper_markers.stg2projectile5()
        print("Stage 2 Projectile 5 is firing")
def deflected():
    reaper_markers.deflect()
    #time.sleep(1)
def deflectDirection(direction):
    deflected()
    if direction == "North":
        NorthPressed = "True"
        print(f"Deflected from the {direction}")
        print(f"{direction} has been pressed! {NorthPressed} ")
    elif direction == "South":
        SouthPressed = "True"
        print(f"Deflected from the {direction}")
        print(f"{direction} has been pressed! {SouthPressed} ")
    elif direction == "East":
        EastPressed = "True"
        print(f"Deflected from the {direction}")
        print(f"{direction} has been pressed! {EastPressed} ")
    elif direction == "West":
        WestPressed = "True"
        print(f"Deflected from the {direction}")
        print(f"{direction} has been pressed! {WestPressed} ")
    snapshotsRandom()
    time.sleep(2)
    #stg1projectilesRandom()
def varReset():
    global NorthPressed
    global SouthPressed
    global EastPressed
    global WestPressed
    NorthPressed = "False"
    SouthPressed = "False"
    EastPressed = "False"
    WestPressed = "False"
## Main game function
def launchpad_listen():
    LaunchpadPro_Name = "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0"
    if LaunchpadPro_Name not in mido.get_input_names():
        print(f"Device {LaunchpadPro_Name} not found. Please check the device name")
        return
    with mido.open_input(LaunchpadPro_Name) as inport,mido.open_output(LaunchpadPro_Name) as outport:
        print(f"Listening to {LaunchpadPro_Name} for note messages" )
        global stageNo
        global gameCount 
        global counting
        global direction
        global reactionTiming
        global projCount
        try:
            for msg in inport.iter.pending():
                while True:
                    if msg.type == "note_on":
                        print(f"Note On:Note={msg.note}")
                    elif msg.type == "note_off":
                        print(f"Note Off: Note={msg.note}")
                    if stageNo == 1:
                        while gameCount > 35.0: #Nothing happens before first projectile is heard
                            if gameCount  == 36.0:
                                #snapshotsRandom() [For soft coding]
                                Lisa_GrandMa3_Functions.Seq21() # [North]
                                direction = "North"
                            elif gameCount == 38.0 and direction == "North":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 4
                                reactionTime(reactionTiming)
                                if x < 4 and msg.note == "60": #Under time limit and North pad pressed
                                    projCount += 1
                                    if projCount == 3: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 3: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(2.5)
                                        stg1projectilesRandom()
                                elif (x < 4 and msg.note != "60") or (x == 4 and NorthPressed == "False"): #Either wrong pad pressed or North isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 39:
                                #snapshotsRandom() [For soft coding]
                                Lisa_GrandMa3_Functions.Seq24() # [South]
                                direction = "South"
                            elif gameCount == 40.5 and direction == "South":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 4
                                reactionTime(reactionTiming)
                                if x < 4 and msg.note == "65": #Under time limit and South pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 3: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 3: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(2.5)
                                        stg1projectilesRandom()
                                elif (x < 4 and msg.note != "65") or (x == 4 and SouthPressed == "False"): #Either wrong pad pressed or South isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 42:
                                #snapshotsRandom() [For soft coding]
                                Lisa_GrandMa3_Functions.Seq23() # [East]
                                direction = "East"
                            elif gameCount == 43.5 and direction == "East":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 4
                                reactionTime(reactionTiming)
                                if x < 4 and msg.note == "62": #Under time limit and East pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 3: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 3: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(2.5)
                                        stg1projectilesRandom()
                                elif (x < 4 and msg.note != "62") or (x == 4 and EastPressed == "False"): #Either wrong pad pressed or East isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 45:
                                #snapshotsRandom() [For soft coding]
                                Lisa_GrandMa3_Functions.Seq22() # [West]
                                direction = "West"
                            elif gameCount == 46.5 and direction == "West":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 4
                                reactionTime(reactionTiming)
                                if x < 4 and msg.note == "64": #Under time limit and East pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 3: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 3: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(2.5)
                                        stg1projectilesRandom()
                                elif (x < 4 and msg.note != "64") or (x == 4 and WestPressed == "False"): #Either wrong pad pressed or West isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                    elif stageNo == 2:
                        #Uncomment if errors in stage 2 code
                        """ gameCount = 0
                        counting = "True"
                        gameTimeCounter(counting)
                        if gameCount > 0:
                            stageFail()
                            time.sleep(8) #Change with length of stage fail sound cue
                            Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                            Lisa_GrandMa3_Functions.clear_all()
                            reaper_markers.play_stop()            #Pause audio after fail audio is over
                            exit()  #Comment out and replace when restart feature is implemented """
                
                        #Comment out code below if stage 2 not working and require quick patch
                        #Comment from here#
                        gameCount = 0
                        counting = "True"
                        gameTimeCounter(counting)
                        while gameCount > 0:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq28() # [South]
                            direction = "South"
                        if gameCount == 1.5 and direction == "South":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 3
                            reactionTime(reactionTiming)
                            if x < 3 and msg.note == "65": #Under time limit and South pad pressed
                                global projCount
                                projCount += 1
                                if projCount == 5: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 5: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(3)
                                    stg2projectilesRandom()
                                elif (x < 3 and msg.note != "65") or (x == 3 and SouthPressed == "False"): #Either wrong pad pressed or South isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 3:
                                #snapshotsRandom() [For soft coding]
                                #print(direction)
                                Lisa_GrandMa3_Functions.Seq25() # [East]
                                direction = "East"
                            elif gameCount == 4.5 and direction == "East":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 3
                                reactionTime(reactionTiming)
                                if x < 3 and msg.note == "62": #Under time limit and East pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 5: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 5: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(1.5)
                                        stg2projectilesRandom()
                                elif (x < 3 and msg.note != "62") or (x == 3 and EastPressed == "False"): #Either wrong pad pressed or East isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 5:
                                #snapshotsRandom() [For soft coding]
                                #print(direction)
                                Lisa_GrandMa3_Functions.Seq30() # [South]
                                direction = "South"
                            if gameCount == 6 and direction == "South":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 3
                                reactionTime(reactionTiming)
                                if x < 3 and msg.note == "65": #Under time limit and South pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 5: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 5: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(2.5)
                                        stg2projectilesRandom()
                                elif (x < 3 and msg.note != "65") or (x == 3 and SouthPressed == "False"): #Either wrong pad pressed or South isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 7:
                                #snapshotsRandom() [For soft coding]
                                #print(direction)
                                Lisa_GrandMa3_Functions.Seq22() # [West]
                                direction = "West"
                            if gameCount == 8.5 and direction == "West":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 3
                                reactionTime(reactionTiming)
                                if x < 3 and msg.note == "64": #Under time limit and West pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 5: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 5: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(1)
                                        stg2projectilesRandom()
                                elif (x < 3 and msg.note != "64") or (x == 3 and WestPressed == "False"): #Either wrong pad pressed or West isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            elif gameCount == 9.0:    
                                #snapshotsRandom() [For soft coding]
                                #print(direction)
                                Lisa_GrandMa3_Functions.Seq27() # [North]
                                direction = "North"
                            elif gameCount == 9.5 and direction == "North":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 4
                                reactionTime(reactionTiming)
                                if x < 3 and msg.note == "60": #Under time limit and North pad pressed
                                    projCount += 1
                                    if projCount == 5: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 5: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(3)
                                        stg2projectilesRandom()
                                elif (x < 3 and msg.note != "60") or (x == 3 and NorthPressed == "False"): #Either wrong pad pressed or North isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                            # elif gameCount == 11.0:
                            #     #snapshotsRandom() [For soft coding]
                            #     #print(direction)
                            #     Lisa_GrandMa3_Functions.Seq22() # [West]
                            #     direction = "West"
                            # if gameCount == 12 and direction == "West":
                            #     counting = "False"
                            #     gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            #     reactionTiming = 3
                            #     reactionTime(reactionTiming)
                            #     if x < 3 and msg.note == "64": #Under time limit and West pad pressed
                            #         global projCount
                            #         projCount += 1
                            #         if projCount == 5: #Enough projectiles deflected to beat stage
                            #             deflectDirection(direction)
                            #             stageClear()
                            #             stageNo += 1
                            #             print(stageNo)
                            #         elif projCount < 5: #Not enough proctiles deflected to beat stage
                            #             deflectDirection(direction)
                            #             counting = "True"
                            #             gameTimeCounter(counting)
                            #             time.sleep(1)
                            #             stg2projectilesRandom()
                            #     elif (x < 3 and msg.note != "64") or (x == 3 and WestPressed == "False"): #Either wrong pad pressed or West isn't pressed under time limit
                            #         stageFail()
                            #         time.sleep(8) #Change with length of stage fail sound cue
                            #         Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                            #         Lisa_GrandMa3_Functions.clear_all()
                            #         reaper_markers.play_stop()            #Pause audio after fail audio is over
                            #         exit()  #Comment out and replace when restart feature is implemented
                    #To here#
                    elif stageNo == 3:            
                         #Uncomment if errors in stage 3 code
                        """ gameCount = 0
                        counting = "True"
                        gameTimeCounter(counting)
                        if gameCount > 0:
                            stageFail()
                            time.sleep(8) #Change with length of stage fail sound cue
                            Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                            Lisa_GrandMa3_Functions.clear_all()
                            reaper_markers.play_stop()            #Pause audio after fail audio is over
                            exit()  #Comment out and replace when restart feature is implemented """
                
                        #Comment out code below if stage 2 not working and require quick patch
                        #Comment from here#
                        gameCount = 0
                        counting = "True"
                        gameTimeCounter(counting)
                        while gameCount > 0:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq22() # [West]
                            direction = "West"
                        if gameCount == 0.5 and direction == "West":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 2
                            reactionTime(reactionTiming)
                            if x < 3 and msg.note == "64": #Under time limit and West pad pressed
                                global projCount
                                projCount += 6
                                if projCount == 5: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 6: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(2)
                                    stg2projectilesRandom()
                            elif (x < 2 and msg.note != "64") or (x == 2 and WestPressed == "False"): #Either wrong pad pressed or West isn't pressed under time limit
                                stageFail()
                                time.sleep(8) #Change with length of stage fail sound cue
                                Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                Lisa_GrandMa3_Functions.clear_all()
                                reaper_markers.play_stop()            #Pause audio after fail audio is over
                                exit()  #Comment out and replace when restart feature is implemented
                        elif gameCount == 1.5:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq25() # [East]
                            direction = "East"
                        elif gameCount == 3 and direction == "East":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 2
                            reactionTime(reactionTiming)
                            if x < 2 and msg.note == "62": #Under time limit and East pad pressed
                                global projCount
                                projCount += 1
                                if projCount == 6: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 6: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(3)
                                    stg2projectilesRandom()
                            elif (x < 2 and msg.note != "62") or (x == 2 and EastPressed == "False"): #Either wrong pad pressed or East isn't pressed under time limit
                                stageFail()
                                time.sleep(8) #Change with length of stage fail sound cue
                                Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                Lisa_GrandMa3_Functions.clear_all()
                                reaper_markers.play_stop()            #Pause audio after fail audio is over
                                exit()  #Comment out and replace when restart feature is implemented
                        elif gameCount == 4:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq29() # [North]
                            direction = "North"
                        elif gameCount == 6 and direction == "North":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 3
                            reactionTime(reactionTiming)
                            if x < 2 and msg.note == "60": #Under time limit and North pad pressed
                                projCount += 1
                                if projCount == 6: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 5: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(1)
                                    stg2projectilesRandom()
                            elif (x < 2 and msg.note != "60") or (x == 2 and NorthPressed == "False"): #Either wrong pad pressed or North isn't pressed under time limit
                                stageFail()
                                time.sleep(8) #Change with length of stage fail sound cue
                                Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                Lisa_GrandMa3_Functions.clear_all()
                                reaper_markers.play_stop()            #Pause audio after fail audio is over
                                exit()  #Comment out and replace when restart feature is implemented
                        elif gameCount == 6.5:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq24() # [South]
                            direction = "South"
                        elif gameCount == 7 and direction == "South":
                                counting = "False"
                                gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                                reactionTiming = 2
                                reactionTime(reactionTiming)
                                if x < 2 and msg.note == "65": #Under time limit and South pad pressed
                                    global projCount
                                    projCount += 1
                                    if projCount == 5: #Enough projectiles deflected to beat stage
                                        deflectDirection(direction)
                                        stageClear()
                                        stageNo += 1
                                        print(stageNo)
                                    elif projCount < 6: #Not enough proctiles deflected to beat stage
                                        deflectDirection(direction)
                                        counting = "True"
                                        gameTimeCounter(counting)
                                        time.sleep(3.5)
                                        stg2projectilesRandom()
                                elif (x < 2 and msg.note != "65") or (x == 2 and SouthPressed == "False"): #Either wrong pad pressed or South isn't pressed under time limit
                                    stageFail()
                                    time.sleep(8) #Change with length of stage fail sound cue
                                    Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                    Lisa_GrandMa3_Functions.clear_all()
                                    reaper_markers.play_stop()            #Pause audio after fail audio is over
                                    exit()  #Comment out and replace when restart feature is implemented
                        elif gameCount == 9:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq26() # [West]
                            direction = "West"
                        elif gameCount == 10.5 and direction == "West":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 2
                            reactionTime(reactionTiming)
                            if x < 2 and msg.note == "64": #Under time limit and West pad pressed
                                global projCount
                                projCount += 1
                                if projCount == 6: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 6: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(5)
                                    stg2projectilesRandom()
                            elif (x < 2 and msg.note != "64") or (x == 2 and WestPressed == "False"): #Either wrong pad pressed or West isn't pressed under time limit
                                stageFail()
                                time.sleep(8) #Change with length of stage fail sound cue
                                Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                Lisa_GrandMa3_Functions.clear_all()
                                reaper_markers.play_stop()            #Pause audio after fail audio is over
                                exit()  #Comment out and replace when restart feature is implemented
                        elif gameCount == 14:
                            #snapshotsRandom() [For soft coding]
                            Lisa_GrandMa3_Functions.Seq24() # [South]
                            direction = "South"
                        elif gameCount == 15.5 and direction == "South":
                            counting = "False"
                            gameTimeCounter(counting) #Stops gameCount from incrementing while deflect code is running
                            reactionTiming = 2
                            reactionTime(reactionTiming)
                            if x < 2 and msg.note == "65": #Under time limit and South pad pressed
                                global projCount
                                projCount += 1
                                if projCount == 5: #Enough projectiles deflected to beat stage
                                    deflectDirection(direction)
                                    stageClear()
                                    stageNo += 1
                                    print(stageNo)
                                elif projCount < 6: #Not enough proctiles deflected to beat stage
                                    deflectDirection(direction)
                                    counting = "True"
                                    gameTimeCounter(counting)
                                    time.sleep(3.5)
                                    stg2projectilesRandom()
                            elif (x < 2 and msg.note != "65") or (x == 2 and SouthPressed == "False"): #Either wrong pad pressed or South isn't pressed under time limit
                                stageFail()
                                time.sleep(8) #Change with length of stage fail sound cue
                                Lisa_GrandMa3_Functions.clear_all()   #Clear lights after fail audio is over
                                Lisa_GrandMa3_Functions.clear_all()
                                reaper_markers.play_stop()            #Pause audio after fail audio is over
                                exit()  #Comment out and replace when restart feature is implemented
                        
                        #To here#
        except KeyboardInterrupt:
            print("stopped listening to MIDI messages.")
            
if __name__ == "__main__":
    
    launchpad_listen()