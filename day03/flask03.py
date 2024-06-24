 # URL 접속을 /led/on, /led/off로 접속하면 led를 on,off 하는 웹페이지

 from flask import Flask
 import RPi.GPIO as GPIO
 import time

 blue_led = 5

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(blue_led, GPIO.OUT)

 app = Flask(__name__)

 @app.route("/on")
 def on():
   GPIO.output(blue_led, False)
   return "<h1>LED ON</h1>"

 @app.route("/off")
 def off():
   GPIO.output(blue_led, True)
   return "<h1>LED OFF</h1>"

 if __name__ == "__main__":
   try:
     app.run(host="0.0.0.0", port="10011", debug=True)
   except KeyboardInterrupt:
     GPIO.cleanup()
