# Source: https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/io.html#ticklish-python

from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)