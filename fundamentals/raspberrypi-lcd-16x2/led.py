import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

try:
	while True:
		try:
			print("LED green on")
			GPIO.output(23,GPIO.HIGH)
			time.sleep(1)

			print("LED green off")
			GPIO.output(23,GPIO.LOW)
		
			print("LED red on")
			GPIO.output(24,GPIO.HIGH)
			time.sleep(1)

			print("LED red off")
			GPIO.output(24,GPIO.LOW)

			print("LED green on")
			GPIO.output(25,GPIO.HIGH)
			time.sleep(1)
			print("LED green off")
			GPIO.output(25,GPIO.LOW)
		except RuntimeError as error:
			print(error.args[0])
			time.sleep(2.0)
			continue
except KeyboardInterrupt:
	print("Cleaning up!")
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
