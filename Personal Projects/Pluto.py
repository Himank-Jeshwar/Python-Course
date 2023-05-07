import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import smtplib
robot = pyttsx3.init()
mic = sr.Recognizer()
def speak(msg):
    robot.say(msg)
    robot.runAndWait()
def e_mail(senderId,receiver_mailId):
    server = smtplib.STMP("stmp@gmail.com")
    server.ehlo()
name=input("Enter Your Name = ")
if int(datetime.datetime.now().hour)>=12 and int(datetime.datetime.now().hour)<16:
    print(f"Good Afternoon {name}, how may I help you ?")
    speak(f"Good Afternoon {name}, how may I help you ?")
elif int(datetime.datetime.now().hour)<12:
    print(f"Good Morning {name}, how may I help you ?")
    speak(f"Good Morning {name}, how may I help you ?")
elif int(datetime.datetime.now().hour)>=16:
    print(f"Good Evening {name}, how may I help you ?")
    speak(f"Good Evening {name}, how may I help you ?")
with sr.Microphone() as audio:
    print("Listening...")
    userVoice=mic.listen(audio)
    try:
        speech=mic.recognize_google(userVoice)
        speech=speech.lower()
        if "hello" in speech:
            print(f"Yes {name} I am there to help you.")
            speak(f"Yes {name} I am there to help you.") 
        elif "youtube" in speech:
            print("Opening Youtube...")
            speak("Opening Youtube")
            webbrowser.open("https://youtube.com")
            # webbrowser.search 
        elif "python documentation" in speech or "python docs" in speech:
            print("Opening Python docs...")
            speak("Opening Python docs...")  
            webbrowser.open("https://python.org/docs")  
        elif "open google" in speech :
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("https://google.com")
        
    except:
        print("Couldn't recognize your voice. Can you repeat that again")
        robot.say("Couldn't recognize your voice. Can you repeat that again")
        robot.runAndWait()