import datetime


def greet_me() -> str:
    time = datetime.datetime.now()
    return (
        "Welcome back, sir"
        + " it is "
        + time.strftime("%H:%M")
        + ". and"
        + " today is "
        + time.strftime("%A")
    )