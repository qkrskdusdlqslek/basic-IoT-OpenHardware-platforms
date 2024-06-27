 import RPi.GPIO as GPIO
 import time

 # 0~9까지 1byte hex값
 fndDatas  = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xD>

 fndSegs = [21, 22, 23, 24, 25, 26, 27]
 fndSels = [16, 17, 18, 19]

 GPIO.setmode(GPIO.BCM)
 for fndSeg in fndSegs:
   GPIO.setup(fndSeg, GPIO.OUT)
   GPIO.output(fndSeg, 1)

 for fndSel in fndSels:
   GPIO.setup(fndSel, GPIO.OUT)
   GPIO.output(fndSel, 0)

 def findOut(data):       # 하나의 숫자 형태를 만드는 함수
   for i in range(0, 7):
 #   GPIO.output(fndSegs[0], 0)
 #   GPIO.output(fndSegs[1], 1)
 #   GPIO.output(fndSegs[2], 1)
 #   GPIO.output(fndSegs[3], 0)
     GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
 try:
   while True:
     for i in range(0, 1):
       GPIO.output(fndSels[i], 1)            # fnd 선택
 #     GPIO.output(22, 1)
 #     GPIO.output(23, 1)

       for j in range(0, 10):
         findOut(j)
         time.sleep(0.5)

 except KeyboardInterrupt:
   GPIO.cleanup()
