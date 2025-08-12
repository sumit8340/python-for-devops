

def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 - num2

def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 * num2

def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."


# Now print the results from the returned values
print("Addition:", addition())
print("Subtraction:", subtraction())
print("Multiplication:", multiplication())
print("Division:", division())
