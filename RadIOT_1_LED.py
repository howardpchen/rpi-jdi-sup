#!/usr/bin/python
# Author: Nathan Cross MD MS
# Copyright (c) 2017 Nathan Cross


# Acknowledgements
# Some of the libraries used are from Adafruit Industries who holds the
# copyright.  Please see individual files for details.

# ----------------------------
# LED Tutorial
# ----------------------------

# Notes
# This is a basic demonstration of manipulating an LED using the gpiozero
# library.
#

# Libraries
import time
from time import strftime
from gpiozero import LED

# Setup Pins
# This is a listing of the pins which each device is connected to.
# For a list of the pins on the raspberry pi, see https://pinout.xyz/
led1_pin = 27
led2_pin = 22
led1 = LED(led1_pin)
led2 = LED(led2_pin)

# variable to control light sequence
sequence = 0

# initialization state - start with LED's off
led1.off()
led2.off()

print("LEDs should start lighting up in sequence shortly. Open file in text
        editor to review code")

while True:
    if sequence == 0:
        led1.off()
        led2.off()
        sequence += 1
    elif sequence == 1:
        led1.on()
        led2.off()
        sequence += 1
    elif sequence == 2:
        led1.off()
        led2.on()
        sequence += 1
    elif sequence == 3:
        led1.on()
        led2.on()
        sequence += 1
    else:
        sequence = 0

    # After each change in state, leave LED in that state for a short period of time.
    time.sleep(2)
