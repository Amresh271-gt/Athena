# skill_base.py
class Skill:
    """
    Base class for all skills.
    Each skill must implement:
      - name: unique identifier
      - run(entities): main execution function
    """
    name = "base_skill"

    def run(self, entities=None):
        raise NotImplementedError("Skill must implement run()")
