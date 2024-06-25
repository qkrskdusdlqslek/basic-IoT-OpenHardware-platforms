 from picamera2 import Picamera2
 import RPi.GPIO as GPIO
 import time
 import datetime

 swPin = 6

 oldSw = 0
 newSw = 0

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(swPin, GPIO.IN)

 picam2 = Picamera2()
 camera_config = picam2.create_preview_configuration()
 picam2.configure(camera_config)
 picam2.start()

 try:
   while True:
       newSw = GPIO.input(swPin)
         if newSw != oldSw:
           oldSw = newSw

       if newSw == True:
         now = datetime.datetime.now()
         print("click")
         fileName = now.strftime( '%y-%m-%d %H:%M:%f')
         picam2.capture_file(fileName + '.jpg')

       time.sleep(0.2)

 except KeyboardInterrupt:
   pass
