import speech_recognition as sr


def listen() -> str:
    with sr.Microphone() as source:
        try:
            r = sr.Recognizer()
            print("Say something!")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 8)
            print("Processing..")
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(
                    e
                )
            )


def take_input():
    text = input("Say something: ").lower()
    return text


if __name__ == "__main__":
    listen()
