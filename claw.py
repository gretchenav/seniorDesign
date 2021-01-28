# Program to use claw that is connected to pi->receiver->controller 
# Inputs: Pin 1 used for clockwise rotation. Pin 2 used for counterclockwise rotation. Pin 3 used for control pin. 
# Outputs: servo controller 


import RPI.GPIO as GPIO
from time import sleep

servoPin = 15

# Set pins here 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN) for clockwise rotation
GPIO.setup(pin2, GPIO.IN) for counter counterwise rotation
GPIO.setup(pin3, GPIO.IN) for control pin 
GPIO.setup(servoPin, GPIO.OUT)

# GPIO 15 for the PWM 
pwm = GPIO.PWM(servoPin, 50) 

i = 5;

# clockwise 
while (GPIO.input(pin1) == 1):
	pwm.ChangeDutyCycle(i)
	i = i+1; 
	if (i == 0):
		break

# counterclockwise 
while (GPIO.input(pin2) == 1):
	pwm(ChangeDutyCycle(i))
	i = i-1;
	if (i == 5):
		break







