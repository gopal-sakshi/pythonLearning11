########## OLD
# import openai, os
# openai.api_key = os.environ['apikey24']

# export apikey24=<pat2>


######### NEW
from openai import OpenAI, AsyncOpenAI
import os, json

client = OpenAI(organization='org-LIGpUK3EjQeBAALMWL3xvBo9', api_key=os.environ['apikey24'])
question23 = [{"role": "user", "content": "what is home ground of real madrid"}]
completion = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=question23,
)
print("answers ===> ", completion.model_dump_json(indent=2))
print("whole response23 ====> \n", completion)

# https://platform.openai.com/docs/guides/text-generation/chat-completions-api