# brain.py
from features import datetime_skill, system_commands, weather_skill, app_skill, music_skill
from core import nlp_engine, memory

CONFIDENCE_THRESHOLD = 0.3

def get_response(user_input):
    # Detect intent with confidence and entities
    nlp_result = nlp_engine.detect_intent(user_input)

    intent_name = nlp_result.get("intent", "fallback")
    confidence = nlp_result.get("confidence", 0.0)
    entities = nlp_result.get("entities", {})

    # Load previous memory/context
    user_memory = memory.load_memory()
    last_intent = user_memory.get("last_intent")

    # Low confidence → fallback to last intent or clarify
    if intent_name == "fallback" or confidence < CONFIDENCE_THRESHOLD:
        intent_name = "clarify"

    # Map intents to actual functions/responses
    def safe_call(func, param=None):
        try:
            if param:
                return func(param)
            else:
                return func()
        except:
            return "Something went wrong executing this command."

    intent_map = {
        "greeting": lambda: f"{system_commands.get_greeting()}! How can I help you today?",
        "get_time": lambda: safe_call(datetime_skill.get_time),
        "get_date": lambda: safe_call(datetime_skill.get_date),
        "help": lambda: safe_call(system_commands.help_message),
        "get_weather": lambda: safe_call(weather_skill.get_weather, entities.get("location")),
        "play_song": lambda: safe_call(music_skill.play_song, entities.get("song")),
        "open_app": lambda: safe_call(app_skill.open_app, entities.get("app")),
        "set_alarm": lambda: safe_call(system_commands.set_alarm, entities.get("time")),
        "exit": lambda: "exit",
        "clarify": lambda: "I am not sure how to respond to that yet. Can you rephrase?"
    }

    # Execute function if intent exists
    response = intent_map.get(intent_name, lambda: "I am not sure how to respond to that yet.")()

    # Save updated memory/context
    memory.update_memory(intent_name, user_input)

    return response
