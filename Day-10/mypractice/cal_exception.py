import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

try:
    div = num1/num2
except ZeroDivisionError:
    print("Plz don't provide zero")