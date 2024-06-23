import re
import sqlite3
import webbrowser
import pyttsx3
from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak
import pywhatkit as kit
from engine.db import *


conn = sqlite3.connect("jarvis2.db")
cursor = conn.cursor()

# playing assistant sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assests\\audio\\audio.mp3"
    playsound(music_dir)



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command3 WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM web_command4 WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
# playing on Youtube
def PlayYoutube(query):
    search_item = extract_yt_term(query)
    speak("Playing" + search_item + "on YouTube")
    kit.playonyt(search_item)

def extract_yt_term(command):
    # Defining a regular expression
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match   = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None