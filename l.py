# list_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

print("\n=== AVAILABLE MODELS ===")
for m in models:
    supports = getattr(m, "supported_generation_methods", [])
    print(f"\nModel: {m.name}")
    print(f"Supported Methods: {supports}")
