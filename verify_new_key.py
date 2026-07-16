import requests

api_key = "sk-2gRgOHCb7rVBHhykaqyp8WMIcR9QzViRoGUGvzHewXKCA2yccQzg5KCSQ5YYJyQA"

def test_endpoint(name, url, model, payload_type="openai"):
    print(f"--- Testing {name} ({model}) ---")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    if payload_type == "openai":
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Say hello!"}],
            "max_tokens": 20
        }
    elif payload_type == "anthropic":
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Say hello!"}],
            "max_tokens": 20
        }
    else:
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Say hello!"}],
            "max_tokens": 20
        }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    print()

# Test various documented endpoints
test_endpoint("GPT 5", "https://opencode.ai/zen/v1/responses", "gpt-5")
test_endpoint("Claude Sonnet 4", "https://opencode.ai/zen/v1/messages", "claude-sonnet-4", payload_type="anthropic")
test_endpoint("Qwen3 Coder", "https://opencode.ai/zen/v1/chat/completions", "qwen3-coder")
