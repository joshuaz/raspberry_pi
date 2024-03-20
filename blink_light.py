import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

def blink_led(pin, duration):
    GPIO.setup(pin, GPIO.OUT)
    try:
        start_time = time.time()

        while time.time() - start_time < duration:
            GPIO.output(pin, GPIO.HIGH)  # Turn on the LED
            time.sleep(0.5)  # Sleep for 0.5 seconds
            GPIO.output(pin, GPIO.LOW)   # Turn off the LED
            time.sleep(0.5)  # Sleep for 0.5 seconds

    finally:
        GPIO.cleanup()

# Blink GPIO 17 for 15 seconds
blink_led(17, 15)
