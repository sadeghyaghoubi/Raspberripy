import RPi.GPIO as GPIO
import time

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

#IR Module
GPIO.setup(14 , GPIO.IN)
GPIO.setup(15 , GPIO.IN)
GPIO.setup(18 , GPIO.IN)
GPIO.setup(23 , GPIO.IN)
GPIO.setup(24 , GPIO.IN)
GPIO.setup(21 , GPIO.IN)
GPIO.setup(20 , GPIO.IN)
GPIO.setup(16 , GPIO.IN)


PWMA = GPIO.PWM(12,100) #motorA
PWMB = GPIO.PWM(13,100) #motorB

#sorat kam
def ls():
    PWMA.start(80)
    PWMB.start(80)
    return
#sorat ziad
def hs():
    PWMA.start(100)
    PWMB.start(100)
    return
#sorat ziad
def pwmrast5():
    PWMA.start(70)
    PWMB.start(80)
    return
#sorat ziad
def pwmchap4():
    PWMA.start(80)
    PWMB.start(70)
    return
#sorat ziad
def pwmchap34():
    PWMA.start(80)
    PWMB.start(60)
    return
#sorat ziad
def pwmrast56():
    PWMA.start(60)
    PWMB.start(80)
    return

#sorat ziad
def pwmchap3():
    PWMA.start(80)
    PWMB.start(50)
    return
#sorat ziad
def pwmrast6():
    PWMA.start(10)
    PWMB.start(80)
    return

# harekat jolo
def h45():
    ls()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
    #sleep (10)
# harekat aghab
def h4():
    pwmrast5()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
def h5():
    pwmchap4()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
def h6():
    pwmrast6()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
def h3():
    pwmchap3()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
def h34():
    pwmchap34()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
def h56():
    pwmrast56()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)


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
#    ls()
    GPIO.output(2,1)
    GPIO.output(17,0)
    GPIO.output(3,0)
    GPIO.output(27,1)

def ch2():
#    ls()
    GPIO.output(2,0)
    GPIO.output(17,1)
    GPIO.output(3,1)
    GPIO.output(27,0)
    #sleep(10)

while True :
    sensor1 = GPIO.input(14)
    sensor2 = GPIO.input(15)
    sensor3 = GPIO.input(18)
    sensor4 = GPIO.input(23)
    sensor5 = GPIO.input(24)
    sensor6 = GPIO.input(21)
    sensor7 = GPIO.input(20)
    sensor8 = GPIO.input(16)
    
    if sensor4 == 1 and sensor5 == 1 :
        print ("didam")
        h45()
    elif sensor4 == 1 :
        print ("chap4")
        time.sleep(0.1)
        h4()
    elif sensor5 == 1 :
        print ("rast5")
        time.sleep(0.1)
        stop()
    elif sensor3 == 1 :
        print ("chap3")
        time.sleep(0.1)
        h3()
    elif sensor6 == 1 :
        print ("rast6")
        time.sleep(0.1)
        h6()
    elif sensor5 == 1 and sensor6 == 1:
        print ("rast56")
        time.sleep(0.1)
        h56()
    elif sensor3 == 1 and sensor4 == 1:
        print ("chap34")
        time.sleep(0.1)
        h34()

    else :
        print ("no interrupt")
        stop()

GPIO.cleanup()






