# app_skill.py
from features.skill_base import Skill
from utils.logger import log_info

class OpenAppSkill(Skill):
    name = "open_app"

    def run(self, entities=None):
        app = entities.get("app") if entities else None
        if not app:
            return "Please tell me the app name."
        
        log_info(f"App Skill: Opening {app}")
        # Placeholder: actual OS open code can be added later
        return f"Opening {app}..."
