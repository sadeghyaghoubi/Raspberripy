#importing libraries
import RPi.GPIO as GPIO
import time
#setting the gpio schema to bcm
GPIO.setmode(GPIO.BCM)
#define the pir pin
pirPin = 14
#setting the PIR pin to INPUT
GPIO.setup(pirPin, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(pirPin ):
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
