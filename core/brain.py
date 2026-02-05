# brain.py
from core.nlp_engine import NLPEngine
from core.memory import Memory
from core.skill_registry import load_skills
from utils.logger import log_info
import features  # features package (contains all skills)

CONFIDENCE_THRESHOLD = 0.3

class Brain:
    def __init__(self):
        self.nlp = NLPEngine()
        self.memory = Memory()
        # Load all skills dynamically from features
        self.skills = load_skills(features)
        log_info(f"Brain initialized with skills: {list(self.skills.keys())}")

    def safe_call(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
              import traceback
              traceback.print_exc()   # 🔥 shows exact error line
              return f"ERROR: {str(e)}"


def process(self, user_input):
    nlp_result = self.nlp.detect_intent(user_input)
    intent = nlp_result.get("intent", "fallback")
    confidence = nlp_result.get("confidence", 0.0)
    entities = nlp_result.get("entities", {})

    last_intent = self.memory.get("last_intent")
    last_entities = self.memory.get("last_entities", {})

    # Use last_entities for multi-turn if current entities are missing
    if intent == last_intent:
        for k, v in last_entities.items():
            if k not in entities:
                entities[k] = v

    # Clarification if intent unknown or confidence low
    if intent == "fallback" or confidence < CONFIDENCE_THRESHOLD:
        intent = "clarify"

    # Execute skill dynamically
    skill = self.skills.get(intent)
    if skill:
        response = self.safe_call(skill.run, entities)
    else:
        if intent == "clarify":
            response = "I am not sure how to respond to that yet. Can you rephrase?"
        else:
            response = f"I don't have a skill for '{intent}' yet."

    # Update memory
    self.memory.update(intent, user_input, entities)

    log_info(f"NLP Result: {nlp_result}")
    return response 
