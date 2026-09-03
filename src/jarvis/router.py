from .calculator import calculate
from .parser import parse


def classify(text):

    intents = []

    if "calculate" in text:
        intents.append("calculate")

    if "search" in text:
        intents.append("search")

    if "remind" in text:
        intents.append("remind")

    if len(intents) == 0:
        intents.append("unknown")

    return intents


def route(intents, text):

    if "calculate" in intents:
        result = calculate(*parse(text))
        print(f"Calculator result: {result}")

    if "search" in intents:
        print("Routing to search module...")

    if "remind" in intents:
        print("Routing to reminder module...")

    if "unknown" in intents:
        print("Unknown intent. Please try again.")


text = input("Enter your command: ")

intents = classify(text.lower())

print(f"Classified intents: {intents}")

route(intents)