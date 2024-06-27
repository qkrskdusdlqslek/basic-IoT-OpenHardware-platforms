 import RPi.GPIO as GPIO
 import time

 # 0~9까지 1byte hex값
 fndDatas  = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xD8, 0x80, 0x90]

 fndSegs = [21, 22, 23, 24, 25, 26, 27]
 fndSels = [19, 18, 17, 16]
 count = 0

 #GPIO 설정
 GPIO.setmode(GPIO.BCM)
 for fndSeg in fndSegs:
   GPIO.setup(fndSeg, GPIO.OUT)
   GPIO.output(fndSeg, 1)

 for fndSel in fndSels:
   GPIO.setup(fndSel, GPIO.OUT)
   GPIO.output(fndSel, 0)

 def findOut(data, sel):       # 하나의 숫자 형태를 만드는 함수
   for h in range(0, 50):
     for i in range(0, 7):
       GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
       for j in range(0, 4):         # 표시할  자리수의 fnd만 on
         if j == sel:
           GPIO.output(fndSels[j], 1)
         else:
           GPIO.output(fndSels[j], 0)

 try:
   while True:
     count += 1
     d1000 = count / 1000
     d100 = count % 1000 / 100
     d10 = count % 100 / 10
     d1 = count % 10
     d= [d1, d10, d100, d1000]

     for i in range(3, -1, -1):
         findOut(int(d[i]), i)                    # 자리수와 값을 전달
         time.sleep(0.003)
     if count == 9999:
       count = 0

 except KeyboardInterrupt:
   GPIO.cleanup()
