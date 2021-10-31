import pyttsx3
from pytube.extract import playlist_id
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
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
#import ChatBot
import whatsapp


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',190)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    Assistant.say(audio)
    print("   ")
    Assistant.runAndWait()

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio,language='en-US')
            print(f"You said : {query}")

        except:
            return "none"

        return query.lower()

def TaskExe():

    Speak("Hello, My name is Jarvis.")
    Speak("How may I help You ?")

    def Music():
        Speak("Tell me name of the song!")
        musicName = takeCommand()

        if 'open music file' in musicName:
            os.startfile('C:\\Users\\valtt\\Music\\music.mp3\\yt1s.com - RISE ft The Glitch Mob Mako and The Word Alive  Worlds 2018  League of Legends.mp4')

        elif 'music.mp3' in musicName:
            os.startfile('C:\\Users\\valtt\\Music\\music.mp3\\yt1s.com - RISE ft The Glitch Mob Mako and The Word Alive  Worlds 2018  League of Legends.mp4')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Song has started, Enjoy sir!")

    def Whatsapp():
        Speak("Tell me name of the person!")
        name = takeCommand()
        
        if 'Valtteri' in name:
            Speak("Tell me the message!")
            msg = takeCommand()
            Speak("Tell me the time sir")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+358504936222", msg,hour,min,20)
            Speak("Very well sir , Sending Whatsapp message!")

        elif 'Sandström' in name:
            Speak("Tell me the message!")
            msg = takeCommand()
            Speak("Tell me the time sir")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+358504936222", msg,hour,min,20)
            Speak("Very well sir , Sending Whatsapp message!")

        else:
            Speak("Tell me phone number!")
            phone = int(takeCommand())
            ph = '+358' + phone
            Speak("Tell me the message!")
            msg = takeCommand()
            Speak("Tell me the time sir")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Very well sir , Sending Whatsapp message!")

    
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


        Speak("Task has been complited sir!")

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

#async def spotify():
 #   playlist_uri = input("playlist_uri: ")
  #  client_id = input("client_id: ")
   # secret = getpass.getpass("application secret")
    #token = getpass.getpass("user token: ")

    #async with spotify.Client(client_id, secret) as client:
     #   user = await spotify.User.from_token(client, token)

      #  async for playlist in user:
       #     if playlist_uri == playlist_uri:
        #        return await playlist.sort(reverse=True, key=)


    def Reader():
        Speak("Tell me the name of the book!")

        name =  takeCommand()

        if 'finland' in name:
            
            os.startfile('') #path for book
            book = open('')  #path for book
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book is {pages}")
            Speak("From Which Page I can start reading ?")
            numPage = int(input("Enter the page number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In wich Language, I can read ?")
            lang = takeCommand()

            if 'fin' in lang:
                transl = Translator()
                textFin = transl.translate(text, 'fin')
                textm = textFin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'europe' in name:
            os.startfile('') #path for book
            book = open('')  #path for book
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book is {pages}")
            Speak("From Which Page I can start reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In wich Language, I can read ?")
            lang = takeCommand()

            if 'fin' in lang:
                transl = Translator()
                textFin = transl.translate(text, 'fin')
                textm = textFin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)            

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

        elif 'you need a break' in query:
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

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki}")

        elif 'whatsapp message' in query:
            Whatsapp()

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
            webbrowser.open('https://www.google.fi/maps/@65.0313728,25.4640128,11z?hl=fi')

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
                    playsound('C:\\Users\\valtt\\Music\\music.mp3')
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

        elif 'read books' in query:
            Reader()

def Task_Gui():
    while True:

        query = takeCommand()

        if 'hello' in query:
            
            Speak("Hello; how are you sir!")

        elif 'whatsapp message' in query:
            query = query.replace("jarvis","")
            query = query.replace("send","")
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            name = query 

            if 'Valtteri' in name:
                numb = "0504936222"
                Speak(f"What's The Message for{name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)

            elif 'Sandsdtröm' in name:
                numb ="0504936222"
                Speak(f"What's The Message for{name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)

            elif 'Himos' in name:
                gro = "" #link to invite group
                Speak(f"What's the message for{name}")
                mess = takeCommand()
                whatsapp.Whatsapp_Grp(gro,mess)


TaskExe()

            

