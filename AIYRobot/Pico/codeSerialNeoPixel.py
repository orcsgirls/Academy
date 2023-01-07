import usb_cdc
import board
import digitalio
from rainbowio import colorwheel
import neopixel

in_data = bytearray()
out_data = bytearray()

num_pixels=8
pixels = neopixel.NeoPixel(board.GP21, num_pixels, auto_write=True)
pixels.brightness = 0.4
pixels.fill((0,0,0))

serial = usb_cdc.data
print ('Robot server started')

while True:
    # Check if we have a new command
    if(len(out_data)>0):
        command = out_data.decode('utf-8')
        out_data = bytearray()

        if "neo" in command:
            got=command.split()
            color=(float(got[1]),float(got[2]),float(got[3]))
            pixels.fill(color)

    # This part checks the serial connection for data
    # One there is a carriage return, it writes it to out_data.
    if serial.in_waiting > 0:
        byte = serial.read(1)
        if byte == b'\r':
            out_data = in_data
            in_data = bytearray()
        else:
            in_data += byte
            if len(in_data) == 129:
                in_data = in_data[128] + in_data[0:127]
