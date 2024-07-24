import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14 ,GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup(15,GPIO.OUT)


################HARVAGHT DOKME FESHAR DADE BESHE LAMP 2 SANIE ROSHAN MISHE####################
def TURN_ON_2_SEC ():

    while True:
        button_state = GPIO.input(14)
        if button_state == False :
            GPIO.output(15 , True)
            time.sleep(2)        
        else :
            GPIO.output(15, False)

###############BA HARBAR FESHAR DADANE KLID , CHERAGH TAGHIR VAZIAT MIDE #######################
now_state= False

def TAGHIR_VAZIAT_BA_CLICK ():
    global now_state
    if now_state == False :
        now_state = True
        return 
    elif now_state == True :
        now_state = False
        return

def MAIN_CHANGE_LAMP ():
    while True :
        if GPIO.input(14):
            TAGHIR_VAZIAT_BA_CLICK()
    
        elif now_state  == False :
            print ("Khamoosh")
            GPIO.output(15 , False)
        else :
            print ("roshan")
            GPIO.output (15 , True)

#TURN_ON_2_SEC()
MAIN_CHANGE_LAMP()
GPIO.cleanup()






