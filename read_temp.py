import time
import board
import digitalio
import adafruit_dht

# Sensor data pin is connected to GPIO 4
print(adafruit_dht.DHT11)
sensor = adafruit_dht.DHT11(board.D4)
humidifier = digitalio.DigitalInOut(board.D17)
humidifier.direction = digitalio.Direction.OUTPUT

humidifier_on = False

def press_button():
    global humidifier_on  # Declare humidifier_on as global
    # this is the equivalent of pressing the button for ~.5 seconds
    humidifier.value = True
    time.sleep(.5)
    # humidifier.value = False

def turn_on():
    global humidifier_on  # Declare humidifier_on as global
    # this is the equivalent of pressing the button once IF humidifier is not on
    if not humidifier_on:
        press_button()
        humidifier_on = True

def turn_off():
    global humidifier_on  # Declare humidifier_on as global
    # this is the equivalent of pressing the button twice IF the humidifier is on
    if humidifier_on:
        press_button()
        press_button()
        humidifier_on = False

while True:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        if (humidity < 70):
            print("humidity is less than 70")
            turn_on()
        else:
            turn_off()
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)