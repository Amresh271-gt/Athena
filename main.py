# main.py
from core.brain import Brain
from utils.logger import log_info

def main():
    print("🧠 Athena is online. Type 'exit' to quit.")
    brain = Brain()

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            response = brain.process(user_input)
            print(f"Athena: {response}")

            if response.lower() == "exit":
                print("Athena shutting down. Goodbye! 👋")
                break

        except KeyboardInterrupt:
            print("\nAthena interrupted. Goodbye! 👋")
            break
        except Exception as e:
            log_info(f"Main loop error: {e}")
            print("Athena: Something went wrong. Please try again.")

if __name__ == "__main__":
    main()
