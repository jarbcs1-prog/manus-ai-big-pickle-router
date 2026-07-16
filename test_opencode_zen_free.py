import requests

api_key = "sk-X4uxdpzuIWYAAm3kaOQyKxMgupNaPmk19iBrJZ8KVI9sJYAx4HcvbbV7QSMoC3SU"

def test_free_model():
    print("Testing Code Supernova (Free model)...")
    url = "https://opencode.ai/zen/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "code-supernova",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 50
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(response.text)

test_free_model()
