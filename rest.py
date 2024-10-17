import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.getenv("NV_API_KEY"))}
query = "How many R's are there in the word 'strawberry'?."
data = {"messages": [{"role": "user", "content": query}], "model": "nvidia/llama-3.1-nemotron-70b-instruct"}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(response.reason)