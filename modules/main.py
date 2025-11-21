from calculator import add, subtract, multiply, divide, msg, isRunning
from operations.functions import my_name

print(my_name)


while isRunning:
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
