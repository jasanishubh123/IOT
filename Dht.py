import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D8)
while True:
    try:
        print(dhtDevice)
        temperature_c=dhtDevice.temperature
        temperature_f=temperature_c*(9/5)+32
        humidity=dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} c Humidity: {}% ". format(temperature_f,temperature_c,humidity))
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2.0)