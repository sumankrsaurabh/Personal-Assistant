from dotenv import load_dotenv
from Body.OfflineListner import take_input
from Body.Speak import speak
from Features.Gemini import get_response

load_dotenv()


def Vaniska():
    while True:
        input_text = take_input()
        output = get_response(input_text)
        speak(output)


Vaniska()
