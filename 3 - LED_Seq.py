import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led=2
led1=3
led2=4
GPIO.setup(led,GPIO.OUT)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
pause_time=0.1
while True:
	GPIO.output(led,1)
	GPIO.output(led1,0)
	GPIO.output(led2,0)
	time.sleep(pause_time)
	GPIO.output(led,0)
	GPIO.output(led1,1)
	GPIO.output(led2,0)
	time.sleep(pause_time)
	GPIO.output(led,0)
	GPIO.output(led1,0)
	GPIO.output(led2,1)
	time.sleep(pause_time)


