import adafruit_dht
import time
import board
import RPi.GPIO as GPIO
import time
import drivers

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

MINUTES_BETWEEN_READS = 1

display = drivers.Lcd()
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
			GPIO.output(23,GPIO.HIGH)
			display.lcd_display_string("Temp:{:.1f}F/{:.1f}C".format(temp_f, temp_c), 1)
			#display.lcd_display_string("Temperature: %d F" % temp_f, 2)
			display.lcd_display_string("Humidity: {}%".format(humidity), 2)
			
			time.sleep(2.0)
			GPIO.output(23,GPIO.LOW)
		except RuntimeError as error:
			print(error.args[0])
			GPIO.output(24,GPIO.HIGH)
			
			display.lcd_clear()

			time.sleep(2.0)
			GPIO.output(24,GPIO.LOW)
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
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)

	display.lcd_clear()
