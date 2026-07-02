from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)
CORS(app)

# Load BlenderBot model
model_name = "facebook/blenderbot-400M-distill"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

conversation_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():

    data = request.get_json()

    if not data or "prompt" not in data:
        return "No prompt received", 400

    user_input = data["prompt"]

    # Keep only the last 6 messages
    history = conversation_history[-6:]

    if history:
        context = "\n".join(history) + "\n" + user_input
    else:
        context = user_input

    # Tokenize
    inputs = tokenizer(
        context,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id,
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Save conversation
    conversation_history.append(user_input)
    conversation_history.append(response)

    return response


if __name__ == "__main__":
    app.run(debug=True)