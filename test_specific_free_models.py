import requests

api_key = "YOUR_OPENCODE_ZEN_APIKEY"

def test_models(model_list):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    url = "https://opencode.ai/zen/v1/chat/completions"
    
    for model in model_list:
        print(f"--- Testing {model} ---")
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Say 'Active'"}],
            "max_tokens": 10
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        print()

requested_models = [
    "big-pickle",
    "hy3-free",
    "north-mini-code-free",
    "nemotron-3-ultra-free",
    "deepseek-v4-flash-free",
    "mimo-v2.5-free"
]

test_models(requested_models)
