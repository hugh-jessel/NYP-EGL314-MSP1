import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Setup GPIO21 as output
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.LOW)  # Turn off the relay
print('Relay OFF - Cleaning up GPIO.')
GPIO.cleanup()