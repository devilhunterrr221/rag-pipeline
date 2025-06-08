import openai
from PyPDF2 import PdfReader
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text(file_bytes):
    reader = PdfReader(file_bytes)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def query_llm(context, question):
    prompt = f"Use the following context to answer:\n\n{''.join(context)}\n\nQ: {question}\nA:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']