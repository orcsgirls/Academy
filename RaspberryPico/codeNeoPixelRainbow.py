import time
import board
import analogio
from rainbowio import colorwheel
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 8

pixels = neopixel.NeoPixel(board.GP0, num_pixels, auto_write=False)
pixels.brightness = 0.2

potentiometer = analogio.AnalogIn(board.GP28)

def rainbow():
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        speed=potentiometer.value / 65535 / 255
        time.sleep(speed)


while True:
    rainbow()
