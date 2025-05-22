import requests
import json
from openai import OpenAI

def LLM_response(content, model):
    if model in ("DeepSeek-V3", "DeepSeek-R1"):
        if model == "DeepSeek-V3":
            max_token = 8192
            model = "deepseek-chat"
        else:
            max_token = 8192
            model = "deepseek-reasoner"

        client = OpenAI(api_key="", base_url="")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model=model,
            max_tokens= max_token,
            temperature=0.3,
        )
        return chat_completion.choices[0].message.content
    
    elif model in ("llama"):
        url = f"http://localhost:8000/v1/chat/completions" 
        messages = [ {'role': 'user', 'content': content} ] 
        request_data = { 
            "model": "meta-llama/Meta-Llama-3-8B-Instruct", 
            "messages": messages, 
            "stream": False, 
            # "temperature": 0.3, 
            "max_tokens": 8192,
        } 
        response = requests.post(url, json=request_data) 
        if response.status_code == 200: 
            try:
                ans = json.loads(response.text)["choices"][0]['message']['content'] 
            except Exception as e:
                print(e)
                print(response.json()['msg'])
                ans = ''
        return ans
    else:
        client = OpenAI(
            base_url='',
            api_key='',
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model=model, 
            temperature=0.2,
        )
        return chat_completion.choices[0].message.content