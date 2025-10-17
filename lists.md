## lists.py — List examples and reference

This file documents the examples and list operations shown in `lists.py`. It is intended as a beginner-friendly reference to Python lists, with short examples and notes that mirror the code in the repository.

### Overview

`lists.py` demonstrates common list operations in Python using the sample list:

```py
fruits = ["Aaam", "papita", "angur", "prince"]
```

The examples cover: getting length, creating lists, indexing and slicing, membership testing, modification, insertion, appending, extending, removal, popping, deletion, clearing, looping, comprehension-style filtering, sorting, copying, and a short method reference.

### Basic operations

- len(list): returns the number of items in a list.

Example:

```py
# number_of_fruits = len(fruits)
# print("Number of fruits:", number_of_fruits)
```

- list(iterable): creates a list from an iterable (for example, a tuple).

Example:

```py
# my_list_using_list_function = list(("apple", "banana", "cherry"))
# print(my_list_using_list_function)
```

### Indexing and slicing

- Access items by index: `fruits[0]`, `fruits[1]`, etc. Negative indexes count from the end (`fruits[-1]`).
- Slicing returns a sub-list: `fruits[0:2]` returns the first two items.

Example:

```py
# print(fruits[1])  # second item
# print(fruits[-1])  # last item
# print(fruits[0:2])  # slice of first two items
```

### Membership test

Use `in` to check if a value exists in the list.

Example from `lists.py`:

```py
if "Angur" in fruits:
	print("Yes, 'angur' is in the fruits list")
```

Note: membership checks are case-sensitive. In the example above the list contains the lowercase string "angur" while the test uses "Angur"; to match correctly the case must be the same.

### Modifying lists

- Assign to an index to change a single item: `fruits[1] = "Mango"`.
- Assign to a slice to replace multiple items: `fruits[1:3] = ["Banana", "Grapes"]`.

Examples:

```py
# fruits[1] = "Mango"
# fruits[1:3] = ["Banana", "Grapes"]
```

### Inserting, appending, and extending

- `insert(index, value)`: insert value at given index.
- `append(value)`: add value at the end.
- `extend(iterable)`: add all elements from another iterable.

Examples:

```py
# fruits.insert(1, "Banana")
# fruits.append("Kiwi")
# more_fruits = ["Pineapple", "Mango"]
# fruits.extend(more_fruits)
```

### Removing items

- `remove(value)`: removes the first occurrence of value (raises ValueError if not found).
- `pop([index])`: removes and returns item at index (default last). Raises IndexError if list is empty or index out of range.
- `del`: delete by index or slice.
- `clear()`: remove all items.

Examples:

```py
# fruits.remove("Aaam")
# popped = fruits.pop(0)
# del fruits[0:2]
# fruits.clear()
```

### Looping and list comprehensions

Classic loop:

```py
# for fruit in fruits:
#     print(fruit)
```

Filtering into a new list:

```py
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
```

This can be expressed as a list comprehension:

```py
# newlist = [x for x in fruits if "a" in x]
```

### Sorting and copying

- `sort(reverse=True)` sorts in descending order when reverse=True. Default is ascending.
- `copy()` returns a shallow copy of the list.

Examples:

```py
# fruits.sort(reverse=True)
# fruits_copy = fruits.copy()
# fruits_copy.append("Pineapple")
```

### Method quick reference

Method | Description
:--|:--
append() | Adds an element at the end of the list
clear() | Removes all the elements from the list
copy() | Returns a shallow copy of the list
count() | Returns the number of elements with the specified value
extend() | Add the elements of an iterable to the end of the current list
index() | Returns the index of the first element with the specified value
insert() | Adds an element at the specified position
pop() | Removes and returns the element at the specified position
remove() | Removes the first item with the specified value
reverse() | Reverses the order of the list in-place
sort() | Sorts the list in-place

### Notes and edge cases

- Lists in Python are ordered, mutable, and allow duplicate elements.
- Methods like `remove()` and `index()` raise exceptions if the value is not found; handle with try/except if the input is uncertain.
- `copy()` creates a shallow copy. For nested lists, use `copy.deepcopy()` from the `copy` module if an independent deep copy is required.
- Most list methods modify the list in-place and return `None` (for example, `list.sort()` and `list.reverse()` do not return the modified list).

### Further reading

- Official Python tutorial: Data Structures — lists
- Python built-in methods documentation for `list`
