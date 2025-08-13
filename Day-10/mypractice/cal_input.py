num1 = float(input("Please provide first number:"))
num2 = float(input("Please provide second number:"))

try:
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Please provide another number")    