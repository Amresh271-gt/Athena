# memory.py
import json
import os
from pathlib import Path
from utils.logger import log_info

MEMORY_FILE = Path("data/user_memory.json")

# memory.py
class Memory:
    def __init__(self):
        self.memory_file = MEMORY_FILE
        self.memory = self.load()

    def load(self):
        if os.path.exists(self.memory_file):
            try:
                data = json.load(open(self.memory_file, "r"))
                return data
            except json.JSONDecodeError:
                return {}
        return {}

    def save(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def update(self, intent, user_input, entities=None):
        self.memory["last_intent"] = intent
        self.memory["last_input"] = user_input
        if entities:
            self.memory["last_entities"] = entities
        self.save()
        log_info(f"Memory updated: Intent={intent}, Input={user_input}, Entities={entities}")

    def get(self, key, default=None):
        return self.memory.get(key, default)

