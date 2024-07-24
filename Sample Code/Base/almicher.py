import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)          
GPIO.setup(14, GPIO.OUT)   
GPIO.output(14, GPIO.LOW)
GPIO.output(14 , GPIO.HIGH)
sleep (5)

GPIO.cleanup()
