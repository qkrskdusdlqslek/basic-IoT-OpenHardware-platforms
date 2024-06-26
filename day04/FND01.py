 import RPi.GPIO as GPIO
 import time

 # Define GPIO pins for segments
 segments = [21, 22, 23, 24, 25, 26, 27]

 # Set GPIO mode and setup pins
 GPIO.setmode(GPIO.BCM)
 for segment in segments:
     GPIO.setup(segment, GPIO.OUT)

 # Define patterns for digits 0-9 on a 7-segment display
 # Each tuple represents the segments (a to g) that should be on to display the digit
 digit_patterns = {
     0: (False, False, False, False, False, False, True),
     1: (True, False, False, True, True, True, True),
     2: (False, False, True, False, False, True, False),
     3: (False, False, False, False, True, True, False),
     4: (True, False, False, True, True, False, False),
     5: (False, True, False, False, True, False, False),
     6: (False, True, False, False, False, False, False),
     7: (False, False, False, True, True, True, True),
     8: (False, False, False, False, False, False, False),
     9: (False, False, False, False, True, False, False)
 }

 try:
     while True:
         # Display digits 0-9 repeatedly
         for digit in range(10):
             pattern = digit_patterns[digit]
             for pin, state in zip(segments, pattern):
                 GPIO.output(pin, state)
             time.sleep(1)

 except KeyboardInterrupt:
     GPIO.cleanup()
