import pyfiglet

# result = pyfiglet.figlet_format("Calculator")
# print(result)

msg = """
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

# def add(a,b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

add = lambda a ,b : a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b


while True:
    operation = input(msg)

    if operation == "5":
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    

    result = 0

    if operation == "1":
        result = add(num1, num2)
    elif operation == "2":
        result = subtract(num1, num2)
    elif operation == "3":
        result = multiply(num1, num2)
    elif operation == "4":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        continue
    print("==============================")
    print("Result:", result)
    print("==============================")
