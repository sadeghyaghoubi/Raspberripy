import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

#control sorat A , B
GPIO.setup(12,GPIO.OUT)     # ENB
GPIO.setup(13,GPIO.OUT)     # ENA

#motorA Control jahat
GPIO.setup(2,GPIO.OUT)      # IN1
GPIO.setup(3,GPIO.OUT)      # IN2

#motorB Control jahat
GPIO.setup(17,GPIO.OUT)     # IN3
GPIO.setup(27,GPIO.OUT)     # IN4

PWMA = GPIO.PWM(12,100) #motorA
PWMB = GPIO.PWM(13,100) #motorA

#sorat kam
def ls():
    PWMA.start(50)
    PWMB.start(50)
    return
#sorat ziad
def hs():
    PWMA.start(100)
    PWMB.start(100)
    return
# harekat jolo
def hj():
    hs()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
    #sleep (10)
# harekat aghab
def ha():
    hs()
    GPIO.output(2,0)
    GPIO.output(17,0)
    GPIO.output(3,1)
    GPIO.output(27,1)
    #sleep (5)
def stop():
    GPIO.output(2,0)
    GPIO.output(17,0)
    GPIO.output(3,0)
    GPIO.output(27,0)

def ch1():
    ls()
    GPIO.output(2,1)
    GPIO.output(17,0)
    GPIO.output(3,0)
    GPIO.output(27,1)

def ch2():
    ls()
    GPIO.output(2,0)
    GPIO.output(17,1)
    GPIO.output(3,1)
    GPIO.output(27,0)
    #sleep(10)

                
hj()
sleep (2)
ha()
sleep(2)
ch1()
sleep(2)
ch2()
sleep(2)
GPIO.cleanup()
print ("b")
