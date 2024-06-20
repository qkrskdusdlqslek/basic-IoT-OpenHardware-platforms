 import RPi.GPIO as GPIO
 import time

 red_led = 21
 blue_led = 5
 green_led = 26

 switch = 6

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(switch, GPIO.IN)
 GPIO.setup(red_led, GPIO.OUT)
 GPIO.setup(blue_led, GPIO.OUT)
 GPIO.setup(green_led, GPIO.OUT)

 try:
   while True:
     if GPIO.input(switch) == True:
       GPIO.output(red_led, False)
       GPIO.output(blue_led, True)
       GPIO.output(green_led, True)
       time.sleep(1)

     if GPIO.input(switch) == True:
       GPIO.output(red_led, True)
       GPIO.output(blue_led, False)
       GPIO.output(green_led, True)
       time.sleep(1)

     if GPIO.input(switch) == True:
       GPIO.output(red_led, True)
       GPIO.output(blue_led, True)
       GPIO.output(green_led, False)
       time.sleep(1)

 except KeyboardInterrupt:
   GPIO.cleanup()
