import pyttsx3
from colorama import Fore

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", 160)


def speak(text):
    print(Fore.LIGHTYELLOW_EX, f"Vaniska : {text}")
    engine.say(text)
    engine.runAndWait()
    print(Fore.RESET)