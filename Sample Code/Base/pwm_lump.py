import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)          
GPIO.setup(18, GPIO.OUT)   
pwm = GPIO.PWM(18, 100)   
try :
        pwm.start(100)   
        sleep (5)
        pwm.ChangeDutyCycle(50)
        sleep (5)
        pwm.ChangeDutyCycle(25)
        sleep(5)
except :
    pass
pwm.stop()
#try:
#    while 1:                   
#        for x in range(100):    
#            pwm.ChangeDutyCycle(x)
#            sleep(0.05)  
#
#        for x in range(100,0,-1):
#            pwm.ChangeDutyCycle(x)
#            sleep(0.05)

#except KeyboardInterrupt:
#    pass        


GPIO.cleanup()
