 import RPi.GPIO as GPIO
 import time

 piezoPin = 13
 melody = [262, 294, 330, 349, 392, 440, 494, 524]

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(piezoPin, GPIO.OUT)

 Buzz = GPIO.PWM(piezoPin, 440)

 try:
   while True:
     Buzz.start(30)
     user_input = input('숫자입력')
     if user_input == '1':
       Buzz.ChangeFrequency(melody[0])
     elif user_input == '2':
       Buzz.ChangeFrequency(melody[1])
     elif user_input == '3':
       Buzz.ChangeFrequency(melody[2])
     elif user_input == '4':
       Buzz.ChangeFrequency(melody[3])
     elif user_input == '5':
       Buzz.ChangeFrequency(melody[4])
     elif user_input == '6':
       Buzz.ChangeFrequency(melody[5])
     elif user_input == '7':
       Buzz.ChangeFrequency(melody[6])
     elif user_input == '8':
       Buzz.ChangeFrequency(melody[7])

 except KeyboardInterrupt:
   GPIO.cleanup()
