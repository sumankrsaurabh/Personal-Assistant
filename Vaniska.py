from dotenv import load_dotenv
from Body.OfflineListner import take_input,listen
from Body.Speak import speak
from Features.GreetMe import greet_me
from main import main

load_dotenv()


def Vaniska():
    speak(greet_me())
    while True:
        input_text = listen()
        output = main(input_text)
        speak(output)


if __name__ == "__main__":
    while True:
        print("Hi I am Vaniska. Please say special word to activate me")
        if "vaniska" in take_input():
            Vaniska()
        else:
            print("Please say Vaniska")
