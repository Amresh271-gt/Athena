# features/app_skill.py
import os

def open_app(app_name):
    if not app_name:
        return "Which app would you like me to open?"
    
    # Example for Windows (can be extended)
    try:
        os.system(f"start {app_name}")
        return f"Opening {app_name}..."
    except Exception:
        return f"Sorry, I couldn't open {app_name}."
