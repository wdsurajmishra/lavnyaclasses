# WHILE LOOPS 


# isRunning = True
# count = 0

# while isRunning:
#     print("This loop will run forever unless interrupted.")
#     count += 1 # Har baar Count ka increment.
#     if count == 5:
#         isRunning = False  # Jab count 5 ho jaye, loop ko rok do.


# CONTINUE EXAMPLE 

# count = 0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         continue  # Agar count even hai, to neeche ka code skip karo aur loop ke next iteration pe jao.
#     print(f"Odd number: {count}")  # Sirf odd numbers print honge.

# ==================== FOR LOOPS =========================

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for i in range(1,10):
#     print(i)


# nested loop 

# fruits = [
#     ["apple", "banana", "cherry"],
#     ["orange", "kiwi", "melon"],
#     ["grape", "peach", "plum"]
# ]

# for sublist in fruits:
#     for fruit in sublist:
#         print(fruit)


students = [
    {
        "name":"Krishna",
        "course": "Python"
    },
    {
        "name": "Prince",
        "course": "ADCA"
    },
    {
        "name": "Abhay",
        "course": "Web Development"
    }
]

for issadansd in students:
    print(f"{issadansd['name']} is enrolled in {issadansd['course']} course.")