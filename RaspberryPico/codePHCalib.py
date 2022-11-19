import board
import analogio
import busio
import time
from rgb1602 import Screen

#LCD screen definitions
i2c = busio.I2C(board.GP17, board.GP16)
screen = Screen(i2c)
screen.set_css_colour("green")

#calibration
ph7_voltage = 1.567
ph4_voltage = 2.043

#calculate slope and intercept
slope = (4 - 7) / (ph4_voltage - ph7_voltage)
intercept = 7 - slope * ph7_voltage
print(f"Slope: {slope} with intercept: {intercept}")

# pH analog input
raw = analogio.AnalogIn(board.GP27)

# Main code loop
while True:
    raw_voltage = raw.value * 3.3 / 65535
    ph = raw_voltage * slope + intercept
    print(f"Raw. : {raw_voltage:.3f}V, pH: {ph:.2f}")
    screen.update(f"Raw: {raw_voltage:.3f} V",f"pH:  {ph:.2f}")

    time.sleep(1.0)
