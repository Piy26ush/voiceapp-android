import spacy
from spacy.util import minibatch, compounding
from spacy.training.example import Example
import random
import json
import os

# Load and format dataset
DATA_PATH = os.path.join("intent_model", "data", "dataset.json")
with open(DATA_PATH, "r") as f:
    raw_data = json.load(f)

TRAIN_DATA = [(entry["text"], {"cats": {entry["intent"]: 1.0}}) for entry in raw_data["intents"]]

# Create blank English NLP model
nlp = spacy.blank("en")

# Add text categorizer to pipeline
if "textcat" not in nlp.pipe_names:
    textcat = nlp.add_pipe("textcat", last=True)
else:
    textcat = nlp.get_pipe("textcat")

# Add unique intent labels
labels = list(set(intent["intent"] for intent in raw_data["intents"]))
for label in labels:
    textcat.add_label(label)

# Prepare examples
examples = [Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in TRAIN_DATA]

# Training loop
optimizer = nlp.begin_training()
for i in range(10):  # Epochs
    random.shuffle(examples)
    losses = {}
    batches = minibatch(examples, size=compounding(4.0, 32.0, 1.5))
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)
    print(f"Epoch {i+1} Loss: {losses['textcat']}")

# Save the model
MODEL_DIR = os.path.join("intent_model", "model", "nlu_model")
os.makedirs(MODEL_DIR, exist_ok=True)
nlp.to_disk(MODEL_DIR)
print(f"✅ Model saved to {MODEL_DIR}")
