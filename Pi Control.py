import Rpi.GPIO as GPIO

#Joystick Control Pins (pick numbers still)
controlArmForward = 0
controlArmBackward = 0
controlClawOpen = 0
controlClawClose = 0
#Camera pan perhaps

#Component Control Pins (pick numbers still)
armForward = 0
armBackward = 0
clawOpen = 0
clawClose = 0
#Camera pan perhaps

#Set up pins
GPIO.setup(controlArmForward, GPIO.IN)
GPIO.setup(controlArmBackward, GPIO.IN)
GPIO.setup(armForward, GPIO.OUT)
GPIO.setup(armBackward, GPIO.OUT)

GPIO.setup(controlClawOpen, GPIO.IN)
GPIO.setup(controlClawClose, GPIO.IN)
GPIO.setup(clawOpen, GPIO.OUT)
GPIO.setup(clawClose, GPIO.OUT)
#Camera setup pins

#Control Algorithm
while(True):
    if(controlArmForward == 1): #Arm Extension
        #set ArmForward pin to 1 (true value outputs max 3.3v)
        while(controlArmForward == 1):
            pass
        #set pin back to 0 once done
        
    if(controlArmBackward == 1): #Arm Retraction
        #set ArmBackward pin to 1 (true value outputs max 3.3v)
        while(controlArmBackward == 1):
            pass
        #set pin back to 0v once done

    if(controlClawOpen == 1):
        #turn servo slowly to max threshold

    if(controlClawClose == 1):
        #turn servo slowly to min threshold

    #stuff for camera pan/tilt
        
#end
    
    


















        
