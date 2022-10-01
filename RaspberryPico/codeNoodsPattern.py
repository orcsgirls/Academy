import board
import pwmio
import time

led = pwmio.PWMOut(board.GP1, frequency=1000)
led.duty_cycle = 65535

pattern = [0.3,0.3,0.3,0.1,0.1,0.1]

while True:
    for p in pattern:
        led.duty_cycle=65535
        time.sleep(p)
        led.duty_cycle=0
        time.sleep(p)
