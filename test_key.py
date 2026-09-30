import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key:
    print("Key loaded successfully!")
    print("Key starts with:", api_key[:15])
else:
    print("Key not found. Check your .env file.")