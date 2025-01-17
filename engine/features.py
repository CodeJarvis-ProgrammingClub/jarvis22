from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME

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
        speak()