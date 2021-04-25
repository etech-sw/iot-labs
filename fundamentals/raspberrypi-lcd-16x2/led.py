import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

try:
	while True:
		try:
			print("LED green on")
			GPIO.output(5,GPIO.HIGH)
			time.sleep(1)

			print("LED green off")
			GPIO.output(5,GPIO.LOW)
		
			print("LED red on")
			GPIO.output(6,GPIO.HIGH)
			time.sleep(1)

			print("LED red off")
			GPIO.output(6,GPIO.LOW)

			print("LED green on")
			GPIO.output(12,GPIO.HIGH)
			time.sleep(1)
			print("LED green off")
			GPIO.output(12,GPIO.LOW)
		except RuntimeError as error:
			print(error.args[0])
			time.sleep(2.0)
			continue
except KeyboardInterrupt:
	print("Cleaning up!")
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
