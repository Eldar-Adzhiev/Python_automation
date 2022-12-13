welcome_string = """
Select operation:
    1. Add (+)
    2. Subtract (-)
    3. Multiply (*)
    4. Divide (/)
"""

actions = {
    '1': float.__add__,
    '2': float.__sub__,
    '3': float.__mul__,
    '4': float.__truediv__
}


while True:
    print(welcome_string)

    operation = input("Enter operation (1/2/3/4): ")
    if operation not in actions:
        print(f"Unsupported operation: \"{operation}\". Try again.")
        continue

    try:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
    except ValueError:
        print("Entered values are not a number. Try again.")
        continue

    try:
        action = actions[operation]
        res = action(num_1, num_2)
        print(res)
    except ZeroDivisionError:
        print(f"Division by zero! Try again.")
