import sys
import json
import base64
from datetime import datetime
from pathlib import Path
from config import client, PROMPT_DIR, OUTPUT_DIR


def load_prompt(file_path):
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def generate_and_save_images(prompt_data, base_name="image"):
    model = "gpt-image-1"
    quality = "high"

    prompt = prompt_data.get("prompt")
    n = prompt_data.get("n", 1)
    size = prompt_data.get("size", "1024x1024")

    print(f"\U0001f3a8 Generating {n} image(s): {base_name} [{size}]")

    response = client.images.generate(
        model=model,
        prompt=prompt,
        n=n,
        size=size,
        quality=quality,
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for idx, image in enumerate(response.data):
        b64_image = image.b64_json
        if not b64_image:
            print(f"⚠️ Skipping image {idx}, no data.")
            continue
        image_bytes = base64.b64decode(b64_image)

        base_filename = f"{base_name}_{timestamp}_{idx}"
        image_path = OUTPUT_DIR / f"{base_filename}.png"
        prompt_path = OUTPUT_DIR / f"{base_filename}.json"

        image_path.write_bytes(image_bytes)

        # Save full prompt data including parameters
        full_metadata = {
            "model": model,
            "prompt": prompt,
            "n": n,
            "size": size,
            "quality": quality,
        }
        prompt_path.write_text(json.dumps(full_metadata, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"✅ Saved: {image_path} and {prompt_path}")



def main():
    args = sys.argv[1:]
    if args:
        file = PROMPT_DIR / args[0]
        if not file.exists():
            print(f"❌ File not found: {file.name}")
            sys.exit(1)
        data = load_prompt(file)
        generate_and_save_images(data, file.stem)
    else:
        for file in sorted(PROMPT_DIR.glob("*.json")):
            try:
                data = load_prompt(file)
                generate_and_save_images(data, file.stem)
            except Exception as e:
                print(f"⚠️ Failed to process {file.name}: {e}")


if __name__ == "__main__":
    main()
