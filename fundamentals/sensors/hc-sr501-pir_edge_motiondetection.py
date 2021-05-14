import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_SENSOR_PIN = 16
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)


def motion(PIR_SENSOR_PIN):
	print("Mouvement détecté")


print("Lancement du capteur de presence IR (CTRL-C pour quitter)")
time.sleep(1)

try:
	GPIO.add_event_detect(PIR_SENSOR_PIN,GPIO.RISING,callback=motion)
	while True:
		time.sleep(100)

except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	# Reinitialisation des parametres GPIOs
	GPIO.cleanup()

