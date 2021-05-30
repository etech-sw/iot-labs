#! /usr/bin/env python

# Sample Demo program to interface with the DHT11
# Created by Etech-SW

import adafruit_dht
import board
import time

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
			time.sleep(2.0)
		except RuntimeError as error:
			print(error.args[0])
			time.sleep(2.0)
			continue
		except Exception as error:
			dhtSensor.exit()
			raise error

except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	dhtSensor.exit()

