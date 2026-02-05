# nlp_engine.py
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import json
from pathlib import Path
import re
from utils.logger import log_info

# Load intents once
INTENTS_PATH = Path("data/intents.json")
with open(INTENTS_PATH, encoding="utf-8") as file:
    INTENTS = json.load(file)

# Download NLTK resources once
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

class NLPEngine:
    def __init__(self):
        self.intents = INTENTS

    def preprocess_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
        return tokens

    def detect_intent(self, user_input, threshold=0.2):
        user_tokens = set(self.preprocess_text(user_input))
        best_intent = "fallback"
        highest_match = 0.0

        for intent, data in self.intents.items():
            examples = data.get("examples", [])
            for example in examples:
                example_tokens = set(self.preprocess_text(example))
                match_count = len(user_tokens & example_tokens) / max(len(example_tokens), 1)
                if match_count > highest_match:
                    highest_match = match_count
                    best_intent = intent

        confidence = highest_match
        if highest_match < threshold:
            best_intent = "fallback"

        entities = self.extract_entities(user_input, best_intent)

        log_info(f"NLPEngine: Intent detected: {best_intent}, Confidence: {confidence}, Entities: {entities}")
        return {
            "intent": best_intent,
            "confidence": confidence,
            "entities": entities
        }

    def extract_entities(self, user_input, intent):
        entities = {}
        if intent == "play_song":
            match = re.search(r'play (song )?(.*)', user_input, re.IGNORECASE)
            if match: entities["song"] = match.group(2).strip()
        elif intent == "open_app":
            match = re.search(r'open (app )?(.*)', user_input, re.IGNORECASE)
            if match: entities["app"] = match.group(2).strip()
        elif intent == "set_alarm":
            match = re.search(r'at (\d{1,2}(:\d{2})?\s?(AM|PM)?)', user_input, re.IGNORECASE)
            if match: entities["time"] = match.group(1).strip()
        elif intent == "get_weather":
            match = re.search(r'in ([a-zA-Z\s]+)', user_input, re.IGNORECASE)
            if match: entities["location"] = match.group(1).strip()
        return entities
