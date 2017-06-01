#!/usr/bin/python

# Constants used in the algorithm
class Constants:
    def __init__(self):
	self.PWM_Freq = 100
	#self.PWM_L_DIR = "P9_14"
	self.PWM_L_PWM = "P9_22"
	self.L_POS = #"pin..."
	self.L_NEG = #"pin..."
	self.PWM_R_PWM = "P9_16"
	self.R_POS = #"pin..."
	self.R_NEG = #"pin..."
	self.rad_to_deg = 57.29578
	self.Angle_offset = 5
	self.GYR_offset = -0.3
        self.PWM_KpV = 80
        self.PWM_KiV = 0.3
        self.PWM_KdV = 300
        self.PWM_KpA = 5
        self.PWM_KiA = 1.5
        self.PWM_KdA = -0.2
	self.limitV = 1000 
        self.limitA = 1000 
        self.integrated_error_V1 = 0
        self.integrated_error_V2 = 0
        self.integrated_error_A1 = 0
        self.integrated_error_A2 = 0
        self.last_error_V1 = 0
        self.last_error_V2 = 0
        self.last_error_A1 = 0
        self.last_error_A2 = 0
        self.MinRedLiPo = 20
        self.AnalogPinLiPo = "P9_40"

