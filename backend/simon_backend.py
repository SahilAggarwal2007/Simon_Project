from flask import Flask, request, jsonify
import pyttsx3
from gpt4all import GPT4All

app = Flask(__name__)

# Voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# Model path (relative to backend folder)
local_model_file = "backend/mpt-7b-chat.gguf4.Q4_0.gguf"
model = GPT4All(model_name=local_model_file, allow_download=False)

@app.route("/ask", methods=["POST"])
def ask_simon():
    data = request.get_json()
    prompt = data.get("prompt", "")

    concise_prompt = f"{prompt}\n\nPlease answer concisely in 1-2 sentences."
    response = model.generate(concise_prompt, max_tokens=200)

    if isinstance(response, list):
        output = "".join(response)
    else:
        output = response

    output = output.strip()

    # Speak response
    engine.say(output)
    engine.runAndWait()

    return jsonify({"reply": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

