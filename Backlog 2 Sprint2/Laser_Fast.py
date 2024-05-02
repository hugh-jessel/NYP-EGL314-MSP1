import RPi.GPIO as GPIO
import time

def laser_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    GPIO.output(21, GPIO.LOW)

def laser_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    GPIO.output(21, GPIO.HIGH)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()  

def counter(bpm, duration):
    beat_gap = 60/bpm # Time interval between beats
    count = 0
    start_time = time.time()
    while time.time() - start_time < duration :
        laser_on()
        time.sleep(beat_gap)
        count += 1
        laser_off()
    print(f"Counted {count} beats in {duration} seconds.")

def onBeat():
    counter(70,30)