import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import json
from urllib.request import urlopen
import time
import random
import wolframalpha

wolframalpha_app_id = 'your wolframalpha id'


engine = pyttsx3.init()


def speak(audio):
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', voice_id)
    engine.say(audio)
    engine.runAndWait()


def Clock():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print("Que :",query)
    print("Ans :",Time)
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    print("Que :", query)
    print("Ans :", day,"/",month,"/",year)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)


def Greetings():

    lst = ['Hello', 'Hii!', 'Hey there!', 'Howdy!', 'Hey!']
    greet = random.choice(lst)
    print(greet,"Welcome!")
    speak(greet)

    speak("Welcome!")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <12 :
        print("Good Morning Sir!")
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif 17 >= hour < 19:
        print("Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print("Good Night Sir!")
        speak("Good Night Sir!")

    print("JARVIS at your service. Tell me, what can i do for you ?")
    speak("JARVIS at your service. Tell me, what can i do for you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        Query = r.recognize_google(audio, language='en-in')
        print(Query)

    except Exception as E:
        print(E)
        speak("I didn't get that, can you say that again please?")

        return "None"
    return Query

def screenshot():
    img = pyautogui.screenshot()
    print("Screenshot has taken successfully!!")
    img.save("D:\JARVIS\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = str(psutil.cpu_stats())
    print(battery)
    speak("CPU states are "+battery)


if __name__ == "__main__":
     Greetings()
     while True:
         query = takeCommand().lower()

         if 'time' in query:
             Clock()

         elif 'date' in query:
             date()

         elif 'wikipedia' in query:
             print("Wait a moment, I am searching it !")
             speak("Wait a moment, I am searching it !")
             query = query.replace("wikipedia","")
             result = wikipedia.summary(query, sentences=2)
             print(result)
             speak(result)

         elif 'search in chrome' in query:
             print("Que : What should i search ?")
             speak("What should i search ?")
             search = takeCommand().lower()
             wb.get('chrome %s').open_new_tab(search+'.com')

         elif 'play song' in query:
             songs_dir = 'D:\Music'
             songs = os.listdir(songs_dir)
             os.startfile(os.path.join(songs_dir,songs[0]))

         elif 'remember' in query:
             print("Que : What should i remember sir ??")
             speak("What should i remember sir ??")
             data = takeCommand()
             print("Ans :",data)
             speak("You said me to remember "+data)
             remember = open('data.txt','a')
             remember.write(data+'\n')
             remember.close()

         elif 'do you know anything' in query:
             remember = open('data.txt','r')
             print(remember)
             speak("You said me to note down that "+remember.read())

         elif 'screenshot' in query:
             screenshot()
             speak("I have taken the screenshot !")

         elif 'cpu' in query:
             cpu()

         elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=0e75538ed73a4deeafe3cff3704f827f")
                data = json.load(jsonObj)
                i = 1

                speak("Here I have some top headlines for you!!")
                print("=================== TOP HEADLINES ===================="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(e)

         elif 'where is' in query:
             query = query.replace("where is","")
             location = query.lower()
             speak("You asked to locate "+location)
             wb.get('chrome %s').open_new_tab("https://www.google.com/maps/dir/"+location)

         elif 'stop listening' in query:
             speak("For how many seconds you want me to stop listening to your commands ?")
             ans = int(takeCommand())
             time.sleep(ans)
             print(ans)

         elif 'calculate' in query:
             client = wolframalpha.Client(wolframalpha_app_id)
             indx = query.lower().split().index('calculate')
             query = query.split()[indx + 1:]
             res = client.query(''.join(query))
             answer = next(res.results).text
             print('The answer is :' + answer)
             speak('The answer is :' + answer)

         elif 'offline' in query:
             speak("Okay sir, see you later!!")
             break
