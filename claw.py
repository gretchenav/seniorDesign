# Program to use claw that is connected to pi->receiver->controller 
# Inputs: Pin 1 used for clockwise rotation. Pin 2 used for counterclockwise rotation. Pin 3 used for control pin. 
# Outputs: servo controller 


import RPI.GPIO as GPIO
from time import sleep

# Set Pins Here
servoPin = 0
forwardButton = 0
backwardButton = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(forwardButton, GPIO.IN) # for clockwise rotation
GPIO.setup(backwardButton, GPIO.IN) # for counter counterwise rotation
GPIO.setup(servoPin, GPIO.OUT) # for control pin 

# GPIO servoPin for the PWM with frequency of 50 Hz
pwmServo = GPIO.PWM(servoPin, 50) 
pwmServo.start(0)
i = 2;

# clockwise 
while (GPIO.input(forwardButton) == 1):
	pwmServo.ChangeDutyCycle(i)
	i = i+1; 
	if (i == 12):
		break

# counterclockwise 
while (GPIO.input(backwardButton) == 1):
	pwmServo(ChangeDutyCycle(i))
	i = i-1;
	if (i == 2):
		break







