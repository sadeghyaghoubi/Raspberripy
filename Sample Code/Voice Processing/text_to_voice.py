from gtts import gTTS


def convert_text_to_speech(text):
    audio = gTTS(text)
    audio.save("voicefile1.mp3")


convert_text_to_speech("I'm fine thank you")
