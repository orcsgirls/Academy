import time
import board
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20

# This uses a socalled one-wire protocol
ow_bus = OneWireBus(board.GP16)
devices = ow_bus.scan()

# List all devices - we are looking for Family 0x28. If it is
# not the first one, we need to chance devices[0] to the right one.

for device in devices:
    print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))

# Now we create the temperature object
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])

while True:
    print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))
    time.sleep(1.0)
