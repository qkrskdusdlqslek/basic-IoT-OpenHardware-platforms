 #interrupt

 import RPi.GPIO as GPIO
 import time

 #핀 설정
 red_led = 21
 switch = 6

 #인터럽트 변수
 intFlag = False

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(red_led, GPIO.OUT)
 GPIO.setup(switch, GPIO.IN)

 def ledBlink(channel):
   global intFlag
   if intFlag == False:
     GPIO.output(red_led, True)
     intFlag = True
   else:
     GPIO.output(led, False)
     intFlag = False

 #인터럽트 설정(switch핀에 rising 신호가 잡히면, callback함수를 실행)
 GPIO.add_event_detect(switch, GPIO.RISING, callback=ledBlink)

 try:
   while True:
     pass
 except KeyboardInterrupt:
   GPIO.cleanup()
