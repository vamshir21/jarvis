def parse(text):
    tokens = text.split()

    left = int(tokens[1])
    operator = tokens[2]
    right = int(tokens[3])

    return left, operator, right