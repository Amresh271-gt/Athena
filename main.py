from core import brain, memory, nlp_engine
from features import datetime_skill, weather_skill, system_commands
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
        
        if cleaned_input.lower() in ["exit", "quit", "bye"]:
            print("Athena: Goodbye! Have a great day.")
            sys.exit()
        
        # Get response from brain (handles multi-turn & context)
        response = brain.get_response(cleaned_input)
        
        # Handle exit intent
        if response == "exit":
            print("Athena: Goodbye! Have a great day.")
            sys.exit()
        
        # Print Athena's response
        print(f"Athena: {response}\n")

if __name__ == "__main__":
    main()
