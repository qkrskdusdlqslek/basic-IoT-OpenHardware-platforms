 from PyQt5.QtWidgets import *
  2 from PyQt5 import uic
  3 import sys
  4 import RPi.GPIO as GPIO
  5 import time
  6 from PyQt5.QtCore import QTimer
  7
  8 # PIN 설정
  9 red_led = 13
 10 green_led = 12
 11 blue_led = 6
 12
 13 pirPin = 4
 14
 15 relayPin = 5
 16
 17 trigPin = 6
 18 echoPin = 5
 19
 20 fndDatas = [
 21   [False, False, False, False, False, False, True],
 22   [True, False, False, True, True, True, True],
 23   [False, False, True, False, False, True, False],
 24   [False, False, False, False, True, True, False],
 25   [True, False, False, True, True, False, False],
 26   [False, True, False, False, True, False, False],
 27   [False, True, False, False, False, False, False],
 28   [False, False, False, True, True, True, True],
 29   [False, False, False, False, False, False, False],
 30   [False, False, False, False, True, False, False]
 31 ]
 32 #[0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xD8, 0x80, 0x90]
 33 fndSegs = [21, 22, 23, 24, 25, 26, 27]
 34 fndSels = [19, 18, 17, 16]
 35
 36 stepPin = [6, 13, 5, 12]
 37
 38 GPIO.setmode(GPIO.BCM)
 # LED
 40 GPIO.setup(red_led, GPIO.OUT)
 41 GPIO.setup(blue_led, GPIO.OUT)
 42 GPIO.setup(green_led, GPIO.OUT)
 43 # PIR Sensor
 44 GPIO.setup(pirPin, GPIO.IN)
 45 # Relay
 46 GPIO.setup(relayPin, GPIO.OUT)
 47 # TIMER
 48 for seg in fndSegs:
 49   GPIO.setup(seg, GPIO.OUT)
 50   GPIO.output(seg, 0)
 51 for sel in fndSels:
 52   GPIO.setup(sel, GPIO.OUT)
 53   GPIO.output(sel, 1)
 54
 55
 56 # 초음파 센서로  거리계산
 57 def measure():
 58   GPIO.setup(trigPin, GPIO.OUT)
 59   GPIO.setup(echoPin, GPIO.IN)
 60
 61   GPIO.output(trigPin, True)
 62   time.sleep(0.00001)
 63   GPIO.output(trigPin, False)
 64
 65   start = time.time()
 66   stop = time.time()
 67
 68   while GPIO.input(echoPin) == 0:
 69     start = time.time()
 70
 71   while GPIO.input(echoPin) == 1:
 72     stop = time.time()
 73
 74   elapsed = stop -start
 75   distance = (elapsed * 19000) / 2
 76
   return distance
 78
 79 #step
 80 GPIO.setup(stepPin, GPIO.OUT)
 81
 82
 83 form_class = uic.loadUiType("./final01.ui")[0]
 84
 85 class WindowClass(QMainWindow, form_class):
 86   def __init__(self):
 87     super().__init__()
 88     self.setupUi(self)
 89     count = 0
 90
 91     self.timer = QTimer(self)
 92     self.timer.timeout.connect(self.updateDisplay)
 93
 94   def btn1Function(self):   # RED
 95     GPIO.output(red_led, False)
 96     GPIO.output(green_led, True)
 97     GPIO.output(blue_led, True)
 98     print("RED LED ON")
 99
100   def btn2Function(self):   # GREEN
101     GPIO.output(red_led, True)
102     GPIO.output(green_led, False)
103     GPIO.output(blue_led, True)
104     print("GREEN LED ON")
105
106   def btn3Function(self):   # BLUE
107     GPIO.output(red_led, True)
108     GPIO.output(green_led, True)
109     GPIO.output(blue_led, False)
110     print("BLUE LED ON")
111
112 # 버튼을 눌렀을 때 인체 감지되면 red_led에 불 들어오고 SENSOR ON 출력, 반대로 >
113   def btn4Function(self):   # PIR Sensor
114     if GPIO.input(pirPin) == True:
       GPIO.output(red_led, False)
116       print("SENSOR ON")
117
118     elif GPIO.input(pirPin) == False:
119       GPIO.output(red_led, True)
120       print("SENSOR OFF")
121       time.sleep(0.2)
122
123 # 버튼 누르면 blue_led 켜짐
124   def btn5Function(self):
125     GPIO.output(relayPin,1)
126     GPIO.output(blue_led, False)
127     print("BLUE_LED ON")
128
129 # Distance Calculation 버튼을 누르면 초음파 센서가 물체의 거리를 감지하고 콘솔>
130   def btn6Function(self):
131     distance = measure()
132     print("Distance: %.2f cm" %distance)
133     time.sleep(1)
134
135 # TIMER 버튼을 누르면 브레드 보드에 연결되어 있는 타이머가 돌아감
136   def startTimer(self):
137     self.count = 0
138     self.timer.start(1000)
139
140   def findOut(self, data, sel):
141     for h in range(0, 50):
142       for i in range(0, 7):
143         GPIO.output(fndSegs[i], fndDatas[data][i])
144       for j in range(0, 4):
145         if j == sel:
146           GPIO.output(fndSels[j], 1)
147         else:
148           GPIO.output(fndSels[j], 0)
149       time.sleep(0.0003)
150
151   def updateDisplay(self):
152     self.count += 1
     d1000 = self.count // 1000
154     d100 = self.count % 1000 // 100
155     d10 = self.count % 100 // 10
156     d1 = self.count % 10
157     d = [d1, d10, d100, d1000]
158
159     for i in range(3, -1, -1):
160       self.findOut(d[i], i)
161       time.sleep(0.003)
162     if self.count == 9999:
163       self.count = 0
164
165   def closeEvent(self, event):
166     GPIO.cleanup()
167     event.accept()
168
169 #Step
170   def clickFunction(self):
171     GPIO.output(stepPin[0], 1)
172     GPIO.output(stepPin[1], 0)
173     GPIO.output(stepPin[2], 0)
174     GPIO.output(stepPin[3], 0)
175
176 if __name__ == "__main__":
177   app = QApplication(sys.argv)
178   myWindow = WindowClass()
179   myWindow.show()
180   app.exec_()
