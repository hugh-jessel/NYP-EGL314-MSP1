import RPi.GPIO as GPIO
import time
import audioowl

data = audioowl.analyze_file(path='INSERT MUSIC FILE LOCATION HERE',sr=22050)

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

def countdown(t):
    while t > 0:
        time.sleep(1)
        t-=1

def onBeat():
    countdowns = countdown(30)
    measure = data['beat_samples']
    while countdowns > 0:
        for beat_sample in measure:
            time.sleep(beat_sample/measure)
            print('At Beat :' + measure)
            laser_off()
            laser_on()

    else:
        laser_off()
        GPIO.cleanup()  