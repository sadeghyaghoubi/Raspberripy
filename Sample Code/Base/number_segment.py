import RPi.GPIO as GPIO

import time

#tedad = int(input("Lotfan tedade roshan shodan ra vared konid: "))
#zaman= float(input("meghdar zaman roshan moondane cheragh (sanie) : "))


GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(27,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)

#GPIO.output(27,GPIO.HIGH)
#GPIO.output(22,GPIO.HIGH)
#GPIO.output(4,GPIO.HIGH)
#GPIO.output(14,GPIO.HIGH)
#GPIO.output(15,GPIO.HIGH)
#GPIO.output(17,GPIO.HIGH)
#GPIO.output(18,GPIO.HIGH)
while True :
    GPIO.output(4,GPIO.LOW)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)

    user_input = int (input("Pleas enter your number : "))
    
    if user_input == 1 :
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 2:
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 3 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 4 :
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 5 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 6 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 7 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 8 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)

    elif user_input == 9 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)
    else :
        print ("Your number is incorrect ! ")





#time.sleep (5)
#for i in range(5):
#    GPIO.output(18,GPIO.LOW)
#    time.sleep(0.5)
#    GPIO.output(18,GPIO.HIGH)
#    time.sleep(0.5)

GPIO.cleanup() 
 
