# my_file = open("file.txt", "r")
# content = my_file.read()
# print(content)

# my_file = open("prince.txt", "a")
# my_file.write("Prince in Append Mode\n")


# my_file = open("prince.txt", "w")
# content = my_file.read()
# my_file.write(f"{content}\n Prince in Write Mode\n")
# my_file.close()


# import os

# os.remove("prince.txt")


students = ["Prince", "Krishna", "Aditya", "Anshita"]


def greetings(name):
    msg = f"Hello, {name}! Welcome to the class."
    return msg


for student in students:
    file = open(f"{student}.txt", "a")
    file.write(greetings(student) + "\n")
    file.close()