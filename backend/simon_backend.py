from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

# Load model
local_model_file = r"C:\Users\sahil\Python_Projects\mpt-7b-chat.gguf4.Q4_0.gguf"
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

    return jsonify({"reply": output.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
