from flask import Flask, request, jsonify
import spacy
import os

app = Flask(__name__)

# Load the trained spaCy intent model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_model', 'model', 'nlu_model')
nlp = spacy.load(MODEL_PATH)

# Simple function to extract intent label and confidence
def get_intent(text):
    doc = nlp(text)
    if doc.cats:
        intent = max(doc.cats, key=doc.cats.get)
        confidence = round(float(doc.cats[intent]), 2)
        return intent, confidence
    return None, 0.0

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    intent, confidence = get_intent(text)

    return jsonify({
        'intent': intent,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
