import adafruit_dht
import time
import board
import RPi.GPIO as GPIO
import time
import drivers

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

MINUTES_BETWEEN_READS = 1
LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

display = drivers.GpioLcd()
dhtSensor = adafruit_dht.DHT11(board.D4)

try:
	while True:
		try:
			humidity = dhtSensor.humidity
			temp_c = dhtSensor.temperature
			temp_f = temp_c * (9 / 5) + 32
			print(
            			"Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                		temp_f, temp_c, humidity
            			)
        		)
			GPIO.output(5,GPIO.HIGH)
			display.lcd_display_string("Temp:{:.1f}F/{:.1f}C".format(temp_f, temp_c), LCD_LINE_1)
			display.lcd_display_string("Humidity: {}%".format(humidity), LCD_LINE_2)
			
			time.sleep(2.0)
			GPIO.output(5,GPIO.LOW)
		except RuntimeError as error:
			print(error.args[0])
			GPIO.output(6,GPIO.HIGH)
			
			#display.lcd_clear()

			time.sleep(2.0)
			GPIO.output(6,GPIO.LOW)
			#time.sleep(2.0)
			continue
		except Exception as error:
			dhtSensor.exit()
			raise error
		#time.sleep(2.0)

except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	dhtSensor.exit()
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
finally:
	GPIO.cleanup()
