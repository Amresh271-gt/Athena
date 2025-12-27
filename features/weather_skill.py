# features/weather_skill.py
def get_weather(location=None):
    if location:
        return f"Fetching weather for {location}... 🌤️"
    else:
        return "Fetching current weather... 🌤️"
