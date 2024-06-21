import pathlib
import textwrap


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY='AIzaSyDJRM59DAR5kixwq_di3t2F8KwNy_5jXDg'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is the meaning of enemy?")
print(response.text)
print(to_markdown(response.text))