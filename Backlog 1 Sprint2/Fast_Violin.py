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
        time.sleep(beat_gap)
        count += 1
        if count % 2 == 0:
            laser_on()
        elif count == 2:
            laser_off()
        else:
            laser_on()
    print(f"Counted {count} beats in {duration} seconds.")
    laser_off()