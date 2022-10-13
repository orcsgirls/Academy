import board
import busio
import adafruit_pct2075
import time

i2c = busio.I2C(board.GP5, board.GP4)
pct = adafruit_pct2075.PCT2075(i2c, address=0x48)

while True:
    print(f"T={pct.temperature}C")
    time.sleep(1.0)

