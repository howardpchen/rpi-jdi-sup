#!/usr/bin/python
# Author: Nathan Cross MD MS
# Copyright (c) 2017 Nathan Cross

# Acknowledgements
# Some of the libraries used are from Adafruit Industries who holds the
# copyright.  Please see individual files for details.

# Notes

# Libraries
from time import strftime, sleep, localtime, time
from gpiozero import Button, LED

# Setup Pins
button1_pin = 17
button2_pin = 12
led1_pin = 27
led2_pin = 22
button1 = Button(button1_pin)
button2 = Button(button2_pin)
led1 = LED(led1_pin)
led2 = LED(led2_pin)
reed_pin = 5
reed = Button(reed_pin, pull_up=True, bounce_time=0.5)

# Initialize leds to off state
led1.off()
led2.off()

print("Place magnet near reed switch")

# Enter infinite loop where reed switch is being constantly polled to see if its
# contacts get closed.  When contacts of reed switch are closed by a nearby magnet
# the LEDs turn on and a message is printed.
while True:
    if reed.is_pressed:
        print("Reed Switch Activated -" + strftime(" %a, %d %b %Y, %H:%M:%S", localtime()))
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()

    time.sleep(.1)
