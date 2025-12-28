# memory.py
import json
import os
from pathlib import Path

MEMORY_FILE = Path("data/user_memory.json")

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_memory(intent, user_input):
    memory = load_memory()
    memory["last_intent"] = intent
    memory["last_input"] = user_input
    save_memory(memory)
