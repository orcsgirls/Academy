import board
import pwmio
import time

led = pwmio.PWMOut(board.GP1, frequency = 1000)

while True:
    for i in range(0, 65535):
        led.duty_cycle = i
        time.sleep(0.001)
    print("Max brightness")

    for j in range(65535, 0, -1):
        led.duty_cycle = j
        time.sleep(0.001)
    print("Off")

