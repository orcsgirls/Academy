import board
import analogio
import time

# pH analog input 
raw = analogio.AnalogIn(board.GP28)

# Main code loop
while True:
    raw_voltage = raw.value * 3.3 / 65535
    
    print('Raw. : {0:0.3f}V'.format(raw_voltage))
    time.sleep(1.0)
