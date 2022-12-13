welcome_string = """
Select operation:
    1. Add (+)
    2. Subtract (-)
    3. Multiply (*)
    4. Divide (/)
"""

while True:
    print(welcome_string)

    operation = input("Enter operation (1/2/3/4): ")
    if operation not in ("1", "2", "3", "4"):
        print(f"Unsupported operation: \"{operation}\". Try again.")
        continue

    try:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
    except ValueError:
        print("Entered values are not a number. Try again.")
        continue

    match operation:
        case "1":
            print(num_1 + num_2)
        case "2":
            print(num_1 - num_2)
        case "3":
            print(num_1 * num_2)
        case "4":
            if not num_2:
                print(f"Division by zero! Try again.")
                continue

            print(num_1 / num_2)
