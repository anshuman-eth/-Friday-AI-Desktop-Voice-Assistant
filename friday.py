import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import music
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("Hi my name is Friday. How may i help you.")
    

#takes microphone input from user and returns string output.
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__=='__main__':
    
    wishMe()
    while True:
        query=takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.......')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("OK! opening youtube in your browser")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("OK! opening google in your browser")
            webbrowser.open("https://google.com")

        elif 'play music' in query:
            speak("Okey Playing a song")
            webbrowser.open("https://music.youtube.com/watch?v=0p-YUiyWf-A&list=OLAK5uy_koFYb2Butc5XtA9h5dXAb6elXRRUedmVA")

        elif 'play song' in query:
            music_dir="C:\\Users\\anshu\\Videos\\Friday AI assistent\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            x=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir, songs[x]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%S:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open chrome' in query:
            path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'