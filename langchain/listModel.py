import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

for model in genai.list_models():
    print(f"Model: {model.name}")
    print(f"  Description: {model.description}")
    print(f"  Supported generation methods: {model.supported_generation_methods}")
    print("-" * 20)

