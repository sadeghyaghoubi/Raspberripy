import time
import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
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


# harekat jolo speed
def hjs():
    hs()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
    #sleep (10)

def hjl():
    ls()
    GPIO.output(2,1)
    GPIO.output(17,1)
    GPIO.output(3,0)
    GPIO.output(27,0)
    sleep (10)
# harekat aghab speed
def has():
    hs()
    GPIO.output(2,0)
    GPIO.output(17,0)
    GPIO.output(3,1)
    GPIO.output(27,1)
    #sleep (5)

# harekat aghab speed
def hal():
    ls()
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
    hs()
    GPIO.output(2,1)
    GPIO.output(17,0)
    GPIO.output(3,0)
    GPIO.output(27,1)

def ch2():
    hs()
    GPIO.output(2,0)
    GPIO.output(17,1)
    GPIO.output(3,1)
    GPIO.output(27,0)
    #sleep(10)

    
now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)

    if command == '/golow':
        telegram_bot.sendMessage(chat_id, str("Go Forward (Low)"))
        hjl()


    elif command == '/gofast':
        telegram_bot.sendMessage(chat_id, str(
            "Go Forward (Fast)"))
        hjs()
    
    elif command == '/backlow':
        telegram_bot.sendMessage(chat_id, str(
            "Go Back (Slow)"))
        hal()


    elif command == '/backfast':
        telegram_bot.sendMessage(chat_id, str(
            "Go Back (Fast)"))
        has()
    
    elif command == '/stop':
        telegram_bot.sendMessage(chat_id, str( "Stop"))
        stop()
    


    elif command == '/turnleft':
        telegram_bot.sendMessage(chat_id, str(
            "Turn Left"))
        ch1()
        time.sleep(1)
        return
    elif command == '/turnright':
        telegram_bot.sendMessage(chat_id, str(
            "Turn Right"))
        ch2()
        time.sleep(1)
        return

    elif command == '/rotation':
        telegram_bot.sendMessage(chat_id, str(
            "Rotate"))
        ch1()
        time.sleep(3)
        ch2()
        time.sleep(3)    
         
#    elif command == '/time':
#        telegram_bot.sendMessage(chat_id, str(
#            now.hour)+str(":")+str(now.minute))
    # elif command == '/file':
    #     telegram_bot.sendDocument(
    #         chat_id, document=open('/home/pi/Desktop/fire_sms.py'))
    # elif command == '/picture':
    #     telegram_bot.sendDocument(chat_id, document=open(
    #         '/home/pi/Desktop/OpGL/3d-model.png'))

telegram_bot = telepot.Bot('5340104944:AAGbNPQltCXiaVAgDSsSiPMBfaZomO81WbA')

MessageLoop(telegram_bot, action).run_as_thread()
print('Lets have a chat session...')

while 1:
    time.sleep(10)
