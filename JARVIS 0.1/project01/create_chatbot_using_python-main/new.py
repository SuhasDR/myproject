import operator
import sys
import pyttsx3
import requests
import pyautogui
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

        if 'thank you' in query:
            print("Its my pleasure sir ,do you what anything sir...?")
            speak("Its my pleasure sir ,do you what anything sir...?")

        if 'nothing' in query:
            print("ok sir,when you need call ,i will be present...!")
            speak("ok sir,when you need call ,i will be present...!")        

        elif "hu r u" in query:
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
            speak("According to data")
            print(results)
            speak(results)

        elif 'when is' in query:
            speak('Searching wikipedia...')
            query = query.replace("when is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my data")
            print(results)
            speak(results)

        elif 'where' in query:
            speak('Searching wikipedia...')
            query = query.replace('where', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my data")
            print(results)
            speak(results)

        elif 'why' in query:
            speak('Searching wikipedia...')
            query = query.replace('why', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my data")
            print(results)
            speak(results)

        elif 'who' in query:
            speak('Searching wikipedia...')
            query = query.replace('who', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my data")
            print(results)
            speak(results)           
###############################################################################################################            

        elif 'just open google' in query:
            webbrowser.open('google.com')

        elif 'open google' in query:
            speak("what should I search for you ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif'search on youtube' in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?serach_query={query}")

        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")  

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe") 
###############################################################################################################                            

        elif "open notepad" in query:
            npath = "C:\Windows"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "shut down the system" in query:
            os.system("shutdown /r /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
##############################################################################################################

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name of the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "calculate" in query:
            r = sr.recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("listning...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    '×' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]  
            def eval_binary_expr(op1,oper,op2):
                op1,op2 = int(op1), int(op2) 
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))

        elif "my ip address" in query:
            speak("checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "volume" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "unmute" in query:
            pyautogui.press("volumeunmute")      
#############################################################################################            
        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "drag visual studio to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)

        elif "rectangular spiral" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.click()
            distance = 300
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "who are you" in query:
            print('My Name Is ')
            speak('My Name Is Six')
            print('I can Do Everything that my creator programmed me to do my work')
            speak('I can Do Everything that my creator programmed me to do my work')

        elif "who created you" in query:
            print('Created by SDR, I created with python language,in visual studio')
            speak('Created by SDR, I created with python language,in visual studio')

        elif"open notepad and write my name" in query:
            pyautogui.hotkey('win\notepad.exe')
            time.sleep(1)
            pyautogui.write('notepad')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write("HI SUHAS,HOW ARE YOU", internal = 0.1)

        elif "subscribe" in query:
            print("Everyone Who are watching This, Please subscribe Our Channel")
            speak("Everyone Who are watching This, Please subscribe Our Channel")


            