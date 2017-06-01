#!/usr/bin/python
 
# Python Standart Library Imports

import PWMFile
import ConstantsFile

# Initialization of classes from local files

PWM = PWMFile.PWMClass()
Pconst = ConstantsFile.Constants()


class MotorsControlClass():
    
    def MotorsControl(self,rightMotor, leftMotor):
		# Sending the values to the pwm controller that is connected to the motors
		PWM.PWM_Signals(round(rightMotor, 2), round(leftMotor, 2))
