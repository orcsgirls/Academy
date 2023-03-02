import time

class Joint:
    # init method or constructor
    def __init__(self, id, name, servo, home_position=90, max_value=180, min_value=0, speed=30):
         
        self.id = id
        self.name = name
        self.servo = servo
        self.max_value = max_value
        self.min_value = min_value
        self.speed = speed
        self.home_position = home_position
        
        # Homing
        self.servo.angle = self.home_position

    # Output on print
    def __str__(self):
        return f"{self.name} at position {self.servo.angle:.1f}"
       
    # Check angle is valid
    def _angleValid(self, angle):
        return angle <= self.max_value and angle >= self.min_value
    
    # Move to angle at speed
    def move(self, angle):   
        if(self._angleValid(angle)):        
            start  = self.servo.angle    
            points = abs(round(angle-start))
            if (points>0):
                delta  = (angle-start)/points
                for p in range(points):
                    start=start+delta
                    self.servo.angle = start
                    time.sleep(1.0/self.speed)

            self.servo.angle = angle
        
    # Go to angle direct
    def goto(self, angle):
        if(self._angleValid(angle)):
            self.servo.angle = angle

    # Increment angle
    def jog(self, increment):
        self.goto(self.servo.angle + increment)

    # Go home
    def home(self):
        self.move(self.home_position)

