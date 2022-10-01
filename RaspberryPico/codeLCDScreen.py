import board
import busio
from rgb1602 import Screen

i2c = busio.I2C(board.GP5, board.GP4)

screen = Screen(i2c)
screen.update("ORCSGirls rocks!")

