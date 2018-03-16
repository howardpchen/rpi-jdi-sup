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
from time import sleep, gmtime, localtime, strftime
from gpiozero import Button, LED
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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
reed = Button(reed_pin, pull_up=True, bounce_time=1.5)

# OLED Pin Configuration for Raspberry Pi
RST = None      # not using oled rst pin
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display using hardware SPI interface:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Instantiate and initialize object
disp.begin()

# Wipe display buffer and output to screen
disp.clear()
disp.display()

# Obtain display width and height
width = disp.width
height = disp.height

# Load font.
font = ImageFont.load_default()

# Defaults
padding = -1
top = padding
bottom = height-padding

# Starting X-location on screen
x = 0

# Create black and white image canvas object
image = Image.new('1', (width,height))
# Instantiate drawing object on image canvas
draw = ImageDraw.Draw(image)

# Draw black background image
draw.rectangle((0,0,width,height), outline=0, fill=0)

def clearOutput():
    led1.off()
    led2.off()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    disp.clear()
    disp.display()
    return True


clearOutput()
print("Telephone Logger v1")
draw.text((x, top), str("Telephone Logger"), font=font, fill=255)
draw.text((x, top+16), str("  Loading..."), font=font, fill=255)
disp.image(image)
disp.display()

sleep(2)

clearOutput()
draw.text((x, top+24), str("        ..."), font=font, fill=255)
disp.image(image)
disp.display()

def ask_question():
    # Reed Switch activated load question onto screen and light LEDs to attact user
    led1.on()
    led2.on()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top), str("Press appropriate"), font=font, fill=255)
    draw.text((x, top+8), str(" response."), font=font, fill=255)
    draw.text((x, top+24), str("Question 1"), font=font, fill=255)
    disp.image(image)
    disp.display()
    while True:
        if button1.is_pressed:
            # Answer 1 was selected by pressing button 1, light corresponding LED, output
            # acknowledged response to the display and return to waiting state.
            print("Button 1 Pressed - " + strftime("  %a, %d %b %Y, %H:%M:%S", localtime()))
            led2.off()
            led1.on()
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+8), str(strftime("  %a, %d %b %Y", localtime())), font=font, fill=255)
            draw.text((x, top+16), str(strftime("      %H:%M:%S", localtime())), font=font, fill=255)
            draw.text((x, top+24), str("      Button 1"), font=font, fill=255)
            draw.text((x, top+32), str("      Pressed"), font=font, fill=255)
            disp.image(image)
            disp.display()
            sleep(3)

            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+24), str("Sleeping..."), font=font, fill=255)
            disp.image(image)
            disp.display()
            sleep(1)
            clearOutput()
            break
        if button2.is_pressed:
            # Answer 2 was selected by pressing button 2, light corresponding LED, output
            # acknowledged response to the display and return to waiting state.
            print("Button 2 Pressed - " + strftime("  %a, %d %b %Y, %H:%M:%S", localtime()))
            led1.off()
            led2.on()
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+8), str(strftime("  %a, %d %b %Y", localtime())), font=font, fill=255)
            draw.text((x, top+16), str(strftime("      %H:%M:%S", localtime())), font=font, fill=255)
            draw.text((x, top+24), str("      Button 2"), font=font, fill=255)
            draw.text((x, top+32), str("      Pressed"), font=font, fill=255)
            disp.image(image)
            disp.display()
            sleep(3)

            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+24), str("Sleeping..."), font=font, fill=255)
            disp.image(image)
            disp.display()
            sleep(1)
            clearOutput()
            break

    return True

while True:
    reed.when_pressed = ask_question

