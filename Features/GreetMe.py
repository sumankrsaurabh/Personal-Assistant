import datetime


def greet_me() -> str:
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        return "Morning"
    elif 12 < hour <= 18:
        return "Afternoon"
    else:
        return "Evening"
