import pyttsx3
import requests

# -----------------------------
# Voice setup
# -----------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 180)   # speaking speed
engine.setProperty('volume', 1.0)

# -----------------------------
# API endpoint
# -----------------------------
API_URL = "http://127.0.0.1:5000/ask"

# -----------------------------
# Optional conversation history
# -----------------------------
conversation_history = []

print("✅ Simon is ready! Type 'quit' to exit. He will respond via voice.")

while True:
    prompt = input("You: ").strip()
    if prompt.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    # Send prompt to backend
    response = requests.post(API_URL, json={"prompt": prompt}).json()
    text = response.get("reply", "")

    # Remove unwanted tokens
    text = text.replace("<|im_end|>", "").strip()

    # Print and speak
    print("Simon:", text)
    engine.say(text)
    engine.runAndWait()

    # Store in history
    conversation_history.append({"user": prompt, "assistant": text})
