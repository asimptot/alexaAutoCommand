import webbrowser as wb
import time
from gtts import gTTS
from datetime import datetime
import playsound

def search(data, name):
    speak("wait for a while " + name + " ,I will search for you.")
    wb.open(
        "https://www.google.co.in/?gfe_rd=cr&ei=V7DXWJuQNarT8gfb-42QBw&gws_rd=ssl#newwindow=1&safe=active&q=" + data + "&*")

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    time.sleep(10)
    # tts = gTTS(text=audioString, lang='en')
    # tts.save("audio.mp3")
    # os.system("audio.mp3")

def power_control():
    speak("Alexa! Turn Off " + device_name)
    speak("Alexa! Turn On " + device_name)

def channel_control():
    speak("Alexa! Change channel to three on " + device_name)
    speak("Alexa! Change channel to BBC One.")
    speak("Alexa! Next channel on " + device_name)
    speak("Alexa! Previous channel on " + device_name)

def volume_control():
    speak("Alexa! set volume to five on " + device_name)
    speak("Alexa! mute " + device_name)
    speak("Alexa! unmute " + device_name)
    speak("Alexa! volume down " + device_name)
    speak("Alexa! volume up " + device_name)

def input_control():
    speak("Alexa! Switch input to HDMI one on " + device_name)
    speak("Alexa! Switch input to TV on " + device_name)

def player_control():
    speak("Alexa! pause on " + device_name)
    speak("Alexa! resume on " + device_name)
    speak("Alexa! fast forward on " + device_name)
    speak("Alexa! rewind on " + device_name)
    speak("Alexa! stop on " + device_name)

def launcher_control():
    speak("Alexa! launch Youtube")
    speak("Alexa! launch Netflix")
    speak("Alexa! launch Prime Video")
    speak("Alexa! launch BBC News")
    speak("Alexa! launch ITV Hub")
    speak("Alexa! launch BBC iPlayer")
    speak("Alexa! launch All four")
    speak("Alexa! launch My5")
    speak("Alexa! launch CBS")
    speak("Alexa! launch UKTV")

def remote_video_player():
    speak("Alexa! play ‘Killing Eve’")
    speak("Alexa! show me ‘Doctor Who’")

def shortcut_control():
    speak("Alexa! go to What to Watch")
    speak("Alexa! go to Kids")
    speak("Alexa! go to Accessibility Settings")
    speak("Alexa! go to Guide Settings")
    speak("Alexa! go to Guide")
    speak("Alexa! go to Home")
    speak("Alexa! go to Info")
    speak("Alexa! go to Inputs")
    speak("Alexa! go to Parental Controls")
    speak("Alexa! go to Recordings")
    speak("Alexa! go to Scheduled Recordings")
    speak("Alexa! go to Settings")
    speak("Alexa! go to Timer Settings")
    speak("Alexa! go to Display Settings")
    speak("Alexa! go to TV Display Settings")
    speak("Alexa! go to Internet Settings")
    speak("Alexa! go to Network Settings")

device_name = input("Device Name'i girin:   ")

while (1):
    power_control()
    channel_control()
    volume_control()
    input_control()
    player_control()
    launcher_control()
    remote_video_player()
    shortcut_control()





