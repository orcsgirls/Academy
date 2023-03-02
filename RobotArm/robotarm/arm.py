import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import itertools
from robotarm import Joint

class Arm():  
    # init method or constructor
    def __init__(self, config):    
        i2c = busio.I2C(board.SCL, board.SDA)
        pca = adafruit_pca9685.PCA9685(i2c)
        self.kit = ServoKit(channels=16)
        
        self.joints=[]
        for c in config:
            self.joints.append(Joint(c['name'], c['channel'], self.kit.servo[c['channel']], 
                                     min_value = c['min_angle'], max_value = c['max_angle'], home_position = c['home_angle']))        
        self.locations = []

    def __str__(self):
        info = "Arm status"
        for joint in self.joints:
            info = info + "\n  " +str(joint)
        return info
    
    def home(self):
        for joint in self.joints:
            joint.home()
            
    def clear_locations(self):
        self.locations.clear()
        
    def save_location(self):
        self.locations.append([joint.servo.angle for joint in self.joints])
        
    def run_locations(self):
        for location in self.locations:
            for (angle, joint) in zip(location, self.joints):
                joint.move(angle)
        
    def stored_locations(self):
        return len(self.locations)
