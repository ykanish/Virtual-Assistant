import pyttsx3
import speech_recognition as sr
import eel
import time
# Initialize Eel
eel.init('web')  # Point to the directory where your HTML/JS files are located

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 124)
    eel.DisplayMessage(text)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}")
        #eel.DisplayMessage(f"{query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        #speak(query)
    except Exception as e:
        eel.DisplayMessage("Sorry, I did not catch that")
        return ""

    return query.lower()

@eel.expose
def allCommands():
    query = take_command()
    print(query)
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)

    else:
        print("Not Run")

    eel.ShowHood()



