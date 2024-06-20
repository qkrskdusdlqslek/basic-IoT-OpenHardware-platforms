 import RPi.GPIO as GPIO
 import time

 red_led = 21
 blue_led = 5
 green_led = 26

 #GPIO를 BCM모드로 설정
 GPIO.setmode(GPIO.BCM)
 #GPIO핀 설정(입력/출력)
 GPIO.setup(red_led, GPIO.OUT)
 GPIO.setup(blue_led, GPIO.OUT)
 GPIO.setup(green_led, GPIO.OUT)

 try:
   while True:
     GPIO.output(red_led, False)
     GPIO.output(blue_led, True)
     GPIO.output(green_led, True)
     time.sleep(1)

     GPIO.output(red_led, True)
     GPIO.output(blue_led, False)
     GPIO.output(green_led, True)
     time.sleep(1)

     GPIO.output(red_led, True)
     GPIO.output(blue_led, True)
     GPIO.output(green_led, False)
     time.sleep(1)


     GPIO.output(red_led, True)
     GPIO.output(blue_led, True)
     GPIO.output(green_led, True)
     time.sleep(1)
 except KeyboardInterrupt:   #Ctrl + c
   GPIO.cleanup()
