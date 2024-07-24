import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# def control_motor ():
# control sorat A , B
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# motorA Control jahat
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# motorB Control jahat
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

PWMA = GPIO.PWM(12, 100)  # motorA
PWMB = GPIO.PWM(13, 100)  # motorA

# sorat kam


def low_speed():
    PWMA.start(50)
    PWMB.start(50)
    return
# sorat ziad


def fast_speed():
    PWMA.start(100)
    PWMB.start(100)
    return
# harekat jolo


def go_straight_ahead():
    low_speed()
    GPIO.output(2, 1)
    GPIO.output(17, 1)
    GPIO.output(3, 0)
    GPIO.output(27, 0)

# harekat aghab


def roll_back():
    low_speed()
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 1)
    GPIO.output(27, 1)
    time.sleep(2)


def stop():
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 0)


def go_left():
    fast_speed()
    GPIO.output(2, 1)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 1)


def go_right():
    fast_speed()
    GPIO.output(2, 0)
    GPIO.output(17, 1)
    GPIO.output(3, 1)
    GPIO.output(27, 0)


# Distance
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)


disright = []
disleft = []
#disahead = []


def distance_right():
    global disright
    for i in range(3):
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
        time.sleep(0.5)


def distance_left():
    global disleft
    for i in range(3):
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
        time.sleep(0.5)


def distance():
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
# Reset by pressing CTRL + C

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


# def servo_motor ():
def servo_right():
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 40)
    pwm.start(7)
    pwm.ChangeDutyCycle(2.0)
    print("right")
    time.sleep(1.5)
    pwm.ChangeDutyCycle(0)
    pwm.stop()


def servo_left():
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 40)
    pwm.start(7)
    pwm.ChangeDutyCycle(9.0)
    print("left")
    time.sleep(1.5)
    pwm.ChangeDutyCycle(0)
    pwm.stop()


def servo_ahead():
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 40)
    pwm.start(7)
    pwm.ChangeDutyCycle(5.0)
    print("ahead")
    pwm.ChangeDutyCycle(0)
    pwm.stop()


while True:
    servo_ahead()
    print("servo ahead")
    go_straight_ahead()
    print("go1")
    diss = distance()
    print(diss)
    if diss < 20:
        stop()
#        roll_back()
        time.sleep(1)
#        stop()
#        time.sleep(1)
        while True:
            servo_right()
            print("servo is right")
            distance_right()
            mindisright = min(disright)
            print(mindisright)

            servo_left()
            distance_left()
            mindisleft = min(disleft)
            print(mindisleft)

            if mindisright > mindisleft:
                servo_ahead()
                print ("go right")
                go_right()
                time.sleep(0.4)
#               control_motor(go_straight_ahead())
                break
            elif mindisleft > mindisright:
                servo_ahead()
                print ("go left")
                go_left()
                time.sleep(0.4)
#                    control_motor(go_straight_ahead())
                break
            else:
                print ("etmam")
                roll_back()
                time.sleep(2)
                break

GPIO.cleanup()
