import json
import os

import ollama

MODEL_NAME = "qwen3.5:4b"
IMAGES_JSON = "public\\images.json"
PROMPT = """
Write a concise alt text for this image
to assist visually impaired users.
Keep it under 150 characters.
Do not start with 'An image of' or 'A picture of'.
Do not speculate, state facts.
Just describe the subject and context.
Your output must be one or two sentences in plain english.
"""

with open(IMAGES_JSON) as f:
    global imgjson
    imgjson = json.load(f)

for img in imgjson:
    if img["alt"] == "":
        filepath = os.path.join("images", img["dir"], img["original"])

        print(f"Analizing {filepath}...")

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": PROMPT,
                    "images": [filepath],
                }
            ],
        )

        generatedText = response["message"]["content"].strip()

        print("Generated text:\n" + generatedText)
        print()

        img["alt"] = generatedText

        with open(IMAGES_JSON, mode="w") as f:
            json.dump(imgjson, f, indent=4)
