# first_name, last_name = "John", "Doe"

# print(first_name, last_name)


first_name = "John"


def print_name():
    print(first_name)

def change_name():
    global last_name
    last_name = "Smith"

change_name()    


print(last_name)