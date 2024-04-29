import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Setup GPIO21 as output
GPIO.setup(21, GPIO.OUT)

# Turn on the relay connected to GPIO21
GPIO.output(21, GPIO.HIGH)
print('Relay ON - The relay will stay on until the program is terminated.')
