

# def add_numbers(a, b):
#     """Returns the sum of two numbers."""
#     return a + b

# # result = add_numbers(10, 25)
# # print("The sum is:", result)


# def upper_case_convertor(txt):
#     """Converts a string to uppercase."""
#     return txt.upper()


# converted_text = upper_case_convertor("hello world")
# # print("Converted Text:", converted_text)


# def greet(name):
#     """Returns a greeting message for the given name."""
#     return f"Hello, {name}!"


# greet_list = [
#     'Suraj', 'Aditya', 'Rohan', 'Sahil', 'Ankit'
# ]

# for person in greet_list:
#     message = greet(person)
#     print(message)



def print_car_details(name, *colors, **specs):
    """Prints the car name and its available colors."""
    print(f"Car Name: {name}")
    print("Specifications:")

    for spec, value in specs.items():
        print(f"{spec}: {value}")

    print("Available Colors:")
    for color in colors:
        print(color)

# print_car_details("Car", "Red", "Blue", "Green", "Black", isAutomatic=True, year=2020)




def calculate_mutiple_numbers(*args):
    """Calculates the product of multiple numbers."""
    count = 0
    for num in args:
        count += num
    return count

print(calculate_mutiple_numbers(2, 3, 4, 5))



