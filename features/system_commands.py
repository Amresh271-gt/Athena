# system_commands.py
from datetime import datetime

def get_greeting():
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Hello"

def help_message():
    return (
        "You can ask me things like:\n"
        "- 'time' → to know current time\n"
        "- 'date' → to know today's date\n"
        "- 'hello' → greetings\n"
        "- 'exit' → to quit Athena"
    )
