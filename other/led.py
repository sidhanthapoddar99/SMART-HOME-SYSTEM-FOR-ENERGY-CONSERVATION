import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
print ("LED on")
while True:
    GPIO.output(22,GPIO.HIGH)
time.sleep(1)
#print "LED off"
#GPIO.output(18,GPIO.LOW)
