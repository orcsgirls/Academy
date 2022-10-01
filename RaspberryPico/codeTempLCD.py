import board
import busio
from rgb1602 import Screen
import adafruit_pct2075
import time

i2c = busio.I2C(board.GP5, board.GP4)
pct = adafruit_pct2075.PCT2075(i2c, address=0x48)

print(pct.temperature)

screen = Screen(i2c)
screen.set_css_colour("blue")

while True:
    out=f"T={pct.temperature}C"
    screen.update("ORCSGirls",out)
    time.sleep(2.0)

