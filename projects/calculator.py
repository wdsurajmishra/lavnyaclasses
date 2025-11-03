print("+=============================+")
print("welcome to the calculator project!")
print("+=============================+")

msg = """
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""

operation = input(msg)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "1":
    print("Result:", num1 + num2)
elif operation == "2":
    print("Result:", num1 - num2)
elif operation == "3":
    print("Result:", num1 * num2)
elif operation == "4":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")