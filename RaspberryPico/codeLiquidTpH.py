import board
import busio
import analogio
import adafruit_ds18x20
import time
from rgb1602 import Screen
from adafruit_onewire.bus import OneWireBus

# Liquids thermometer
ow_bus = OneWireBus(board.GP16)
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, ow_bus.scan()[0])

# LCD display
i2c = busio.I2C(board.GP5, board.GP4)
screen = Screen(i2c)
screen.set_css_colour("blue")

# pH analog input 
raw = analogio.AnalogIn(board.GP28)

# Main code loop
while True:
    try:
        raw_voltage = raw.value * 3.3 / 65535
        screen.update('Temp.: {0:0.3f}C'.format(ds18b20.temperature),'Raw. : {0:0.3f}V'.format(raw_voltage))
        time.sleep(1.0)
    except CRC Error:
        print "Temperature sensor communication error - hold on .."
        pass