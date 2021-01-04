import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.IN)


while True:
    inp = GPIO.input(18)
    if inp == True:
        print(inp)
        print("motion Detacted")
        GPIO.output(24,True)
        time.sleep(0.5)
        GPIO.output(24,False)
        time.sleep(0.5)

