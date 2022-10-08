import board
import digitalio

pir = digitalio.DigitalInOut(board.GP15)
pir.direction = digitalio.Direction.INPUT

alarmCount=0
while True:
    if pir.value:
        alarmCount+=1
        print(f"ALARM! Motion detected! - Count {alarmCount}")
        while pir.value:
            pass
