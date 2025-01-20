import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

#Playing assistant sound function
@eel.expose
def playAssistantSound():
    mymusic="www\\assets\\audio\\start_sound.mp3"
    playsound(mymusic)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak('not found')     

def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+" on youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None  