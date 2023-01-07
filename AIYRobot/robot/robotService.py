#-------------------------------------------------------------------------------
# Simple robot class for our AIY robot
# (c) ORCSGirls Academy, 2022
#-------------------------------------------------------------------------------
from aiy.pins import PIN_A, PIN_B
from gpiozero import Servo
import threading
import queue
import signal
import time

#-------------------------------------------------------------------------------
class Service():

    def __init__(self):
        self._requests = queue.Queue()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self):
        while True:
            request = self._requests.get()
            if request is None:
                self.shutdown()
                break
            self.process(request)
            self._requests.task_done()

    def process(self, request):
        pass

    def shutdown(self):
        pass

    def submit(self, request):
        self._requests.put(request)

    def close(self):
        self._requests.put(None)
        self._thread.join()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

#-------------------------------------------------------------------------------
class RobotService(Service):
    
    def __init__(self, pin_right=PIN_A, pin_left=PIN_B, zero_left=-0.05, zero_right=-0.05):
        super().__init__()
        self._motor_right = Servo(pin_right)
        self._motor_left  = Servo(pin_left)
        
        # Offsets so Servo is off at this value (should be zero)
        self.zero_left   = zero_left
        self.zero_right  = zero_right
        self.stop()
        
    def process(self, request):
        (left, right, duration) = request
        self._motor_right.value = right
        self._motor_left.value = left
        if(duration > 0):
            time.sleep(duration)
            self.stop()
        
    def forward(self, speed=0.5, duration=0.0):
        self.submit((-speed, speed, duration))

    def backward(self, speed=0.5, duration=0.0):
        self.submit((speed, -speed, duration))

    def right(self, speed=0.5, duration=0.0):
        self.submit((speed, speed, duration))

    def left(self, speed=0.5, duration=0.0):
        self.submit((-speed, -speed, duration))

    def stop(self):
        self.submit((self.zero_left, self.zero_right, 0))
        
    def close(self):
        self.stop()
        self._motor_right.close()
        self._motor_left.close()