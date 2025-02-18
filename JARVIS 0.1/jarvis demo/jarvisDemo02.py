import operator
import sys
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import cv2
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,sir...!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir...!")

    else:
        speak("Good Evening,sir...!")

    speak("Ready to comply sir ,how can i help you ?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogning...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("i am having difficulty hearing you , Can you please speakup or i dont have any information about that ....")
        speak("i am having difficulty hearing you , Can you please speakup or i dont have any information about that ....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("yes sir,i am at your service , what can i do for you..?")
            speak("yes sir,i am at your service , what can i do for you..?") 

        elif "who are you" in query:
            print('hi ,My name is jarvis')
            speak('hi ,My Name is jarvis')
            print('i am  your voice assistant,i can do Everything that my creator functioned me to do')
            speak('i am  your voice assistant,i can do Everything that my creator functioned me to do')

        elif "who created you" in query:
            print('created by SDR, he created with python language, in Visual Studio Code')
            speak('created by SDR, he created with python language, in Visual Studio Code')  

        elif 'what is' in query:
            speak('Searching wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('google.com')    
