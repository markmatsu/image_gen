import os
from pathlib import Path
from getpass import getpass
from openai import OpenAI
from dotenv import load_dotenv

# Constants
PROMPT_DIR = Path("image_prompts")
OUTPUT_DIR = Path("images")
ENV_FILE = Path(".env.local")

# Load or ask for API key
if not ENV_FILE.exists():
    print("\U0001f511 Enter your OpenAI API key:")
    api_key = getpass("API Key: ").strip()
    ENV_FILE.write_text(f"OPENAI_API_KEY={api_key}\n")
else:
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
