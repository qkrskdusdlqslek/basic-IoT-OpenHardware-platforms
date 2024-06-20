 import RPi.GPIO as GPIO
 import time

 red_led=21

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(red_led, GPIO.OUT)

 try:
   while True:
     user_input = input('o 또는  x 입력')
     if user_input == 'o':
       GPIO.output(red_led, False)
     elif user_input == 'x':
       GPIO.output(red_led, True)

 except KeyboardInterrupt:
   GPIO.cleanup()
