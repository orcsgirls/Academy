import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

#-------------------------------------------------------------------------
class liquidThermometer(DS18X20):

    def __init__(self, pin):
        self.pin = pin
        self.ow_bus = OneWireBus(self.pin)
        super().__init__(self.ow_bus, self.ow_bus.scan()[0])

    @property
    def celcius(self):
        return super().temperature

    @property
    def fahrenheit(self):
        return super().temperature * 1.8 +32.0

#-------------------------------------------------------------------------
# Liquids thermometer
try:
    thermometer = liquidThermometer(board.GP22)
    print ("Thermometer found.")
    tConnected = True
except:
    print ("Thermometer not found - disabling.")
    tConnected = False
    del(thermometer)

#-------------------------------------------------------------------------
while True and tConnected:
    print(f"Temperature: {thermometer.fahrenheit:.3f} F")
    time.sleep(1.0)
