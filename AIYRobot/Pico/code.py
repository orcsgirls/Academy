import usb_cdc
import board
import digitalio

in_data = bytearray()
out_data = bytearray()

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

serial = usb_cdc.data
print ('Robot server started')

while True:
    # Check if we have a new command
    if(len(out_data)>0):
        command = out_data.decode('utf-8')
        out_data = bytearray()
        print('Got:',command)

        if command.lower() == "light":
            led.value = not led.value

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
