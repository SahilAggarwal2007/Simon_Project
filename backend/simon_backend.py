import os
import pyttsx3
from gpt4all import GPT4All
import requests

# Voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# Where the model will be stored in your Render instance
model_dir = os.path.join(os.getcwd(), "models")
os.makedirs(model_dir, exist_ok=True)

local_model_file = os.path.join(model_dir, "mpt-7b-chat.gguf4.Q4_0.gguf")

# URL to the MPT model (hosted publicly, e.g., Hugging Face or your own server)
MODEL_URL = "https://huggingface.co/your-username/mpt-7b-chat/resolve/main/mpt-7b-chat.gguf4.Q4_0.gguf"

# Download the model if it doesn't exist
if not os.path.isfile(local_model_file):
    print("Model not found locally. Downloading...")
    response = requests.get(MODEL_URL, stream=True)
    with open(local_model_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Download complete.")

# Load GPT4All model
model = GPT4All(model_name=local_model_file, allow_download=False)

print("✅ Simon is ready! Type 'quit' to exit. He will respond via voice.")

conversation_history = []

while True:
    prompt = input("You: ").strip()
    if prompt.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    concise_prompt = f"{prompt}\n\nPlease answer concisely in 1-2 sentences."
    response = model.generate(concise_prompt, max_tokens=200)
    output = "".join(response) if isinstance(response, list) else response
    output = output.strip()

    print("Simon:", output)
    engine.say(output)
    engine.runAndWait()

    conversation_history.append({"user": prompt, "assistant": output})
