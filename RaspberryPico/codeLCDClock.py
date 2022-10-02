import board
import busio
from rgb1602 import Screen
from adafruit_datetime import datetime
import time

i2c = busio.I2C(board.GP5, board.GP4)

screen = Screen(i2c)

screen.set_css_colour("pink")

while True:
    now = datetime.now()
    current_time = now.time()
    screen.update("ORCSGirls rocks!", str(current_time))
    print(current_time)
    time.sleep(1.0)



