# weather_skill.py
from features.skill_base import Skill
from utils.logger import log_info

class GetWeatherSkill(Skill):
    name = "get_weather"

    def run(self, entities=None):
        location = entities.get("location") if entities else None
        if not location:
            return "Please specify a location."
        
        log_info(f"Weather Skill: Fetching weather for {location}")
        # Placeholder: actual API call can be added later
        return f"Fetching weather for {location}..."
