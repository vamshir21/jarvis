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