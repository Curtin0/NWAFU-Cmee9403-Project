import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 
GPIO.cleanup()

GPIO_IN=25 

def init(): 
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(GPIO_IN,GPIO.IN) 
	
def run(): 
	while True: 
		inValue=GPIO.input(GPIO_IN)
		if inValue!=0:
          print("补给机构需要填枣")
time.sleep(2)

		else:
			print("补给机构正常运行")
time.sleep(2)
 
init()
run()

GPIO.cleanup()