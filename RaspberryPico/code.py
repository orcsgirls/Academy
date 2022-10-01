import board
import pwmio
import time

led = pwmio.PWMOut(board.GP1, frequency=1000)
led.duty_cycle = 65535

brightness = [0.5,1.0,0.5,0.0]
current_brightness = 0.0

while True:
    for b in brightness:
        start = int(current_brightness * 65536)
        end = int(b * 65536)
        if (start > end):
            step = -1
        else:
            step = 1

        for i in range(start,end,step):
            led.duty_cycle = i
            time.sleep(0.0001)

        current_brightness = b * 65536

