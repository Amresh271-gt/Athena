# brain.py
from features import datetime_skill, system_commands
from datetime import datetime

def get_response(user_input):
    user_input = user_input.lower()
    
    # Basic greetings
    if "hello" in user_input or "hi" in user_input:
        return f"{system_commands.get_greeting()}! How can I help you today?"
    
     # Help command
    elif "help" in user_input:
        return system_commands.help_message()
    
    # Date query
    elif "date" in user_input:
        return datetime_skill.get_date()
    
    # Time query
    elif "time" in user_input:
        return datetime_skill.get_time()
    
    # Fallback
    else:
        return "I am not sure how to respond to that yet."
