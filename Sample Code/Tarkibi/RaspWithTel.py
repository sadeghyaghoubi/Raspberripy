import time
import datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()
telegram_bot = telepot.Bot('5267439648:AAGJZaWJpq22npls3y70Kvc3lerLcKy_10g')
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str(
            "Hi sadegh!! Welcome to Learn Electronics"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(
            now.hour)+str(":")+str(now.minute))
    # elif command == '/file':
    #     telegram_bot.sendDocument(
    #         chat_id, document=open('/home/pi/Desktop/fire_sms.py'))
    # elif command == '/picture':
    #     telegram_bot.sendDocument(chat_id, document=open(
    #         '/home/pi/Desktop/OpGL/3d-model.png'))

#telegram_bot = telepot.Bot('5267439648:AAGJZaWJpq22npls3y70Kvc3lerLcKy_10g')

MessageLoop(telegram_bot, action).run_as_thread()
print('Lets have a chat session...')

while 1:
    time.sleep(10)
