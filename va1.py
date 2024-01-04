#importing the libraries
import speech_recognition as sr
import pyttsx3
import datetime
import os 
import webbrowser
import pyjokes

engine=pyttsx3.init()  #initializing the text to speech engine
voices=engine.getProperty('voices')  #get the available voices
r=sr.Recognizer() #initializing the recognizer class for recognizing the speech

def greet():
    now=datetime.datetime.now() #importing the datetime package for getting the current date and time
    hour=int(now.hour) #extracting the hour from entire date and time
    if (hour>0 and hour<12):
        engine.say("Good Morning ma'am") #converts the text to speech
        engine.runAndWait() #makes the speech audible in the system, if this command is not written then the speech will not be audible
    elif(hour>=12 and hour<16):
        engine.say("Good Afternoon ma'am")
        engine.runAndWait()
    else:
        engine.say("Good evening ma'am") 
        engine.runAndWait()

def introduction(): #function to greet the user
    engine.say("What should i call you ma'am?")
    engine.runAndWait()
    user= asking()
    engine.say("Welcome Miss")
    engine.runAndWait()
    engine.say(user)
    engine.runAndWait()
    print("WELCOME MISS ")
    print(user)
    engine.say("How can i Help you, Ma'am?")
    engine.runAndWait()

def asking(): #function to ask for commands
    with sr.Microphone() as source:
        print("Please wait...")
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Listening...")
        audio=r.listen(source)
    try:
        recorded = r.recognize_google(audio)
        recorded=recorded.lower() 
        print(recorded)
    except sr.RequestError as e:
        print("Could not request results",e)
        return 'none'
    except sr.UnknownValueError:
        print("Unknown error occured")
        return 'none'
    except Exception as e1:
        print("Voice could not be recognized...")
        print(e1)
        return 'none'
    return recorded
    

if __name__ == '__main__': #main function
    #clearing the screen before the assistant starts
    os.system('cls||clear')
    name =("Charlie") #setting the name of the assisstant
    greet()
    engine.say("Hello, I am your Assistant")
    engine.say(name)
    introduction()
    while(1): #various commands for performing various functions as per user instruction
        recorded=asking()
        if 'time' in recorded:
            now=datetime.datetime.now()
            print(now)
            engine.say(now)
            engine.runAndWait()
        elif 'youtube' in recorded:
            a='opening youtube...'
            engine.say(a)
            engine.runAndWait()
            webbrowser.open('www.youtube.com')
        elif 'chrome'in recorded:
            a='Opening chrome...'
            engine.say(a)
            engine.runAndWait()
            a1="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(a1)
        elif 'play' in recorded:
            a='Playing for you...'
            print(a)
            engine.say(a)
            engine.runAndWait()
            webbrowser.open(recorded)
        elif 'joke' in recorded:
            a=pyjokes.get_joke()
            engine.say(a)
            engine.runAndWait()
        elif 'exit' in recorded:
            a="Thank you for your time!"
            print(a)
            engine.say(a)
            engine.runAndWait()
            break
        elif 'how are you' in recorded:
            a="I'm fine. Thank you for asking."
            b= "How are you?"
            print(a)
            engine.say(a)
            engine.runAndWait()	
            print(b)
            engine.say(b)
            engine.runAndWait()
        elif 'powerpoint presentation' in recorded:
            engine.say("opening Power Point presentation")
            a = r"C:\\Users\\Adyatoni\\OneDrive\\Documents\\Activate milestone.pptx"
            os.startfile(a)
