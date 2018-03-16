#!/usr/bin/python
# Author: Nathan Cross MD MS
# Copyright (c) 2017 Nathan Cross

# Acknowledgements
# Some of the libraries used are from Adafruit Industries who holds the
# copyright.  Please see individual files for details.

# Notes
# This file is to test the raspberry pi with an Adafruit 128px x 64px OLED
# display. This display uses SPI by default to communicate.

# Libraries
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Pin Configuration for Raspberry Pi
# Listing of device pins and what pins they connect to on the Pi
RST = 24      # not using oled rst pin
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

# Output Information
draw.text((x, top+16), str("Great Work!"), font=font, fill=255)
draw.text((x, top+24), str("Keep it up..."), font=font, fill=255)

# Display image.
disp.image(image)
disp.display()

print("Output default text to display.  To modify the output to the display, open
        this file in a text editor.")
