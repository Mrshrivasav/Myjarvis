import os
import requests
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(question, history=None):
    # Check if API key is available and valid
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "I'm sorry, but I need a valid Gemini API key to provide AI responses. Please set up your API key in the .env file."
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": question}]}
        ]
    }
    if history:
        # Optionally add conversation history for context
        data["contents"].extend([{"parts": [{"text": h}]} for h in history])

    params = {"key": GEMINI_API_KEY}
    response = requests.post(url, headers=headers, params=params, json=data)
    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Sorry, I couldn't understand the response from Gemini."
    else:
        return f"Error: {response.status_code} - {response.text}" 