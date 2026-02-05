# datetime_skill.py
from features.skill_base import Skill
from datetime import datetime

class GetTimeSkill(Skill):
    name = "get_time"

    def run(self, entities=None):
        return datetime.now().strftime("%I:%M %p")

class GetDateSkill(Skill):
    name = "get_date"

    def run(self, entities=None):
        return datetime.now().strftime("%d %B %Y")
