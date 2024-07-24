from pygame import mixer
from time import sleep

input_volume = int (input("Enter Volume (from 1 to 100) : "))
music_file = "Alireza Ghorbani - Roozegare Gharib.mp3"
mixer.init()
mixer.music.set_volume(input_volume)
mixer.music.load(music_file)
mixer.music.play()
sleep ( 10 )
# while True:
#     input_play = str(input("p = pause , u = unpause , q = exit : "))
#     if input_play == "p" :
#         mixer.music.pause()
#     elif input_play == "u" :
#         mixer.music.unpause()
#     elif input_play == "q" :
#         mixer.music.stop()
#         break
#     else :
#         print ("wrong input")