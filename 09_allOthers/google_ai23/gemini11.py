# python3 -m pip install -q -U google-generativeai

import google.generativeai as genai
import os

genai.configure(api_key=os.environ["apikey23"])
model = genai.GenerativeModel('gemini-pro')
response23 = model.generate_content("Write a story about a magic backpack.")
# response24 = model.generate_content("What is the meaning of life?")
print('response23 =========> ', response23.text)
# print('response23 =========> ', response24.text)

# export apikey23=<pat2>