import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

#-------------------------------------------------------------------------
# This is out liquidThermometer class which inherits from the 
# DS18X20 class used for our liquids thermometer.
#-------------------------------------------------------------------------
class liquidThermometer(DS18X20):

    def __init__(self, pin, unit='c'):
        self.pin  = pin
        self.ow_bus = OneWireBus(self.pin)
        super().__init__(self.ow_bus, self.ow_bus.scan()[0])

        self.unit = unit        
        self.max = -9999
        self.min = 9999

    def _updateMaxMin(self, value):
        self.max = max(self.max,value)
        self.min = min(self.min,value)            
    
    def reset(self):
        self.max = -9999
        self.min = 9999
        
    @property
    def temperature(self):
        c = super().temperature
        if (self.unit=='C'):
            self._updateMaxMin(c)
            return c
        elif (self.unit=='F'):
            f = c * 1.8 + 32.0
            self._updateMaxMin(f)
            return f
        else:
            return 'Invalid unit'

#-------------------------------------------------------------------------
# Instantiating the class
#-------------------------------------------------------------------------

t = liquidThermometer(board.GP22, "F")
print (f"Thermometer connected. Unit is {t.unit}")

#-------------------------------------------------------------------------
# Measuring loop
#-------------------------------------------------------------------------

while True:
    print(f"Temperature: {t.temperature:.3f} {t.unit} - Max: {t.max:.3f} {t.unit}, Min: {t.min:.3f} {t.unit}")
    time.sleep(1.0)

