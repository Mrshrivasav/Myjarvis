import os
import requests

# Set API key directly to avoid .env file issues
GROQ_API_KEY = "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"

def ask_groq(question, history=None):
    # Check if API key is available and valid
    if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
        return "I'm sorry, but I need a valid Groq API key to provide AI responses. Please set up your API key in the .env file."
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    
    # Prepare messages
    messages = []
    
    # Add conversation history if provided
    if history:
        for h in history:
            messages.append({"role": "user", "content": h})
    
    # Add current question
    messages.append({"role": "user", "content": question})
    
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            try:
                return response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                return f"Sorry, I couldn't understand the response from Groq. Error: {str(e)}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Network error: {str(e)}" 