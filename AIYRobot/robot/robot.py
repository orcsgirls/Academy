#-------------------------------------------------------------------------------
# Simple robot class for our AIY robot
# (c) ORCSGirls Academy, 2022
#-------------------------------------------------------------------------------
from aiy.pins import PIN_A, PIN_B
from gpiozero import Servo

class Robot():
    
    def __init__(self, pin_right=PIN_A, pin_left=PIN_B, zero_left=-0.05, zero_right=-0.05):
        self.motor_right = Servo(pin_right)
        self.motor_left  = Servo(pin_left)
        
        # Offsets so Servo is off at this value (should be zero)
        self.zero_left   = zero_left
        self.zero_right  = zero_right
        self.stop()
        
    def forward(self, speed=0.5):
        self.motor_left.value = -speed
        self.motor_right.value = speed

    def backward(self, speed=0.5):
        self.motor_left.value = speed
        self.motor_right.value = -speed

    def right(self, speed=0.5):
        self.motor_left.value = speed
        self.motor_right.value = speed

    def left(self, speed=0.5):
        self.motor_left.value = -speed
        self.motor_right.value = -speed

    def stop(self):
        self.motor_left.value = self.zero_left
        self.motor_right.value = self.zero_right
        
    def close(self):
        self.stop()
        self.motor_right.close()
        self.motor_left.close()