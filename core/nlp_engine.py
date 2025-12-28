import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import json
from pathlib import Path
import re

# Load intents only once
INTENTS_PATH = Path("data/intents.json")

with open(INTENTS_PATH, encoding="utf-8") as file:
    INTENTS = json.load(file)

# Download NLTK resources (first time only)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

# -----------------------------
# Intent Detection (returns dict)
# -----------------------------
def detect_intent(user_input: str, threshold: float = 0.2) -> dict:
    user_tokens = set(preprocess_text(user_input))
    best_intent = "fallback"
    highest_match = 0.0

    for intent, data in INTENTS.items():
        examples = data.get("examples", [])
        for example in examples:
            example_tokens = set(preprocess_text(example))
            match_count = len(user_tokens & example_tokens) / max(len(example_tokens), 1)
            if match_count > highest_match:
                highest_match = match_count
                best_intent = intent

    confidence = highest_match
    if highest_match < threshold:
        best_intent = "fallback"

    # Extract entities based on intent
    entities = extract_entities(user_input, best_intent)

    return {
        "intent": best_intent,
        "confidence": confidence,
        "entities": entities
    }

# -----------------------------
# Entity Extraction
# -----------------------------
def extract_entities(user_input: str, intent: str) -> dict:
    entities = {}

    if intent == "play_song":
        match = re.search(r'play (song )?(.*)', user_input, re.IGNORECASE)
        if match:
            entities["song"] = match.group(2).strip()

    elif intent == "open_app":
        match = re.search(r'open (app )?(.*)', user_input, re.IGNORECASE)
        if match:
            entities["app"] = match.group(2).strip()

    elif intent == "set_alarm":
        match = re.search(r'at (\d{1,2}(:\d{2})?\s?(AM|PM)?)', user_input, re.IGNORECASE)
        if match:
            entities["time"] = match.group(1).strip()

    elif intent == "get_weather":
        match = re.search(r'in ([a-zA-Z\s]+)', user_input, re.IGNORECASE)
        if match:
            entities["location"] = match.group(1).strip()

    return entities
