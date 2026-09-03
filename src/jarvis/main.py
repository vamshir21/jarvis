from .classify import classify
from .router import routes


def main():
    text = input("Enter your command: ")

    intents = classify(text.lower())

    print(f"Classified intents: {intents}")

    for intent in intents:
        if intent in routes:
            routes[intent]()
            
            print(f"Routing to: {intent}")
        else:
            print("Unknown intent. Please try again.")

        