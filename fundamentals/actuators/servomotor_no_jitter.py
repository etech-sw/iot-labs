import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 11 for PWM signal
pwm_gpio = 11
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

#Init at 0°
pwm.start(0)
print("Waiting for 2 seconds")
time.sleep(2)

# Duty cycle
duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
      pwm.ChangeDutyCycle(duty)
      time.sleep(0.3)
      pwm.ChangeDutyCycle(0)
      time.sleep(0.7)
      duty = duty + 1

# Wait for 2 seconds
time.sleep(2)

#Go at 90°
#pwm.ChangeDutyCycle(setAngle(90))
#time.sleep(2)
print("Turning back to 90 degrees for 2 seconds")
pwm.ChangeDutyCycle(7)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)
time.sleep(1.5)


# Turn back to 0 degree
print("Turning back to 0 degrees")
pwm.ChangeDutyCycle(2)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)


#Finish at 180°
#pwm.ChangeDutyCycle(setAngle(180))
#time.sleep(1)

#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()
print(" Quit")
