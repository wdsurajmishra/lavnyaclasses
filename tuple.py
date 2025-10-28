my_tuple = (1, 2, 3)

# my_tuple_without_parantheses = 4, 5, 6

# print("Tuple with parentheses:", my_tuple)
# print("Tuple without parentheses:", my_tuple_without_parantheses)

# tuple_with_single_element = (42,)
# print("Type of tuple_with_single_element:", type(tuple_with_single_element))

persons = ("Suraj", "Krishna", "Anshita")

# first, second, third = persons

# print("First person:", first)
# print("Second person:", second)
# print("Third person:", third)


# print(persons[1])

# tuple_with_list = (1, 2, [3, 4])
# tuple_with_list[2][0] = 300

# print("Modified tuple:", tuple_with_list)

third_tuple= my_tuple + persons
# print("Concatenated tuple:", third_tuple)


tuple_convert_into_list = list(my_tuple)
tuple_convert_into_list[1] = "Updated"
print("Modified list:", tuple_convert_into_list)