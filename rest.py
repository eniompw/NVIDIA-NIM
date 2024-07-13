import requests
import os

# Define the URL for the POST request
url = "https://integrate.api.nvidia.com/v1/chat/completions"

# Create a dictionary for headers
headers = {
    "Content-Type": "application/json",  # Adjust content type as needed (e.g., application/xml)
    "Authorization": "Bearer " + str(os.environ.get("NV_API_KEY")),  # Your authorization token
}

q = "Write a limerick about the wonders of GPU computing."
# Prepare the data to be sent (can be JSON, string, etc.)
messages = [{"role": "user", "content": q}]
data = {
  "messages": messages, 
  "model": "meta/llama3-70b-instruct",
  "temperature": 0.5,   
  "top_p": 1,
  "max_tokens": 1024,
  "stream": False
  }

# Send the POST request with headers and data
response = requests.post(url, headers=headers, json=data)

# Check the response status code
if response.status_code == 200:
  # print("Success! Data posted.")
  # Access the response data (if any)
  response_data = response.json()
  print(response)
  print(response_data["choices"][0]["message"]["content"])
else:
  print("Error! Response code:", response.status_code)
  print(response.json())