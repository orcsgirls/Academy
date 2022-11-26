import board
import busio
import time
import adafruit_am2320

i2c = busio.I2C(board.GP17, board.GP16)
sensor = adafruit_am2320.AM2320(i2c)

while True:
    print(f"Humidity: {sensor.relative_humidity:.1f}%")
    time.sleep(0.1) # This is needed between sensor readings!
    print(f"Temperature: {sensor.temperature:.2f}C")
    time.sleep(1.0)
