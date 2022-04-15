import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.output(35,1)
time.sleep(0.5)
GPIO.output(35,0)
time.sleep(0.5)

GPIO.cleanup()