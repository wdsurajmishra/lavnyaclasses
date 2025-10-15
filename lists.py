fruits = ["Aaam", "angur","papita"]

# print(fruits[0]) isko index se acess kr sakte hai

fruits[0] = "Aam" # update krne ka code

fruits.append("Naspati") # ye add krne ka tarika

new_list = fruits.copy()


fruits.extend(new_list)


print(new_list)
print(fruits)

index = fruits.index("angur")

print(index)