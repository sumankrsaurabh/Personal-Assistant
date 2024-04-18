import pywhatkit.ascii_art
import pywhatkit.core
import pywhatkit.mail
import pywhatkit.misc
import pywhatkit.remotekit
import pywhatkit.sc
import pywhatkit.whats
from Features.Gemini import get_response
import pywhatkit
import datetime

app_state = "active"


def main(query):
    query = query.lower()
    if len(query) > 0:
        if "play" in query or "youtube" in query or "yt" in query:
            query = query.replace("youtube", "")
            query = query.replace("yt", "")
            query = query.replace("on", "")
            pywhatkit.playonyt(query)

        elif "search" in query or "google" in query:
            query = query.replace("search", "")
            query = query.replace("on", "")
            query = query.replace("google", "")
            pywhatkit.search(query)

        elif "wikipedia" in query or "get info" in query:
            query = query.replace("wikipedia", "")
            query = query.replace("get info", "")
            query = query.replace("on", "")
            pywhatkit.info(query, lines=2)

        elif "screenshot" in query:
            pywhatkit.take_screenshot()
            return "Done"

        elif "shutdown my computer" in query:
            conf = input("Are you sure you want to shutdown your computer? (yes/no): ")
            if conf.lower() == "yes":
                pywhatkit.sc.shutdown()
            else:
                return "Ok, do not worry. I am still here!"

        elif "time" in query:
            now = datetime.datetime.now()
            return now.strftime("%H:%M")

        elif "date" in query:
            now = datetime.datetime.now()
            return now.strftime("%d-%m-%Y")

        elif "day" in query:
            now = datetime.datetime.now()
            return now.strftime("%A")

        elif "bye" in query or "goodbye" in query:
            app_state = "inactive"
            return get_response("Bye")

        else:
            return get_response(query)


if __name__ == "__main__":
    print(main("get info Sharukh khan"))
