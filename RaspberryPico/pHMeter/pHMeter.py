import time
import board
import digitalio
import analogio
import busio
from rgb1602 import Screen

#---------------------------------------------------------------------------
# These are the calibration values measured with the buffer solutions
#---------------------------------------------------------------------------
rawPH7 = 1.563
rawPH4 = 2.092


# Calculate slope and intercept

slope = (4.0 - 7.0) / (rawPH4 - rawPH7)
intercept = 7.0 - slope * rawPH7
print ('Calibration: pH = {0:.3f} + {1:0.3f} * voltage'.format(intercept, slope))

#---------------------------------------------------------------------------

# Button objects
red = digitalio.DigitalInOut(board.GP14)
red.switch_to_input(pull=digitalio.Pull.DOWN)
green = digitalio.DigitalInOut(board.GP15)
green.switch_to_input(pull=digitalio.Pull.DOWN)

# pH analog input
raw = analogio.AnalogIn(board.GP28)

# LCD display
i2c = busio.I2C(board.GP17, board.GP16)
screen = Screen(i2c)
screen.update('ORCSGirls - pH')

# Menu stuff
color=1
colorChoices=['blue','yellow','green','red','purple','white']
screen.set_css_colour(colorChoices[color])

menu=0
menuChoices=['Measure pH?  ','Measure raw?   ','Change color?']
screen.write_at_position(menuChoices[menu], col=0, row=1)

#---------------------------------------------------------------------------
# Helper routines
#---------------------------------------------------------------------------
def buttonReleased(b):
    while b.value:
        time.sleep(0.02)

#---------------------------------------------------------------------------
# Measure pH
#---------------------------------------------------------------------------
def measurePH(convert,slope,intercept):
    while True:
        if (convert):
            voltage = raw.value * 3.3 / 65535
            phValue = slope * voltage + intercept
            screen.write_at_position('pH : {0:0.2f}        '.format(phValue), col=0, row=1)
        else:
            rawVoltage = raw.value * 3.3 / 65535
            screen.write_at_position('Raw. : {0:0.3f}V     '.format(rawVoltage), col=0, row=1)

        for i in range(10):
            time.sleep(0.05)
            if(red.value):
                buttonReleased(red)
                return

#---------------------------------------------------------------------------
# LCD color
#---------------------------------------------------------------------------
def backgroundColor(colorChoices, color):
    screen.set_css_colour(colorChoices[color])
    while True:
        if(red.value):
            buttonReleased(red)
            if(color<len(colorChoices)-1):
                color = color + 1
            else:
                color = 0
            screen.set_css_colour(colorChoices[color])
            screen.write_at_position(colorChoices[color]+'             ', col=0, row=1)
        time.sleep(0.02)

        if(green.value):
            buttonReleased(green)
            return color

#---------------------------------------------------------------------------
# Main Loop
#---------------------------------------------------------------------------
while True:
    # Red button - cycle through menu
    if(red.value):
        buttonReleased(red)
        if(menu<len(menuChoices)-1):
            menu = menu + 1
        else:
            menu = 0
        screen.write_at_position(menuChoices[menu], col=0, row=1)

    # Green button - select current item
    if(green.value):
        buttonReleased(green)
        if (menu == 0):
            measurePH(True,slope,intercept)
            screen.write_at_position(menuChoices[menu], col=0, row=1)
        elif (menu == 1):
            measurePH(False,slope,intercept);
            screen.write_at_position(menuChoices[menu], col=0, row=1)
        elif (menu == 2):
            color = backgroundColor(colorChoices, color);
            screen.write_at_position(menuChoices[menu], col=0, row=1)

    time.sleep(0.02)

