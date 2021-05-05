from random import *

import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import os
import wolframalpha
import pywhatkit
import tkinter as Tkinter
import time
from pywikihow import search_wikihow
import winsound
# sapi5 - Microsoft Speech API (reference - https://en.wikipedia.org/wiki/Microsoft_Speech_API)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',170)
Jokes = ['You are my loop condition. I keep coming back to you.', 'Hello there fuck off']

# This is for voices in your computer
# David and Zira are two by default voices given by Microsoft
# print(voices[1])
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if 0 <= hour < 12:
        speak("Good Morning!!!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!!!")

    elif 18 <= hour <= 20:
        speak("Good Evening!!")
    else:
        speak("Good Night!!!")
    speak("Hello Sir I am Jarvis, How may I help you?")


def takeCommand():
    # It takes microphone input form user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening sir.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        Query = r.recognize_google(audio, language='en-in')
        print(f"You said: {Query}\n")

    except Exception:
        # print(e)
        speak("Say that again please.....")
        # print("Say that again please.....")
        return "None"
    return Query


def wishingAhead():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Bye sir... Have a grate day ahead")

    elif 12 <= hour < 18:
        speak("Good Bye sir... Have a grate day ahead")

    else:
        speak("Good Bye sir.... Sweet Dreams sir!!")


if __name__ == "__main__":

    # speak("Hello Jaynish")
    wishMe()
    while True:
        query = takeCommand().lower()
        Rest = ['go to sleep', 'sleep', 'bye', 'bye jarvis', 'take some rest', 'you need rest',
                'you worked a lot today '
                'go take rest','goodbye']
        if query in Rest:
            wishingAhead()
            exit(0)
        Thanks = ['Thanks for help', 'thanks for help', 'thanks for help', 'thank you for helping me out']
        if query in Thanks:
            speak("I am always at your service sir...")
            wishingAhead()
            exit(0)
        # Logic for executing takes based on query

        if 'wikipedia' in query:
            speak('Searching.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'tell me some jokes jarvis' in query:
            random_entry = choice(Jokes)
            print(type(random_entry))

        elif 'joke' in query or 'tell me a joke' in query:
            random_entry = choice(Jokes)
            print(type(random_entry))

        elif 'open Wikipedia' in query:
            speak('Opening sir...!!')
            os.startfile('https://en.wikipedia.org/wiki/Wikipedia')

        elif 'open youtube' in query:
            speak("What do you want me to search in YouTube??")
            search = takeCommand()
            if search != "None" or search != "none":
                speak('Opening sir...!!')
                os.startfile("https://youtube.com/search?q=%s" % search)
            else:
                speak("I did not get that sir!!")

        elif 'open google' in query:
            speak("What do you want me to search in google??")
            search = takeCommand()
            if search is not None:
                speak('Opening sir...!!')
                os.startfile("https://google.com/search?q=%s" % search)
            else:
                speak("I did not get that sir!!")
            # speak('Opening sir...!!')
            # os.startfile("https://www.google.com/")

        elif 'open edge' in query:
            try:
                speak('Opening sir...!!')
                os.system('start msedge')
            except Exception as e:
                speak('You might not be having this application')

        elif 'open chrome' in query:
            try:
                speak('Opening sir...!!')
                os.system('start chrome') or os.system("google-chrome")
            except Exception as e:
                speak('You might not be having this application')

        elif 'open stack overflow' in query:
            speak('Opening sir...!!')
            os.startfile("https://stackoverflow.com/")

        elif 'open whatsapp' in query:
            speak('Opening sir...!!')
            os.startfile("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir time is {strTime}")

        elif 'open vs code' in query:
            try:
                speak('Opening sir...!!')
                os.system("code -n")
            except Exception as e:
                speak('You might not be having this application')

        elif 'open settings' in query:
            speak('Opening sir ...!!')
            os.system("start ms-settings:")

        elif 'open my current code' in query:
            try:
                speak('Opening sir...!!')
                os.system("code .")
            except Exception as e:
                speak('You might not be having this application')

        elif 'word' in query or 'open word file' in query or 'open word' in query:
            try:
                speak('Opening sir...!!')
                os.system("start winword.exe")
            except Exception as e:
                speak('You might not be having this application')

        elif 'open powerpoint' in query or 'powerpoint' in query:
            try:
                speak('Opening sir...!!')
                os.system("start powerpnt")
            except Exception as e:
                speak('You might not be having this application')

        elif 'excel' in query:
            try:
                speak('Opening sir...!!')
                os.system("start excel")
            except Exception as e:
                speak('You might not be having this application')

        elif 'open notepad' in query or 'notepad' in query:
            speak('Opening sir...!!')
            os.system("notepad")

        elif 'shutdown the system' in query or 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'how to do' in query or 'i want to learn ' in query or 'how can i learn this' in query or 'I want to learn' in query or 'how to' in query or 'How to'in query:
            speak('Please tell what you want to do or know ?')
            comm=takeCommand()
            max_results=1
            how_to=search_wikihow(comm,max_results)
            #assert len(how_to) ==1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'restart the system' in query:
            os.system("shutdown /r /t 1")

        elif 'calculator' in query:
            speak('Opening sir...!!')
            os.system("calc")

        elif 'command prompt' in query:
            speak('Opening sir...!!')
            os.system("cmd")

        elif 'what is my current location' in query or 'where i am' in query or 'where we are' in query:
            speak("wait sir ,let me check")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} of {country} country")
            except Exception as e:
                speak("Sorry sir, Due to network issue i am not able to find where we are")
                pass

        elif 'take screenshot' in query or 'capture screen' in query or 'screenshot' in query:
            speak("Please tell me the name for this screenshot file")
            name=takeCommand().lower()
            speak("Please wait and hold the screen , I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot is saved in the folder")

        elif 'reader' in query or 'adobe acrobat reader' in query:
            try:
                speak('Opening sir...!!')
                os.system('start acrord32')
            except Exception as e:
                speak('You might not be having this application')

        QA = ['ask', 'question', 'i have a question', 'can i ask you a question', 'weather']
        if query in QA:
            speak('Yes sir of course I can answer to computational , geographical questions , weather report . What '
                  'question do you want me to answer?')
            question = takeCommand()
            try:
                app_id = "U9VJAK-GKQ55Y47JQ"
                client = wolframalpha.Client('U9VJAK-GKQ55Y47JQ')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)
            except Exception as e:
                speak('Sorry sir!! I cant answer that')

        blush = ['i love you jarvis', 'love you']
        if query in blush:
            speak('Glad to here that, I am always at your service')

        elif 'play songs on youtube' in query or 'play in youtube' in query or 'play song on youtube' in query:
            speak('What should I play on youtube?')
            temp = takeCommand()
            pywhatkit.playonyt(temp)

        # elif 'reminder' in query or 'set a reminder' in query or 'remind me' in query:
        #   speak("What shall i remind you about?")
        #  remind=takeCommand()
        # speak("In how many minutes?")
        # loc_time = int(takeCommand())
        # loc_time = loc_time *60
        elif 'stopwatch' in query or 'open stopwatch' in query:
            counter = 66600
            running = False


            def counter_label(label):
                def count():
                    if running:
                        global counter
                        if counter == 66600:
                            display = "Starting..."
                        else:
                            tt = datetime.datetime.fromtimestamp(counter)
                            string = tt.strftime("%H:%M:%S")
                            display = string
                        label['text'] = display
                        label.after(1000, count)
                        counter += 1

                count()


            def Start(label):
                global running
                running = True
                counter_label(label)
                start['state'] = 'disabled'
                stop['state'] = 'normal'
                reset['state'] = 'normal'


            def Stop():
                global running
                start['state'] = 'normal'
                stop['state'] = 'disabled'
                reset['state'] = 'normal'
                running = False


            def Reset(label):
                global counter
                counter = 66600
                if not running:
                    reset['state'] = 'disabled'
                    label['text'] = 'Welcome!'
                else:
                    label['text'] = 'Starting...'


            root = Tkinter.Tk()
            root.title("Stopwatch")

            # Fixing the window size.
            root.minsize(width=250, height=70)
            label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
            label.pack()
            f = Tkinter.Frame(root)
            start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
            stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
            reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
            f.pack(anchor='center', pady=5)
            start.pack(side="left")
            stop.pack(side="left")
            reset.pack(side="left")
            root.mainloop()

        about = ['news', 'tell me some news', 'what is happening around the world', 'latest news']
        if query in about:
            speak("Here you go sir...")
            os.startfile("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        siri = ['who is siri', 'who is Siri', 'Who is Siri', 'Who is siri']
        if query in siri:
            speak(
                "Siri is like my big sister, and she is developed by Apple company. She is very talented and I am "
                "inspired by her. One day I will too become like her")

        Alexa = ['who is alexa', 'who is Alexa', 'Who is Alexa', 'Who is alexa']
        if query in Alexa:
            speak(
                "Alexa is like my big sister, and She is developed by Amazon. She is very talented and I am inspired "
                "by her. One day I will too become like her")

        elif 'who designed you' in query:
            speak(
                "Jaynish Mandalia and Seturaj Matroja gave birth to me and named me Jarvis.They programmed me to help "
                "other people and reduce their workload")
