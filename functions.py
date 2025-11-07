

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# result = add_numbers(10, 25)
# print("The sum is:", result)


def upper_case_convertor(txt):
    """Converts a string to uppercase."""
    return txt.upper()


converted_text = upper_case_convertor("hello world")
# print("Converted Text:", converted_text)


def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"


greet_list = [
    'Suraj', 'Aditya', 'Rohan', 'Sahil', 'Ankit'
]

for person in greet_list:
    message = greet(person)
    print(message)
