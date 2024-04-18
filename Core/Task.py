from Core.Main import *


def main_task_executor(query):
    query = str(query).strip()
    if len(query) <= 0:
        print("Invalid input")
        pass
    else:
        print("Processing your request")


main_task_executor(input("enter : "))
