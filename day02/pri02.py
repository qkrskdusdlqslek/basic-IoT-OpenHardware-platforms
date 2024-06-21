 import RPi.GPIO as GPIO
 import time

 pirPin = 24
 red_led = 21

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(pirPin, GPIO.IN)
 GPIO.setup(red_led, GPIO.OUT)

 try:
   while True:
     if GPIO.input(pirPin) == True:
       GPIO.output(red_led, False)
       print("Detected")

     elif GPIO.input(pirPin) == False:
       GPIO.output(red_led, True)
       time.sleep(0.5)

 except KeyboardInterrupt:
   GPIO.cleanup()
