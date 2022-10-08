import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin GP17.
pwm = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# Move to 0, 90 and 180 degrees
for angle in [0,90,180]:
    my_servo.angle = angle
    time.sleep(1.0)

