from dotenv import load_dotenv
from Body.OfflineListner import take_input, listen
from Body.Speak import speak
from Features.GreetMe import greet_me
from main import Main
from config import Config

load_dotenv()

config = Config()
main = Main()


def Vaniska():
    speak(greet_me())
    while True:

        if config.input_method == "keyboard":
            input_text = take_input()
        else:
            input_text = listen()
        if (
            "change input method" in input_text
            or "use voice" in input_text
            or "use keyboard" in input_text
        ):
            config.change_input_method()
            speak("Selected " + config.input_method)
        else:
            output = main.main(query=input_text)
            speak(output)


if __name__ == "__main__":
    while True:
        print("Hi I am Vaniska. Please say special word to activate me")
        if "vaniska" in take_input():
            Vaniska()
        else:
            print("Please say Vaniska")
