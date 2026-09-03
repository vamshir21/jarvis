def calculate(left, operator, right):
    if operator == "+":
        return left + right

    elif operator == "-":
        return left - right

    elif operator == "*":
        return left * right

    elif operator == "/":
        if right == 0:
            return "Cannot divide by zero"
        return left / right

    else:
        return "Unknown operator"