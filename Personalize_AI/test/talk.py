import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
     
