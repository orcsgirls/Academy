import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

class MyDS18X20(DS18X20):

    def __init__(self, pin):
        ow_bus = OneWireBus(pin)
        super().__init__(ow_bus, ow_bus.scan()[0])
        self.unit='C'
        self.min=9999.  # Hope the first reading is smaller than 9999 :)
        self.max=-9999. # Hope the first reading is larger than -9999 :)
        print("Init done :)")

    def reset(self):
        self.max=-9999.
        self.min=9999.

    @property
    def temperature(self):
        c = super().temperature
        if (self.unit=='C'):
            self.max=max(self.max,c) # Make self.max the larger value
            self.min=min(self.min,c) # Make self.max the larger value
            return c
        elif (self.unit=='F'):
            f = c * 1.8 + 32.0
            self.max=max(self.max,f) # Make self.max the larger value
            self.min=min(self.min,f) # Make self.max the larger value
            return f
        else:
            return 'Invalid unit'

sensor=MyDS18X20(board.GP16)
sensor.unit='F'   # Setting if to F

# Getting 20 values
for i in range(20):
    print(f"Temperature: {sensor.temperature:0.3f}{sensor.unit}")
    time.sleep(1.0)

# Printing max and min values measured
print(f"Maximum: {sensor.max:.3f}{sensor.unit}, Minimum: {sensor.min:.3f}{sensor.unit}")
