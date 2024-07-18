#Imports
import Lisa_GrandMa3_Functions
import reaper_markers
import time
import play_stop
import random

#definitions
def game_over():
    print("Game Over")
    Lisa_GrandMa3_Functions.stageFail()
    reaper_markers.fail()
    time.sleep(8)
    play_stop.play_stop()
    Lisa_GrandMa3_Functions.clear_all()
    Lisa_GrandMa3_Functions.clear_all()
    
def nextstage():
    print("Stage cleared!")
    reaper_markers.tut_stagepass()
    Lisa_GrandMa3_Functions.stagePass()
    time.sleep(13)
    stage2 = "True"
    
def North_deflect():
    deflect_success()
    snapshots()
    time.sleep(2)
    projectiles()

def South():
    deflect_success()
    SouthPressed = "True"
    print("South deflected")
    countT_stop()
    snapshots()
    time.sleep(2)
    projectiles()

def East():
    deflect_success()
    EastPressed = "True"
    print("East deflected")
    countT_stop()
    snapshots()
    time.sleep(2)
    projectiles()

def West():
    deflect_success()
    WestPressed = "True"
    print("West deflected")
    countT_stop()
    snapshots()
    time.sleep(2)
    projectiles()
    
def countT_stop(count_timing):
    print("count_timing Stopped")
    count = 0
    print(count)
    return count
def deflect_success():
    reaper_markers.deflect()
    time.sleep(1)

def resetVar():
    NorthPressed = "False"
    SouthPressed = "False"
    EastPressed = "False"
    WestPressed = "False"

def projectiles():
    if random.randint(1,3) == 1:
        reaper_markers.projectile1()
    elif random.randint(1,3) == 2:
        reaper_markers.projectile2()
    else:
        reaper_markers.projectile3()  

def snapshots():
    random.randint(1,10)
    if random.randint == 1:
        Lisa_GrandMa3_Functions.Seq21()
        directional_Var = "North"
    elif random.randint == 2:
        Lisa_GrandMa3_Functions.Seq22()
        directional_Var = "West"
    elif random.randint == 3:
        Lisa_GrandMa3_Functions.Seq23()
        directional_Var = "East"
    elif random.randint == 4:
        Lisa_GrandMa3_Functions.Seq24()
        directional_Var = "South"
    elif random.randint == 5:
        Lisa_GrandMa3_Functions.Seq25()
        directional_Var = "East"
    elif random.randint == 6:
        Lisa_GrandMa3_Functions.Seq26()
        directional_Var = "West"
    elif random.randint == 7:
        Lisa_GrandMa3_Functions.Seq27()
        directional_Var = "North"
    elif random.randint == 8:
        Lisa_GrandMa3_Functions.Seq28()
        directional_Var = "South"
    elif random.randint == 9:
        Lisa_GrandMa3_Functions.Seq29()
        directional_Var = "North"
    else:
        Lisa_GrandMa3_Functions.Seq30()
        directional_Var = "South"