# core/skill_registry.py
import importlib
import pkgutil
from features import skill_base
import inspect

def load_skills(module):
    skills = {}
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and hasattr(obj, "name") and hasattr(obj, "run"):
            skill_instance = obj()
            skills[skill_instance.name] = skill_instance
    return skills