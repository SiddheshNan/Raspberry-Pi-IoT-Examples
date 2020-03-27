import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led1=2

GPIO.setup(led1,GPIO.OUT)

while True:
	GPIO.output(led1,1)
	time.sleep(1)
	GPIO.output(led1,0)
	time.sleep(1)	

	

