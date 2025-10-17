fruits = ["Aaam", "papita", "angur", "prince"]


# 1. len() function to count number of items in a list

# number_of_fruits = len(fruits) 
# print("Number of fruits:", number_of_fruits)


# 2. List using list() function

# my_list_using_list_function = list(("apple", "banana", "cherry"))
# print(my_list_using_list_function)


# 3. Accessing items in a list using indexing

# print(fruits[1])  # Output: angur'
# print(fruits[-1])  # Output: papita


# 4. Accessing items in a range 

# print(fruits[0:2]) 

# 5. Checking if an item exists in a list

if "Angur" in fruits:
    print("Yes, 'angur' is in the fruits list")

# 6. Modifying items in a list 

# fruits[1] = "Mango"    
# print(fruits)

# fruits[1:3] = ["Banana", "Grapes"]
# print(fruits)


# 7. Inserting items into a list

# fruits.insert(1, "Banana")  # Insert function to add 'Banana' at index 1
# print(fruits)

# 8 . Appending items to the end of a list

# fruits.append("Kiwi")
# print(fruits)

# 9. Extending a list with another list

# more_fruits = ["Pineapple", "Mango"]
# fruits.extend(more_fruits)
# print(fruits)

# 10. Removing items from a list 

# fruits.remove("Aaam")  # Remove function to delete 'Aaam'
# fruits.remove("angur")  # Remove function to delete 'angur'
# print(fruits)

# 11. Pop in a list 

# popped_fruit = fruits.pop(0)  # Pops the last item
# print(fruits)

# 12. del keyword to delete an item at a specific index 

# del fruits[0:2]  # Deletes item at index 2
# print(fruits)

# 13. Clear a list 

# fruits.clear()
# print(fruits)


# 14. Looping through a list

# for fruit in fruits:
#     print(fruit)



# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# 15. List sorting

# fruits.sort(reverse = True)  # Sorts the list in ascending order
# print(fruits)

# 16. Copying a list 

# fruits_copy = fruits.copy()
# fruits_copy.append("Pineapple")
# print(fruits)
# print(fruits_copy)




# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list