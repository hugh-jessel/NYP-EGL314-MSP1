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

def onBeat():
    beat = [1,2,3,4]
    measure = 1
    while True:
        for i in beat:
            time.sleep(1)
            print('At Beat :' + measure)
        measure = measure + 1

        if measure == 1:
            laser_on