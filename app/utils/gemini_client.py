# app/utils/gemini_client.py
import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    logging.error("GOOGLE_API_KEY not found in .env")
    raise ValueError("GOOGLE_API_KEY missing")

genai.configure(api_key=API_KEY)

# Note: Ensure you are using a valid model name
DEFAULT_MODEL = "models/gemini-2.5-flash" 

def call_gemini(prompt: str, model: str = DEFAULT_MODEL, **kwargs) -> str:
    """
    Calls Gemini. Accepts extra arguments like max_output_tokens or temperature
    and passes them as generation_config.
    """
    try:
        # Use the standard GenerativeModel class approach
        generative_model = genai.GenerativeModel(model)
        
        # 'kwargs' captures arguments like max_output_tokens=100 and passes them here
        response = generative_model.generate_content(
            prompt,
            generation_config=kwargs 
        )
        return response.text
    except Exception as e:
        logging.exception("Gemini call failed")
        raise