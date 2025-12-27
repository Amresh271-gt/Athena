# brain.py
from features import datetime_skill, system_commands
from datetime import datetime
from core import nlp_engine
from features import weather_skill


def get_response(user_input):
    intent = nlp_engine.detect_intent(user_input)

    if not intent:
        return "I'm not sure I understood that. Can you rephrase?"

    intent_map = {
        "greeting": lambda: f"{system_commands.get_greeting()}! How can I help you today?",
        "get_time": datetime_skill.get_time,
        "get_date": datetime_skill.get_date,
        "help": system_commands.help_message,
        "get_weather": weather_skill.get_weather
    }

    if intent == "exit":
        return "exit"

    if intent in intent_map:
        return intent_map[intent]()

    return "I am not sure how to respond to that yet."
