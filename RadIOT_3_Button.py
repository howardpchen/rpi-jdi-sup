#!/usr/bin/python
# Author: Nathan Cross MD MS
# Copyright (c) 2017 Nathan Cross

# Acknowledgements
# Some of the libraries used are from Adafruit Industries who holds the
# copyright.  Please see individual files for details.

# Notes
# This file is to test the raspberry pi with an Adafruit 128px x 64px OLED
# display.

# Libraries
import time
from time import strftime
from gpiozero import Button, LED


# Setup Pins
# listing of device pins and which pin on the Pi they are connected to
button1_pin = 17
button2_pin = 12
led1_pin = 27
led2_pin = 22
button1 = Button(button1_pin)
button2 = Button(button2_pin)
led1 = LED(led1_pin)
led2 = LED(led2_pin)

# Initialize pins off
led1.off()
led2.off()

# When pin is pressed the associated LED will light up for half a second and then
# turn off.
print("Press Button When Ready:")

# Enter infinite loop which will poll buttons for state change and when pressed
# will light the associated led for half a second before turning off.
while True:
    if button1.is_pressed:
        print("Button 1 Pressed")
        led1.on()
    else:
        led1.off()

    if button2.is_pressed:
        print("Button 2 Pressed")
        led2.on()
    else:
        led2.off()

    time.sleep(.5)
