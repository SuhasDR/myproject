import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognzing sir...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say That Again Please...")
        speak("i didn't understand ,i dont have any data about that , sir")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if 'jarvis' in query:
            print("yes sir,i am at your service , what can i do for you..?")
            speak("yes sir,i am at your services, what can  i do for you...?")
        
