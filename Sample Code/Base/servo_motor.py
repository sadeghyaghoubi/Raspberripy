import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

pwm = GPIO.PWM(18,40)
pwm.start(7)
for i in range(0,3):
    pwm.ChangeDutyCycle(2.0)
    print ("rast")
    time.sleep(5)
    pwm.ChangeDutyCycle(9.0)
    print ("chap")
    time.sleep(5)
    pwm.ChangeDutyCycle(5.0)
    print ("mos")
    time.sleep(5)

pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.clenup()

