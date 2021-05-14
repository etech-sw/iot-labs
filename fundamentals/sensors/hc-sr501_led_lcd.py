import sys
import RPi.GPIO as GPIO
import time

sys.path.append("/home/pi/Documents/etech-sw/iot-labs/fundamentals/raspberrypi-lcd-16x2")

import drivers

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIR_SENSOR_PIN = 16
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)
GPIO.setup(5, GPIO.OUT)


LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

display = drivers.GpioLcd()

def motion(PIR_SENSOR_PIN):
        if GPIO.input(PIR_SENSOR_PIN):
                GPIO.output(5,GPIO.HIGH)
                display.lcd_display_string("Mouvement",LCD_LINE_1)
                display.lcd_display_string("       detecte",LCD_LINE_2)
                print("Mouvement detecte")
        else:
                GPIO.output(5,GPIO.LOW)
                display.lcd_display_string("Pas de mouvement",LCD_LINE_1)

print("Lancement du capteur de presence IR (CTRL-C pour quitter)")
time.sleep(1)

try:
        GPIO.add_event_detect(PIR_SENSOR_PIN,GPIO.BOTH,callback=motion)
        while True:
                time.sleep(100)

except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        # Reinitialisation des parametres GPIOs
        GPIO.cleanup()


