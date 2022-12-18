import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# This uses a socalled one-wire protocol
ow_bus = OneWireBus(board.GP16)
sensor = DS18X20(ow_bus, ow_bus.scan()[0])

while True:
    print(f"Temperature: {sensor.temperature:0.3f} °C")
    time.sleep(1.0)
