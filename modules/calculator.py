add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else None

msg = """
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

isRunning = True