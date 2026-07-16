import json
import os

# Configuration for Daily Token Limit
LIMIT = 1300
USAGE_FILE = "daily_usage.json"

def check_and_delegate(current_request_tokens):
    """
    Tracks token usage and returns True if the 1300 limit is reached.
    """
    # 1. Load current usage
    if os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, 'r') as f:
            try:
                usage = json.load(f)
            except json.JSONDecodeError:
                usage = {"total_tokens": 0}
    else:
        usage = {"total_tokens": 0}

    # 2. Update usage
    usage["total_tokens"] += current_request_tokens
    
    with open(USAGE_FILE, 'w') as f:
        json.dump(usage, f, indent=2)

    # 3. Check against limit
    if usage["total_tokens"] >= LIMIT:
        print(f"⚠️ DAILY LIMIT REACHED: {usage['total_tokens']}/{LIMIT} tokens.")
        return True
    
    print(f"Token Usage: {usage['total_tokens']}/{LIMIT}")
    return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tokens = int(sys.argv[1])
        reached = check_and_delegate(tokens)
        if reached:
            print("Action: Triggering Zen-Delegator...")
    else:
        print("Usage: python3 token_monitor.py <tokens_used_in_last_call>")
