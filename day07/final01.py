from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QTimer

# PIN 설정 
red_led = 13
green_led = 12
blue_led = 6

pirPin = 4

relayPin = 5

trigPin = 6
echoPin = 5

fndDatas = [
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
fndSegs = [21, 22, 23, 24, 25, 26, 27]
fndSels = [19, 18, 17, 16]

stepPin = [6, 13, 5, 12]

piezoPin = 12
melody = [130, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
# LED
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# PIR Sensor
GPIO.setup(pirPin, GPIO.IN)

# Relay
GPIO.setup(relayPin, GPIO.OUT)

# TIMER
for seg in fndSegs:
	GPIO.setup(seg, GPIO.OUT)
	GPIO.output(seg, 0)
for sel in fndSels:
	GPIO.setup(sel, GPIO.OUT)
	GPIO.output(sel, 1)

# STEP 모터
GPIO.setup(stepPin, GPIO.OUT)
GPIO.output(stepPin, 1)

# 피에조
GPIO.setup(piezoPin, GPIO.OUT)

# 초음파 센서로 거리계산
def measure():
	GPIO.setup(trigPin, GPIO.OUT)
	GPIO.setup(echoPin, GPIO.IN)

	GPIO.output(trigPin, True)
	time.sleep(0.00001)
	GPIO.output(trigPin, False)

	start = time.time()
	stop = time.time()

	while GPIO.input(echoPin) == 0:
		start = time.time()

	while GPIO.input(echoPin) == 1:
		stop = time.time()

	elapsed = stop -start
	distance = (elapsed * 19000) / 2

	return distance

#step
GPIO.setup(stepPin, GPIO.OUT)
	

form_class = uic.loadUiType("./final01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		count = 0
		
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateDisplay)

	def btn1Function(self):   # RED
		GPIO.output(red_led, False)
		GPIO.output(green_led, True)
		GPIO.output(blue_led, True)
		print("RED LED ON")

	def btn2Function(self):   # GREEN
		GPIO.output(red_led, True)
		GPIO.output(green_led, False)
		GPIO.output(blue_led, True)
		print("GREEN LED ON")

	def btn3Function(self):   # BLUE
		GPIO.output(red_led, True)
		GPIO.output(green_led, True)
		GPIO.output(blue_led, False)
		print("BLUE LED ON")

# 버튼을 눌렀을 때 인체 감지되면 red_led에 불 들어오고 SENSOR ON 출력, 반대로 red_led 꺼지고 SENSOR OFF 출력
	def btn4Function(self):   # PIR Sensor
		if GPIO.input(pirPin) == True:
			GPIO.output(red_led, False)
			print("SENSOR ON")

		elif GPIO.input(pirPin) == False:
			GPIO.output(red_led, True)
			print("SENSOR OFF")
			time.sleep(0.2)

# 버튼 누르면 blue_led 켜짐
	def btn5Function(self):
		GPIO.output(relayPin,1) 
		GPIO.output(blue_led, False)
		print("BLUE_LED ON")

# Distance Calculation 버튼을 누르면 초음파 센서가 물체의 거리를 감지하고 콘솔에 거리 출력		
	def btn6Function(self):
		distance = measure()
		print("Distance: %.2f cm" %distance)
		time.sleep(1)

# TIMER 버튼을 누르면 브레드보드에 연결되어 있는 타이머가 돌아감	
  def startTimer(self):
		self.count = 0
		self.timer.start(1000)

	def findOut(self, data, sel):
		for h in range(0, 50):
			for i in range(0, 7):
				GPIO.output(fndSegs[i], fndDatas[data][i])
			for j in range(0, 4):
				if j == sel:
					GPIO.output(fndSels[j], 1)
				else:
					GPIO.output(fndSels[j], 0)
			time.sleep(0.0003)

	def updateDisplay(self):
		self.count += 1
		d1000 = self.count // 1000
		d100 = self.count % 1000 // 100
		d10 = self.count % 100 // 10
		d1 = self.count % 10
		d = [d1, d10, d100, d1000]

		for i in range(3, -1, -1):
			self.findOut(d[i], i)
			time.sleep(0.003)
		if self.count == 9999:
			self.count = 0

	def closeEvent(self, event):
		GPIO.cleanup()
		event.accept()

#Step 버튼을 누를 때 마다 진동이 느껴짐	
  def clickFunction(self):
		GPIO.output(stepPin[0], 1)
		GPIO.output(stepPin[1], 1)
		GPIO.output(stepPin[2], 0)
		GPIO.output(stepPin[3], 0)
		time.sleep(0.01)
		GPIO.output(stepPin[0], 0)
		GPIO.output(stepPin[1], 1)
		GPIO.output(stepPin[2], 1)
		GPIO.output(stepPin[3], 0)
		time.sleep(0.01)
		GPIO.output(stepPin[0], 0)
		GPIO.output(stepPin[1], 0)
		GPIO.output(stepPin[2], 1)
		GPIO.output(stepPin[3], 1)
		time.sleep(0.01)
		GPIO.output(stepPin[0], 1)
		GPIO.output(stepPin[1], 0)
		GPIO.output(stepPin[2], 0)
		GPIO.output(stepPin[3], 1)
		time.sleep(0.01)

# 피에조 (MUSIC 버튼을 누르면 '도레미파솔라시도' 소리가 나옴)
	def musicStart(self):
		Buzz = GPIO.PWM(piezoPin, 440)

		Buzz.start(30)
		for i in range(0, len(melody)):
			Buzz.ChangeFrequency(melody[i])
			time.sleep(0.3)
		Buzz.stop()
		time.sleep(1)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
