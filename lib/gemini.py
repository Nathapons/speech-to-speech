import os
import json
import requests

from dotenv import load_dotenv
from google import genai


def get_prompting(text):
    load_dotenv()
    gemini_key = os.environ.get('GEMINI_API_KEY')
    if not gemini_key:
        raise Exception("Cannot get gemini key from .env file")
    
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-1.5-flash:generateContent?key={gemini_key}"
    )
    parts = [{"text": "อย่าพูดยาวมากครับ"}, {"text": text}]
    data = {"contents": [{"parts": parts}]}
    
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        response_json = response.json()
        text = response_json['candidates'][0]['content']['parts'][0]['text']
    else:
        text = 'ไม่ทราบว่าคุณต้องการพูดอะไรกับเราเหรอ'
        
    return text


def get_gemini_response_text(text):
    load_dotenv()
    gemini_key = os.environ.get('GEMINI_API_KEY')
    if not gemini_key:
        raise Exception("Cannot get gemini key from .env file")
    
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=text,
    )

    return response.text
