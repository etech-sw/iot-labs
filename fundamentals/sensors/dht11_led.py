import adafruit_dht
import time
import board
import RPi.GPIO as GPIO
import time


LED_GREEN_PIN  = 5
LED_RED_PIN    = 6
LED_YELLOW_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_GREEN_PIN,GPIO.OUT)
GPIO.setup(LED_RED_PIN,GPIO.OUT)
GPIO.setup(LED_YELLOW_PIN,GPIO.OUT)

MINUTES_BETWEEN_READS = 1

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
			GPIO.output(LED_GREEN_PIN,GPIO.HIGH)
			time.sleep(1.0)
			GPIO.output(LED_GREEN_PIN,GPIO.LOW)
		except RuntimeError as error:
                        # Errors happen quite often for the DHT's sensors, keep on running
                        print(error.args[0])
                        GPIO.output(LED_RED_PIN,GPIO.HIGH)
                        time.sleep(1.0)
                        GPIO.output(LED_RED_PIN,GPIO.LOW)
                        continue
		except Exception as error:
			dhtSensor.exit()
			raise error
except KeyboardInterrupt:
	# When there is a keyboardInterrupt (ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	dhtSensor.exit()
	GPIO.output(LED_GREEN_PIN, GPIO.LOW)
	GPIO.output(LED_RED_PIN, GPIO.LOW)
