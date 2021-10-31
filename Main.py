import tensorflow as ts
import pyttsx3
from pytube.extract import playlist_id
from requests_cache import response
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
from tensorflow.python.keras.engine import training
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import spotify
import getpass
#import chatbot
import whatsapp
import json
import neuralintents
import pandas as plt
import pickle
from pandas_datareader.data import DataReader
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import imdb
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
from numpy.core.defchararray import mod

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classses.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("Done")
#imdb test part
'''ts.keras.datasets.imdb.load_data(
    path='', num_words=None, skip_top=0, maxlen=None, seed=113,
    start_char=1, oov_char=2, index_from=3
)'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def Speak(Text):
    print("   ")
    print(f": {Text}")
    engine.say(Text)
    print("  ")
    engine.runAndWait()

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizer...")
        query = command.recognize_google(audio, language='en-US')
        print(f"Your Command :  {query}\n")

    except:
        return "None"

    return query.lower()

def Task_Gui():

    def Music():
        Speak("Tell me name of the song!")
        musicName = takeCommand()

        if 'open music file' in musicName:
            os.startfile('C:\\Users\\Valtteri Sandström\\Music\\Music\\Aitch – Taste (Make It Shake) Official Video.webm')
        elif 'music.mp3' in musicName:
            os.startfile('C:\\Users\\Valtteri Sandström\\Music\\Music\\Aitch – Taste (Make It Shake) Official Video.webm')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Song has started, Enjoy sir!")

    def OpenApps():

        Speak("Very well sir") 
    
        if 'code' in query:
            os.startfile("C:\\Users\\valtt\\AppData\\Local\\Programs\\Microsoft VS Code")

        #elif 'telegram' in query:
         #   os.startfile("")

        elif 'chrome' in query: 
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe") #chrome path over here

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'maps' in query:
            webbrowser.open('https://wwww.google.com/maps/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'spotify' in query:
            os.startfile('C:\\Users\\Valtteri Sandström\\AppData\\Roaming\\Spotify\\Spotify') #path for spotify

        Speak("Task has been completed sir!")

    def Temp():
        search = "temperature in oulu is"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        Speak(f"The temperature outside is {temperature} celcius")

        Speak("Do you want some other places temperature ?")
        next = takeCommand()

        if 'yes' in next:
            Speak("Tell me name of the place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_= "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("Very well sir")

    def Dict():
        Speak("Activated dictionary")
        Speak("Tell me the problem")
        probl = takeCommand()
        
        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            Speak(f"The meaning for {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = Diction.synonym(probl)
            Speak(f"The synonym for {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("antonym of","")
            result = Diction.synonym(probl)
            Speak(f"The antonym for {probl} is {result}")

        Speak("Exit Dictionary!")

    def CloseAPPS():
        Speak("Very well sir , Just a second")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'Spotify' in query:
            os.system("TASKKILL /F /im Spotify.exe")

        Speak("Sir, Command Has been Succesfully completed!")

    def YoutubeAuto():
        Speak("What is your command, sir?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('1')
        
        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def TakeFinnish():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing...")
                query = command.recognize_google(audio,language='fin')
                print(f"You said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell me the Line!")
        line = TakeFinnish()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak(Text)

    def ChromeAuto():
        Speak("Chrome Automation stareted!")

        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def screenshot():
        Speak("Very well sir, What should I name this file ?")
        path = takeCommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\valtt\\OneDrive\\Kuvat\\Näyttökuvat\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\valtt\OneDrive\\Kuvat\\Näyttökuvat")
        Speak("Here is your screenshot Sir")

    while True:

        query = takeCommand()

        if 'hello' in query:
            Speak('Hello Sir! my name is Jarvis.')
            Speak('Your personal Ai Assistant!')
            Speak("How may I help you?")

        elif 'how are you' in query:
            Speak("I am fine sir, Thank you about asking")
            Speak("How about you?")

        elif 'go to sleep' in query:
            Speak("Very well Sir, You can call me anytime")
            Speak("Just say wake up Jarvis")
            break

        elif 'youtube search' in query:
            Speak("Very well Sir, I found this from your search!")
            query = query.replace("Jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("It is done Sir!")

        elif 'website' in query:
            Speak("Very well Sir, Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 +'.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell me the name of the Website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("It is done Sir!")

        elif 'music' in query:
            Music()

        elif 'temperature' in query:
            Temp()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki}")

        elif 'whatsapp message' in query:
            whatsapp()

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()
        
        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
 
        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takeCommand()
            Speak(f"You said : {jj}")

        elif 'my location' in query:
            Speak("Very well sir , just wait a second!")
            webbrowser.open('https://www.google.fi/maps')

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter the time please !")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to Wake up sir!")
                    playsound('C:\\Users\\Valtteri Sandström\\Music\\Music\\Aitch – Taste (Make It Shake) Official Video.webm')
                    Speak("Alarm closed")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter video Url here")
            Label(root,text = "Youtube video Downloader",font = 'arial 15bold').pack()
            link = StringVar()
            Label(root,text = "Paste Youtube video URL here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x=180,y=210) 

            Button(root,text = "Download",font = 'arial 15 bold',bg ='pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video downloaded")

        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            Speak("You told me to remind you that :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You tell me that" + remember.read())

        elif 'google search' in query:
            import wikipedia as googleScarp
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This is what I found from web!")

            try:
                result = googleScarp.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available")

        elif 'how to' in query:
            Speak("Getting data from internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func =search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        

Task_Gui()
