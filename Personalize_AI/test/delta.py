import speech_recognition as sr
from talk import talk
import question
import converse
import webbrowser                                                              
import wikipedia
import speedtest
import datetime             
import pyjokes
import pyttsx3
import random                   
import emoji
import time
import os
    
name='delta'
gender=1

try:
    import pywhatkit
    pass
except:
    talk("please connect to internet")
    time.sleep(5)
    exit()

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gender].id)   
talk("hi sir. it's nice to see you again")
talk(f"I am {name}, your person assistant. on service and ready to go .")

def take_command():
    try:
         with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                converse.commantalk(command)
                command = command.replace(name, '')
                
    except Exception as e:
        talk("sorry sir, i can't here you.")
        talk("can you say that again for me please...")
        
        return ""
    return command
 
while True:
    command =take_command()
    question.run_delta(command)