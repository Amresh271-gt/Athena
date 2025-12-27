# nlp_engine.py
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import json
from pathlib import Path

# Load intents only once
INTENTS_PATH = Path("data/intents.json")

with open(INTENTS_PATH, encoding="utf-8") as file:
    INTENTS = json.load(file)

# Download NLTK resources (first time only)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """
    Preprocess user input:
    - Lowercase
    - Tokenize
    - Remove stopwords
    - Lemmatize words
    """
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords & lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return tokens

def detect_intent(user_input):
    """
    Detect user intent based on NLP processed tokens
    """
    user_tokens = preprocess_text(user_input)

    best_intent = None
    highest_match = 0

    for intent, data in INTENTS.items():
        examples=data.get("examples",[])
        for example in examples:
            example_tokens = preprocess_text(example)

            # Count matching tokens
            match_count = len(set(user_tokens) & set(example_tokens))

            if match_count > highest_match:
                highest_match = match_count
                best_intent = intent

    return best_intent
