x = ["Now", "we", "are", "cooking"]
print(type(x))
print(x)
print(len(x))
print("are" in x)
print("Today" in x)
print(x[0])
# methods are the same used in strings in previous lesson
# print(x[4]) list index out of range error

print(x[1:3]) # index 3 element is not inclusive
print(x[:2])
print(x[2:])

# strings and lists are examples of sequence data structures

# Modifying the contents of a list
# different from strings, lists are mutable

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi") # add element to the end of a list
print(fruits)
fruits.insert(0, "Orange")
print(fruits) # add element at the index specified
fruits.insert(25, "Peach") # 25 index doesn't exist, so lists add element to the end
print(fruits)

fruits.remove("Melon")
print(fruits)
# fruits.remove("Pear") # throws value error
print(fruits.pop(3))
print(fruits)
fruits[2] = "Strawberry"
print(fruits)


