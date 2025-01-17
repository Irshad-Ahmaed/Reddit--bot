import requests
import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()

def generate_groq_content(prompt="Generate a motivational quote"):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "max_tokens": 100}
    )
    
    if response.status_code == 200:
        # print(response.json().get("choices")[0]['message']['content'])
        logger.info("Content generated successfully using Groq API.")
        return response.json().get("choices")[0]['message']['content']
    else:
        logger.error(f"Failed to fetch content from Groq API. Status code: {response.status_code}") 
        print(f"Response: {response.text}")
        raise Exception("Failed to fetch content from Groq API.")
    

def generate_comment(prompt="Generate a positive comment for a Reddit post."):
    """Generates Groq AI content for comments."""
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "max_tokens": 50}
    )
    
    if response.status_code == 200:
        logger.info("Comment generated successfully.")
        return response.json().get("choices")[0]['message']['content']
    else:
        logger.error(f"Error generating Groq comment: {response.status_code}")
        raise Exception("Error generating comment.")