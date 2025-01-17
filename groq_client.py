import requests
import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
Headers={"Authorization": f"Bearer {api_key}"}

def generate_groq_content(prompt="Generate a motivational quote"):
    try:
        response = requests.post(
            url,
            headers=Headers,
            json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "max_tokens": 100}
        )
        response.raise_for_status()
        logger.info("Content generated successfully using Groq API.")
        return response.json().get("choices")[0]['message']['content']
    except Exception as e:
        logger.error(f"Error fetching content from Groq API: {e}")
        raise
    

def generate_comment(prompt="Generate a positive comment for a Reddit post."):
    try:    
        response = requests.post(
            url,
            headers=Headers,
            json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "max_tokens": 50}
        )
        response.raise_for_status()
        logger.info("Comment generated successfully.")
        return response.json().get("choices")[0]['message']['content']
    except Exception as e:
        logger.error(f"Error fetching Comment content from Groq API: {e}")
        raise