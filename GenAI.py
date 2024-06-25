import pathlib
import textwrap


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
 
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY='AIzaSyDMvt_t1erXrTBCPDhMrx9jiA_q8YNw4ZY'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

