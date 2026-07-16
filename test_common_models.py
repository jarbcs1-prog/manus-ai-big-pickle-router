import requests

api_key = "sk-2gRgOHCb7rVBHhykaqyp8WMIcR9QzViRoGUGvzHewXKCA2yccQzg5KCSQ5YYJyQA"

def test_common_models():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Trying standard OpenAI-compatible endpoint with common model IDs
    url = "https://opencode.ai/zen/v1/chat/completions"
    models = ["gpt-4o", "claude-3-5-sonnet", "meta-llama/llama-3.1-405b-instruct"]
    
    for model in models:
        print(f"Testing {model}...")
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Hi"}],
            "max_tokens": 10
        }
        response = requests.post(url, headers=headers, json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}\n")

test_common_models()
