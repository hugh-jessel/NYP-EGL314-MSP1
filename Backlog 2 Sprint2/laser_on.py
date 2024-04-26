import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Setup GPIO21 as output
GPIO.setup(21, GPIO.OUT)

try:
    # Turn on the relay connected to GPIO21
    GPIO.output(21, GPIO.HIGH)
    print('Relay ON - The relay will stay on until the program is terminated.')

    while True:
        time.sleep(10)
finally:
    # This block ensures the GPIO is cleaned up properly when the program is terminated
    GPIO.output(21, GPIO.LOW)  # Turn off the relay
    print('Relay OFF - Cleaning up GPIO.')
    GPIO.cleanup()
