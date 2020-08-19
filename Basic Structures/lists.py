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

# Tuples: sequences of elements of any type, that are immutable
# written between parenthesis
# the position of the elements inside the tuple have meaning
fullname = ('Grace', 'M', 'Hopper')
# used to return multiple values in functions

def test():
    return "Grace", "M", "Hopper"

result = test()
type(result)
print(result)

# you can unpack tuples
first, middle, last = result
print(first, middle, last)

first, middle, last = test()
print(first, middle, last)

# Iterating over Lists and Tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
    chars += len(animals)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# enumate function
winners = ["Ashley", "Dilan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# enumerate returns a tuple with index and element information

# List of tuples containing name and email of each person
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example,com", "Shay Brandt")]))

# List Comprehensions
multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

# there's a better way to do this
multiples = [ x*7 for x in range(1,11) ]
print(multiples)

# List comprehensions: let us create new lists based on sequences or ranges

languages = ["Python", "Java", "Ruby", "Perl", "Go", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# get all numbers divisible by 3 between 0 and 100
z = [x for x in range(0,101) if x % 3 == 0]
print(z)
