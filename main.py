# main.py

from core import brain, memory
from features import datetime_skill
from utils import logger, helper
import sys

def main():
    print("Starting Athena...\n")
    
    # Load or initialize memory
    user_data = memory.load_memory()
    
    # Greeting
    if "name" in user_data:
        print(f"Hello {user_data['name']}! Welcome back.")
        logger.log_info(f"Returned user: {user_data['name']}")
    else:
        name = input("Hi! What's your name? ").strip()
        user_data["name"] = name
        memory.save_memory(user_data)
        print(f"Nice to meet you, {name}!")
        logger.log_info(f"New user: {name}")
    
    print("Athena is ready. Type 'exit' to quit.\n")
    
    # Main loop
    while True:
        user_input = input("You: ")
        cleaned_input = helper.clean_input(user_input)
        logger.log_info(f"User input: {cleaned_input}")
        
        if cleaned_input in ["exit", "quit", "bye"]:
            print("Athena: Goodbye! Have a great day.")
            sys.exit()
        
        # Send input to brain for processing
        response = brain.get_response(cleaned_input)
        print(f"Athena: {response}\n")

if __name__ == "__main__":
    main()
