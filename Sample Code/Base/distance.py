import RPi.GPIO as GPIO
from time import sleep

def distance():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.IN)
    while True :
        GPIO.output(23, 0)
        sleep(0.00001)
        GPIO.output(24, 1)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(24) == 0:
            StartTime = time.time()
        while GPIO.input(24) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        now_distance = (TimeElapsed * 34300) / 2
        return now_distance

print(distance())
GPIO.cleanup()
