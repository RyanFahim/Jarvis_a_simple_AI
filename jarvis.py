import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyaudio
import wikipedia
import os


#pip install speechRecognition -> for recogniging the voices/speech
#sapi5 is used to use  voices

engine = pyttsx3.init('sapi5') #sapi5 is used to use voices
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak(" Good Morning! ")
    elif hour>=12 and hour<17:
        speak(" Good afternoon! ")
    elif hour>=17 and hour<21:
        speak("Good Evening! ")
    else:
        speak(" Hello! ")

    speak("I am Jarvis. How may I help you? ")

def takeCommand():
    #takes command from the user and returns as string

    r = sr.Recognizer() #to recognize the audio
    with sr.Microphone() as source: 
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-bd")
        print(f"You said: {query} \n")

    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"

    return query



if __name__ == "__main__":

    

    wishMe()
    #speak("luch cha")

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            #query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2 )
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")

        elif 'code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'stop' in query:
            speak("Ok then. Have a lovely day!")
            break


        elif 'open music' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=music")


     
