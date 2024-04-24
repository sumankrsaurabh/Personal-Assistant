import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import google.generativeai as genai

load_dotenv()
console = Console()
GOOGLE_API_KEY = os.getenv("GEMINI_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def get_response(text: str) -> str:
    response = model.generate_content(text)
    markdown = Markdown(response.text)
    console.print(markdown)
    description = bytes(response.text, "utf-8")
    return description.decode("utf-8")
