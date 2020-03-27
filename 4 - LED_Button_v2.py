import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led=2
button=3
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(led,0)
while True:
	input_state = GPIO.input(button)
	if input_state==0:
		GPIO.output(led,1)
		print("LED ON")
	else:
		GPIO.output(led,0)
		print("LED OFF")
