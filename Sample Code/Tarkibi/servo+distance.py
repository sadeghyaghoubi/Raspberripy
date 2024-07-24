import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)


disright = []
disleft = []
disahead = []
def distance_right():
    global disright
    for i in range(5) :
        GPIO.output(23, True)
        time.sleep(0.00001)
        GPIO.output(23, False)
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(24) == 0:
            StartTime = time.time()
        while GPIO.input(24) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        now_distance = (TimeElapsed * 34300) / 2
#        print (now_distance)
        disright.append(now_distance)
        time.sleep(1)


def distance_ahead():
    global disahead
    for i in range(5) :
        GPIO.output(23, True)
        time.sleep(0.00001)
        GPIO.output(23, False)
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(24) == 0:
            StartTime = time.time()
        while GPIO.input(24) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        now_distance = (TimeElapsed * 34300) / 2
#        print (now_distance)
        disahead.append(now_distance)
        time.sleep(1)


def distance_left():
    global disleft
    for i in range(5) :
        GPIO.output(23, True)
        time.sleep(0.00001)
        GPIO.output(23, False)
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(24) == 0:
            StartTime = time.time()
        while GPIO.input(24) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        now_distance = (TimeElapsed * 34300) / 2
#        print (now_distance)
        disleft.append(now_distance)
        time.sleep(1)





def servo_right():
    GPIO.setup(18,GPIO.OUT)
    pwm = GPIO.PWM(18,40)
    pwm.start(7)
    pwm.ChangeDutyCycle(2.5)
    print ("right")
    time.sleep(5)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    



def servo_left():
    GPIO.setup(18,GPIO.OUT)
    pwm = GPIO.PWM(18,40)
    pwm.start(7)
    pwm.ChangeDutyCycle(11)
    print ("left")
    time.sleep(5)
    pwm.ChangeDutyCycle(0)
    pwm.stop()


def servo_ahead():
    GPIO.setup(18,GPIO.OUT)
    pwm = GPIO.PWM(18,40)
    pwm.start(7)
    pwm.ChangeDutyCycle(6.2)
    print ("ahead")
    time.sleep(5)
    pwm.ChangeDutyCycle(0)
    pwm.stop()






servo_right()
distance_right()
mindisright = min(disright)
print (mindisright)


servo_left()
distance_left()
mindisleft = min(disleft)
print (mindisleft)


servo_ahead()
distance_ahead()
mindisahead = min (disahead)
print (mindisahead)



GPIO.cleanup()


