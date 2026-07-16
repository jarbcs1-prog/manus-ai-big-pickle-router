import requests
import os

api_key = "sk-X4uxdpzuIWYAAm3kaOQyKxMgupNaPmk19iBrJZ8KVI9sJYAx4HcvbbV7QSMoC3SU"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# The documentation mentioned https://opencode.ai/zen/v1/chat/completions for OpenAI compatible models
# Let's try to hit the completions endpoint with a simple prompt using a free model mentioned in docs
# Grok Code Fast 1: grok-code

url = "https://opencode.ai/zen/v1/chat/completions"
data = {
    "model": "grok-code",
    "messages": [{"role": "user", "content": "Hello, are you active?"}],
    "max_tokens": 50
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Response:")
        print(response.json()['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
