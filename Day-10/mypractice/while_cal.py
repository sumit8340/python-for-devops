while True:
    print("\nSimple Calculator (type 'exit' to quit)")
    print("Operations: +  -  *  /")

    # Get input
    num1 = input("Enter first number: ")
    if num1.lower() == 'exit':
        break

    num2 = input("Enter second number: ")
    if num2.lower() == 'exit':
        break

    op = input("Enter operation (+, -, *, /): ")
    if op.lower() == 'exit':
        break

    # Try to convert numbers and calculate
    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numbers.")

print("Calculator exited.")
