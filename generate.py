import sys
from pathlib import Path
from typing import Literal, Optional
from pydantic import BaseModel
from config import client, PROMPT_DIR
from strict import generate_and_save_images

VALID_EXTENSIONS = {".txt", ".text", ".json"}

class ImagePrompt(BaseModel):
    prompt: str
    n: int = 1
    size: Optional[Literal[
        "1024x1024", "1024x1792", "1792x1024", "1536x1024", "1024x1536", "auto"
    ]] = "auto"

SYSTEM_MESSAGE = """
You will be given a free-form text that describes what kind of images the user wants to generate with the OpenAI DALL·E model.
Return a structured JSON object with the following fields: prompt, n, and size.
"""

def parse_text_to_prompt(text: str) -> ImagePrompt:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": text.strip()}
        ],
        response_format=ImagePrompt,
    )
    return completion.choices[0].message.parsed

def main():
    args = sys.argv[1:]
    targets = [PROMPT_DIR / args[0]] if args else sorted(PROMPT_DIR.glob("*"))

    for file in targets:
        if not file.is_file() or file.suffix.lower() not in VALID_EXTENSIONS:
            continue
        try:
            print(f"✨ Parsing and generating from: {file.name}")
            text = file.read_text(encoding="utf-8")
            parsed = parse_text_to_prompt(text)
            generate_and_save_images(parsed.model_dump(), base_name=file.stem)
        except Exception as e:
            print(f"❌ Error processing {file.name}: {e}")

if __name__ == "__main__":
    main()
