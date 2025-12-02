class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error! Division by zero."
        return self.num1 / self.num2
    

while True:
    print("Welcome to the Calculator!")
    msg = """
    Please choose an operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    """

    print(msg)
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        calc = Calculator(num1, num2)

        if choice == '1':
            print(f"The result is: {calc.add()}")
        elif choice == '2':
            print(f"The result is: {calc.subtract()}")
        elif choice == '3':
            print(f"The result is: {calc.multiply()}")
        elif choice == '4':
            print(f"The result is: {calc.divide()}")
