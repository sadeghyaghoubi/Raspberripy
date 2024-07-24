from pygame import mixer
import time
import speech_recognition as sr
import time
import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# control sorat A , B
GPIO.setup(12, GPIO.OUT)     # ENB
GPIO.setup(13, GPIO.OUT)     # ENA

# motorA Control jahat
GPIO.setup(2, GPIO.OUT)      # IN1
GPIO.setup(3, GPIO.OUT)      # IN2

# motorB Control jahat
GPIO.setup(17, GPIO.OUT)     # IN3
GPIO.setup(27, GPIO.OUT)     # IN4

PWMA = GPIO.PWM(12, 100)  # motorA
PWMB = GPIO.PWM(13, 100)  # motorA

# sorat kam


def ls():
    PWMA.start(50)
    PWMB.start(50)
    return
# sorat ziad


def hs():
    PWMA.start(100)
    PWMB.start(100)
    return


# harekat jolo speed
def hjs():
    hs()
    GPIO.output(2, 1)
    GPIO.output(17, 1)
    GPIO.output(3, 0)
    GPIO.output(27, 0)
    #sleep (10)


def hjl():
    ls()
    GPIO.output(2, 1)
    GPIO.output(17, 1)
    GPIO.output(3, 0)
    GPIO.output(27, 0)
    time.sleep(3)
# harekat aghab speed


def has():
    hs()
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 1)
    GPIO.output(27, 1)
    #sleep (5)

# harekat aghab speed


def hal():
    ls()
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 1)
    GPIO.output(27, 1)
    time.sleep(3)


def stop():
    GPIO.output(2, 0)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 0)


def ch1():
    hs()
    GPIO.output(2, 1)
    GPIO.output(17, 0)
    GPIO.output(3, 0)
    GPIO.output(27, 1)
    time.sleep(3)


def ch2():
    hs()
    GPIO.output(2, 0)
    GPIO.output(17, 1)
    GPIO.output(3, 1)
    GPIO.output(27, 0)
    time.sleep(3)


def play_ringtone():
    music_file = "Ringtone.mp3"
    mixer.init()
    mixer.music.set_volume(100)
    mixer.music.load(music_file)
    mixer.music.play()
    time.sleep(2)


def play_howcanihelpyou():
    music_file = "howcanihelpyou.mp3"
    mixer.init()
    mixer.music.set_volume(100)
    mixer.music.load(music_file)
    mixer.music.play()
    time.sleep(2)


def play_myname():
    music_file = "mynametoday.mp3"
    mixer.init()
    mixer.music.set_volume(100)
    mixer.music.load(music_file)
    mixer.music.play()
    time.sleep(6)


def play_iloveyoutoo():
    music_file = "iloveyoutoo.mp3"
    mixer.init()
    mixer.music.set_volume(100)
    mixer.music.load(music_file)
    mixer.music.play()
    time.sleep(6)


def play_imfine():
    music_file = "imfine.mp3"
    mixer.init()
    mixer.music.set_volume(100)
    mixer.music.load(music_file)
    mixer.music.play()
    time.sleep(3)


def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text


while True:
    play_ringtone()
    call = voice_to_text()
    print(call)
    print("*" * 10)
    if str(call) == "how are you":
        play_howcanihelpyou()
        call1 = voice_to_text()
        if call1 == "go forward":
            hjl()
        elif call1 == "go back":
            hal()
        elif call1 == "turn left":
            ch1()
        elif call1 == "turn right":
            ch2()
        if call1 == "i love you":
            play_iloveyoutoo()
        elif call1 == "how are you":
            play_imfine()
    else:
        play_myname()
