import requests

api_key = "sk-X4uxdpzuIWYAAm3kaOQyKxMgupNaPmk19iBrJZ8KVI9sJYAx4HcvbbV7QSMoC3SU"

# Based on docs:
# Claude Sonnet 4 -> https://opencode.ai/zen/v1/messages
# GPT 5 -> https://opencode.ai/zen/v1/responses

def test_claude():
    print("Testing Claude Sonnet 4...")
    url = "https://opencode.ai/zen/v1/messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "claude-sonnet-4",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 50
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(response.text)

def test_gpt():
    print("\nTesting GPT 5...")
    url = "https://opencode.ai/zen/v1/responses"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-5",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 50
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(response.text)

test_claude()
test_gpt()
