#! /usr/bin/env python

# Sample Demo program for the I2C LCD 16x2 Display
# Created by Etech-SW

# Libraries for communication and display
import drivers
from time import sleep

# Load the LCD driver and set it to "display"
display = drivers.Lcd()

# Main
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Start writing to display")
        display.lcd_display_string("IoT@RaspberryPI", 1)       # Write text to first display line
        display.lcd_display_string("Ecran LCD 16x2", 2)        # Write text to second display line
        sleep(2)                                               # Wait for 2 seconds
        display.lcd_clear()
        display.lcd_display_string("Greetings from", 1)   # Update first line of display
        display.lcd_display_string("       Etech-SW", 2)
        sleep(2)                                           # Wait for 2 seconds for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(2)                                           # Wait for 2 seconds for the message to be read
except KeyboardInterrupt:
    # when ctrl+c press, exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
