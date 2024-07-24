import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 40)
pwm.start(7)


def servo_right():
    pwm.ChangeDutyCycle(3.0)
    time.sleep(5)


def servo_left():
    pwm.ChangeDutyCycle(12.0)
    time.sleep(5)


def servo_ahead():
    pwm.ChangeDutyCycle(6.5)


pwm.ChangeDutyCycle(0)
pwm.stop()
servo_right()
time.sleep(5)
