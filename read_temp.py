import time
import board
import digitalio
import adafruit_dht

# Sensor data pin is connected to GPIO 4
print(adafruit_dht.DHT11)
sensor = adafruit_dht.DHT11(board.D4)
humidifier = digitalio.DigitalInOut(board.D17)
humidifier.direction = digitalio.Direction.OUTPUT

def press_button():
    # this is the equivalent of pressing the button for ~.5 seconds
    humidifier.value = True
    time.sleep(.5)
    humidifier.value = False

def turn_on():
    # this is the equivalent of pressing the button once
    press_button()

def turn_off():
    # this is the equivalent of pressing the button twice
    press_button()
    press_button()

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        if humidity is not None:
            if humidity < 70:
                print("humidity is less than 70")
                turn_on()
                time.sleep(10)  # Keep humidifier on for 10 seconds
                turn_off()
            break
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    attempts += 1
    time.sleep(2.0)

if attempts == max_attempts:
    print("Failed to get humidity after {} attempts".format(max_attempts))
