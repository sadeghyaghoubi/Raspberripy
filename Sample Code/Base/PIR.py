import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(14 , GPIO.IN)
#GPIO.setup(15 , GPIO.IN)
#GPIO.setup(18 , GPIO.IN)
#GPIO.setup(23 , GPIO.IN)
#GPIO.setup(24 , GPIO.IN)
#GPIO.setup(25 , GPIO.IN)
#GPIO.setup(17 , GPIO.IN)
#GPIO.setup(27 , GPIO.IN)

#GPIO.setup (17 , GPIO.OUT)
#GPIO.output(17 , GPIO.LOW)
#sleep(2)

while True :
    if GPIO.input(14) == 1:
        print ("interrupt 1")
        time.sleep(0.1)
#    elif GPIO.input(15) == 1:
#        print ("interrupt 2")
#        time.sleep(0.1)
#    elif GPIO.input(18) == 0:
#        print ("interrupt 3")
#        time.sleep(0.1)
#    elif GPIO.input(23) == 0:
#        print ("interrupt 4 ")
#        time.sleep(0.1)
#    elif GPIO.input(24) == 0:
#        print ("interrupt 5 ")
#        time.sleep(0.1)
#    elif GPIO.input(25) == 0:
#        print ("interrupt 6 ")
#        time.sleep(0.1)
#    elif GPIO.input(17) == 0:
#        print ("interrupt 7 ")
#        time.sleep(0.9)
#    elif GPIO.input(27) == 0:
#        print ("interrupt 8 ")
#        time.sleep(0.1)
    else :
        print ("no interrupt")
#        GPIO.output (17 , GPIO.HIGH )
#        sleep(1)
#        GPIO.output(17 , GPIO.LOW)
GPIO.cleanup()
