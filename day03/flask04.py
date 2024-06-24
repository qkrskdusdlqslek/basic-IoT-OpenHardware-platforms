 from flask import Flask
 import RPi.GPIO as GPIO
 import time

 blue_led = 5

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(blue_led, GPIO.OUT)

 app = Flask(__name__)

 @app.route("/")
 def hello():
   return "Hello World"

 @app.route("/led/<state>")
 def control_led(state):
   if state == "on":
     GPIO.output(blue_led, False)
   elif state == "off":
     GPIO.output(blue_led, True)
   elif state == "clear":
     GPIO.cleanup()
     return "GPIO Cleanup()"

 if __name__ == "__main__":
   try:
     app.run(host="0.0.0.0", port="10011", debug=True)
   except KeyboardInterrupt:
     GPIO.cleanup()
