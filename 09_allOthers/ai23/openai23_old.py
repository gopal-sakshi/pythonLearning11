# python3 -m pip install openai
# export apikey24=<pat2>
import openai 
import os
openai.my_api_key = os.environ["apikey24"]


messages = [ {"role": "system", "content":"You are a intelligent assistant."} ]
messages.append({"role": "user", "content": "Who won 2010 football worldcup"})
chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
answer = chat.choices[0].message.content
print("answer ====> ", answer)
print("whole object ===> ", chat.choices[0])
# messages.append({"role": "assistant", "content": answer})


# openai.ChatCompletion ===>  no longer supported in openai>=1.0.0
# https://github.com/openai/openai-python/discussions/742