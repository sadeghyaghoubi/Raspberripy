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


def stop():
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 0)


def go_left():
    low_speed()
    GPIO.output(2, 1)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 1)


def go_right():
    low_speed()
    GPIO.output(2, 0)
    GPIO.output(17, 1)
    GPIO.output(3, 1)
    GPIO.output(27, 0)


# def ultrasonic() :
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)


def distance():
    GPIO.output(23, True)
    time.sleep(0.00001)
    GPIO.output(24, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(24) == 0:
        StartTime = time.time()
    while GPIO.input(24) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    now_distance = (TimeElapsed * 34300) / 2
    return now_distance

# try:
#     while True:
#         dist = distance()
#         print ("Measured Distance = %.1f cm" % dist)
#         sleep(1)
# # Reset by pressing CTRL + C
# except KeyboardInterrupt:
#     print("Measurement stopped by User")


# def servo_motor ():
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(7)


def servo_right():
    pwm.ChangeDutyCycle(1.0)
    time.sleep(5)


def servo_left():
    pwm.ChangeDutyCycle(12.0)
    time.sleep(5)


def servo_ahead():
    pwm.ChangeDutyCycle(7.0)


pwm.ChangeDutyCycle(0)
pwm.stop()


while True:
    servo_ahead()
    go_straight_ahead()
    if distance() < 30:
        stop()
        roll_back()
        time.sleep(2)
        while True:
            servo_right()
            time.sleep(5)
            if distance() > 80:
                servo_ahead()
                go_right()
                time.sleep(2)
#               control_motor(go_straight_ahead())
                break
            elif servo_left():
                if distance() > 80:
                    servo_ahead()
                    go_left()
                    time.sleep(2)
#                    control_motor(go_straight_ahead())
                    break
            else:
                roll_back()
                time.sleep(4)
                break

GPIO.cleanup()
