import speech_recognition
import pyttsx3
import time
import pywhatkit


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

listen = speech_recognition.Recognizer()
engine = pyttsx3.init()
engine.say("hello boss ej,what can i do for you?")
engine.runAndWait()

def jarvis(text):
    if 'time' in text:
        engine.say('the time is '+current_time)
        engine.runAndWait()
    elif 'brother' in text:
        engine.say('the name of your brother is jhon daniel')
        engine.runAndWait()
    elif 'play' in text:
        cmd = text.replace('jarvis','')
        song = cmd.replace('play','')
        engine.say('playing '+ song)
        engine.runAndWait()
        pywhatkit.playonyt(song)
    elif 'love' in text:
        engine.say('i love you to boss')
        engine.runAndWait()

while True:
    try:
        with speech_recognition.Microphone() as source:
            print("listening")
            voice = listen.listen(source)
            command = listen.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                jarvis(command)
                if 'stop' in command:
                    engine.say('ok thank you boss ej')
                    engine.runAndWait()
                    break
            
    except:
        pass
