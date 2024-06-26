 import RPi.GPIO as GPIO
 import time

 # Define GPIO pins for segments
 segments = [21, 22, 23, 24, 25, 26, 27]
 Button = 6

 # Set GPIO mode and setup pins
 GPIO.setmode(GPIO.BCM)
 for segment in segments:
   GPIO.setup(segment, GPIO.OUT)
   GPIO.setup(Button, GPIO.IN)
   GPIO.output(segment, 1)
 # Define patterns for digits 0-9 on a 7-segment display
 # Each tuple represents the segments (a to g) that should be on to display the digit
 digit_patterns = [
     [False, False, False, False, False, False, True],
     [True, False, False, True, True, True, True],
     [False, False, True, False, False, True, False],
     [False, False, False, False, True, True, False],
     [True, False, False, True, True, False, False],
     [False, True, False, False, True, False, False],
     [False, True, False, False, False, False, False],
     [False, False, False, True, True, True, True],
     [False, False, False, False, False, False, False],
     [False, False, False, False, True, False, False]
 ]

 count = 0
 try:
   while True:
     if GPIO.input(Button) == True:
       GPIO.output(segments[0], digit_patterns[count][0])
       GPIO.output(segments[1], digit_patterns[count][1])
       GPIO.output(segments[2], digit_patterns[count][2])
       GPIO.output(segments[3], digit_patterns[count][3])
       GPIO.output(segments[4], digit_patterns[count][4])
       GPIO.output(segments[5], digit_patterns[count][5])
       GPIO.output(segments[6], digit_patterns[count][6])
       time.sleep(1)
       count +=1
     if count == 10:
       count = 0

 except KeyboardInterrupt:
     GPIO.cleanup()

