from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)
# CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})
CORS(app)


model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model(input_ids=inputs["input_ids"])
        logits = outputs.logits

    # Get the logits for the last token (most recent context)
    last_token_logits = logits[0, -1, :]

    # Apply softmax to get probabilities
    probabilites = torch.softmax(last_token_logits, dim=-1)

    top_k = 10
    top_k_probabilities, top_k_indices = torch.topk(probabilites, top_k)

    # Decode the token IDs into words
    suggestions = [
        {"word": tokenizer.decode([token_id]), "probability": prob.item()}
        for token_id, prob in zip(top_k_indices, top_k_probabilities)
    ]

    return jsonify({"suggestion": suggestions})


if __name__ == "__main__":
    app.run(port=5000)
