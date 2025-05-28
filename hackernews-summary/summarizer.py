import os
import requests

def summarize_with_gemma3(content):
    """
    Calls local Gemma 3 LLM via llama.cpp OpenAI-compatible API.
    Only summarizes if content is present.
    """
    if not content or not content.strip():
        return "No content to summarize."

    api_host = os.getenv("MODEL_HOST", "http://localhost:12434")
    api_path_prefix = os.getenv("MODEL_PATH_PREFIX", "")
    api_url = f"{api_host}{api_path_prefix}/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "ai/gemma3:4B-Q4_K_M",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes articles. Do not ask for clarification or to perform any additional tasks after the summarization."},
            {"role": "user", "content": f"Summarize the following article:\n\n{content}"}
        ],
        "max_tokens": 512,
        "temperature": 0.7,
    }
    try:
        response = requests.post(api_url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error communicating with Gemma 3 API: {e}"
