# 🖼️ Batch Image Generator with OpenAI API
Just drop instruction files into the `image_prompts/` folder, then run a single command to generate multiple images at once.
Instructions can be written in structured JSON or plain text. **gpt-4o-mini** will automatically convert free-form text into a valid image prompt when needed.

### 🛠️ Lazy Mode: Generate Images from Plain Text Instructions
```
python generate.py
```

💡 Sample plain text instruction:
```

Split‑screen illustration: left side shows a visitor asking a question (‘What’s this painting?’) into a headset; right side shows an AI waveform traveling through LiveKit nodes to return an instant speech bubble answer (‘It’s by Monet, 1875’).
Futuristic infographic vibe, cyan‑purple accent colors, light grid background, Landscape 1536x1024.

n=2
size=1536x1024

```

🔁 Internally converted to JSON:
```
{
  "prompt": "Split‑screen illustration: left side shows a visitor asking a question (‘What’s this painting?’) into a headset; right side shows an AI waveform traveling through LiveKit nodes to return an instant speech bubble answer (‘It’s by Monet, 1875’). Futuristic infographic vibe, cyan‑purple accent colors, light grid background.",
  "n": 2,
  "size": "1536x1024"
}
```

### 🔒 Strict Mode: Generate Images from Structured JSON Instructions
```
python strict.py
```
Use this mode when your prompts are already structured correctly as `.json` files.


### Single Instruction Mode:
```
python generate.py sample.txt

python generate.py sample.json

python strict.py sample.json
``` 

## 🔧 Features
- 🛠 **Lazy Mode**

  Skip the hassle of editing JSON. Just write plain text prompts—even with missing commas, quotes, or extra line breaks. The script uses gpt-4o-mini to convert your text into structured JSON automatically.

- 🖼 **Multiple Image Generation**

  Specify how many images to generate per instruction file using the `n` parameter.

- 📂 **Batch Processing**

  Drop multiple instruction files into the `image_prompts/` folder. The script processes all of them in one run.

- 💡 **More Efficient** than ChatGPT for Image Generation
    - No need to manually download images one by one
    - Prompt metadata is saved next to each image
    - You can set up 10+ prompts and run them all at once. Go grab a coffee ☕ while it runs!

## 📦 Requirements
- **python 3.12**

  Recommended: use `pyenv` to manage your Python version.

- **OpenAI API Key**

  You’ll need a valid OpenAI API key from platform.openai.com.
  (Note: This is separate from a ChatGPT Plus subscription.)

## 🛠️ Setup
> ✅ Recommended: Use Python 3.12+ with pyenv to avoid version issues.

### Confirm Python version
```
python --version
# Expected: Python 3.12.x
```
If your version is lower or missing, install it with pyenv:
```
brew install pyenv
pyenv install 3.12
pyenv global 3.12
```

### 1. Clone and enter the project
```
git clone https://github.com/markmatsushima/image_gen.git
cd image_gen
```
### 2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Set up your OpenAI API key
The script will prompt you on first run and store the key in `.env.local`.

### 5. Generate Images from Plain Text Instructions
```
python generate.py
```

## 📄 License
MIT License




