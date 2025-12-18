# datetime_skill.py
from datetime import datetime

def get_date():
    return datetime.now().strftime("Today is %A, %d %B %Y")

def get_time():
    return datetime.now().strftime("Current time is %H:%M:%S")
