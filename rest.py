import requests
import os

url = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("NV_API_KEY"))}
query = "Write a limerick about the wonders of GPU computing."
messages = [{"role": "user", "content": query}]
data = {"messages": messages, "model": "meta/llama3-70b-instruct"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])