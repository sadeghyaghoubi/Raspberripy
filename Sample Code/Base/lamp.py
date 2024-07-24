import RPi.GPIO as GPIO
import time, datetime


tedad = int(input("Lotfan tedade roshan shodan ra vared konid: "))
zaman= float(input("meghdar zaman roshan moondane cheragh (sanie) : "))
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

for i in range(tedad):
    GPIO.output(18,GPIO.LOW)
    time.sleep(zaman)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(zaman)

GPIO.cleanup() 
 
