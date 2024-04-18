import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai


GOOGLE_API_KEY = os.getenv("GEMINI_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def get_response(text: str) -> str:
    response = model.generate_content(text)
    return response.text