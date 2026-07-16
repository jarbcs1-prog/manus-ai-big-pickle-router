# Big-Pickle Router Configuration Guide

This package enables automatic task delegation to the **OpenCode Zen `big-pickle` model** once a daily limit of **1,300 tokens** is reached.

## Files in this Package

1.  **`token_monitor.py`**: Tracks your cumulative token usage and triggers the handoff.
2.  **`big_pickle_agent.py`**: The API client that communicates with OpenCode Zen.
3.  **`delegate_manager.py`**: Saves the current task state to ensure a seamless transition.
4.  **`verify_new_key.py`**: A utility to test your API key and model access.

## Setup Instructions

### 1. Installation
Place all files in a dedicated directory (e.g., `/home/ubuntu/big-pickle-router/`).

### 2. Configure API Key
The `big_pickle_agent.py` is pre-configured with your key. If you need to update it, edit the `API_KEY` variable at the top of the script.

### 3. Monitoring Usage
To track usage, the system calls `token_monitor.py` after each task:
```bash
python3 token_monitor.py <tokens_used>
```
Once the `total_tokens` in `daily_usage.json` hits **1,300**, the script will signal for delegation.

### 4. Daily Reset
To start a fresh day, delete the usage log:
```bash
rm /home/ubuntu/daily_usage.json
```

## How Delegation Works
When the limit is reached:
1.  `delegate_manager.py` creates `task_context.json`.
2.  `big_pickle_agent.py` is launched using that context.
3.  The `big-pickle` model provides the final reasoning and response.
