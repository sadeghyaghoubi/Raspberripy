import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("you said :", text)

