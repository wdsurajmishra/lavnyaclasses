unique_numbers = {1, 2, 3, 4, 5, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_from_list = set(my_list)
print(unique_from_list)  # Output: {1, 2, 3, 4, 5}

unique_from_list.add(6)
unique_from_list.remove(2)
print(unique_from_list)  # Output: {1, 2, 3,