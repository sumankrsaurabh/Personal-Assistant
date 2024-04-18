# Importing
import dotenv
import openai
from dotenv.main import load_dotenv

# API Key
fileopen = open("data\\api.txt", "r")
API = fileopen.read()
fileopen.close()

# Coading
openai.api_key = API
load_dotenv()
completion = openai.Completion()


def QuestionAnswer(question, chat_log=None):
    Filelog = open("DataBase\\qna_log.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    promt = f'{chat_log}Question : {question}\n Answer : '
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=promt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + \
                               f"\nQuestion : {question} \nAnswer : {answer}"
    Filelog = open("DataBase\\qna_log.txt", "w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer
