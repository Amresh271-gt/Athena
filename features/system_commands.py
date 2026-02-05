# system_commands.py
from features.skill_base import Skill
from utils.logger import log_info
from datetime import datetime

class GreetingSkill(Skill):
    name = "greeting"

    def run(self, entities=None):
        return "Hello! How can I help you today?"

class HelpSkill(Skill):
    name = "help"

    def run(self, entities=None):
        return "I can help you with music, apps, time, date, weather, and system commands."

class SetAlarmSkill(Skill):
    name = "set_alarm"

    def run(self, entities=None):
        time = entities.get("time") if entities else None
        if not time:
            return "Please provide a time for the alarm."
        log_info(f"System Skill: Alarm set for {time}")
        return f"Alarm set for {time}"

class ExitSkill(Skill):
    name = "exit"

    def run(self, entities=None):
        return "exit"
