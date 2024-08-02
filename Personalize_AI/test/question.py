from talk import talk
import speech_recognition as sr
import subprocess
import webbrowser
import wikipedia
import converse 
import speedtest
import datetime
import weather 
import pyjokes
import pyttsx3
import random
import emoji
import time
import os

try:
    import pywhatkit
    pass
except:
    pass
def run_delta(command):
    converse.conversation(command)
    
    if 'time now' in command:
        strTime = datetime.datetime.now().strftime(" %I:%M:%S %p")
        talk(f"Sir, the time is  {strTime} ")
                    
    elif 'date today' in command:
        strDime = datetime.datetime.now().strftime(" %y %m %d")
        talk(f"sir the date today is {strDime} ")
            
    elif 'network speed' in command:
        st = speedtest.speedtest() 
        dl = st.download()
        up = st.upload()
        talk(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
         
    elif 'open youtube' in command:
        talk("opening youtube")
        webbrowser.open("youtube.com")
                                        
    elif 'open google' in command:
        talk("opening google")
        webbrowser.open("google.com")

    elif 'open chrome' in command:
        talk("opening google chrome.")
        webbrowser.open("Google Chrome.rar")
        
    elif 'open whatsapp' in command:
        talk("oppening whatsapp")
        webbrowser.open("https://www.google.com/")
                
    elif 'your favourite songs' in command:
        talk(" my favourite song is ")
        music_dir = 'E:\songs\delta song'
        songs = os.listdir(music_dir)    
        os.startfile(os.path.join(music_dir, songs[0]))
        
    elif 'my favourite tamil song' in command:
        talk("playing yor favourite song. ")
        tsongs = random.randint(0,30)
        music_dir = 'E:\songs\my tamil'
        songs = os.listdir(music_dir)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'my favourite english song' in command:
        talk("playing yor favourite song. ")
        ensongs = random.randint(0,15)
        music_dir = 'E:\songs\my english'
        songs = os.listdir(music_dir)    
        os.startfile(os.path.join(music_dir, songs[0]))
            
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)   

    elif 'refresh' in command:
        talk("ok sir refreshing the screen")
        os.system('cls')
        talk("refreshed the page and ready to go sir.")
        
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        talk(joke)
                   
    elif 'how ' in command:
        things= command.replace('how', '')
        info1 = wikipedia.summary(things, 2)
        talk(info1)

    elif 'what ' in command:
        person = command.replace('who is', '')
        info2 = wikipedia.summary(person, 2)
        talk(info2)
               
    elif 'who' in command:
        person = command.replace('who is', '')
        info3 = wikipedia.summary(person, 2)
        talk(info3)
            
    elif 'which' in command:
        definite = command.replace('which is', '')
        info4 = wikipedia.summary(definite, 2)
        talk(info4)
                                                
    elif 'where' in command:
        place = command.replace('where is', '')
        info5 = wikipedia.summary(place, 2)
        talk(info5)

    elif 'define' in command:
        defi = command.replace('define', '')
        info6 = wikipedia.summary(defi, 2)
        talk(info6)
        
    elif 'exit' in command or'close' in command:
        talk("ok sir")
        talk("i am happy to help you any time, i hope we meet again soon ")
        subprocess.run([exit], check=True)
    
    else:
        talk("I cant do this command")
        talk("sorry for the inconvenitent ")