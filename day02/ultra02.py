 import RPi.GPIO as GPIO
 import time

 def measure():
   GPIO.output(trigPin, True)
   time.sleep(0.00001)
   GPIO.output(trigPin, False)
   start = time.time()

   while GPIO.input(echoPin) == False:
     start = time.time()
   while GPIO.input(echoPin) ==True:
     stop = time.time()
   elapsed = stop - start
   distance = (elapsed * 19000) / 2

   return distance

 piezoPin = 13
 melody = [440]
 trigPin = 17
 echoPin = 4

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(piezoPin, GPIO.OUT)
 GPIO.setup(trigPin, GPIO.OUT)
 GPIO.setup(echoPin, GPIO.IN)

 Buzz = GPIO.PWM(piezoPin, 440)

 try:
   while True:
     distance = measure()
     print("Distnace: %.2f cm" %distance)
     time.sleep(1)

     if distance <= 30 and distance > 20:
       Buzz.start(50)
       Buzz.ChangeFrequency(melody[0])
       time.sleep(0.6)
       Buzz.stop()

     elif distance <= 20 and distance > 10:
       Buzz.start(50)
       Buzz.ChangeFrequency(melody[0])
       time.sleep(0.3)
       Buzz.stop()

     elif distance <= 10 and distance > 1:
       Buzz.start(50)
       Buzz.ChangeFrequency(melody[0])
       time.sleep(0.1)
       Buzz.stop()

 except KeyboardInterrupt:
   GPIO.cleanup()
