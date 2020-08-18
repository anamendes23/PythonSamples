# string: data type used to represent a piece of text
name = "Sasha"
color = 'gold'

print("Name: " + name + ", Favorite color: " + color)
print("example"*3)
pet = "looooooooooooooong cat"
print(len(pet))

# Parts of a string
# String indexing
name = "Jaylen"
print(name[1])
# print last character
print(name[len(name)-1])
# when you don't know the length
print(name[-1])

# slice or substring
color = "Orange"
print(color[1:4]) #last number is not inclusive
print(color[:4]) # starts from 0 and stops at 3
print(color[4:]) # starts at 4 and stops at last character

# creating a new string
# once the string is created, you can't change it's characters
# strings in Python are immutable
message = "A kong string with a silly typo"
# message[2] = "l" will produce an error
new_message = message[0:2] + "l" + message[3:]
print(new_message)
# you don't have to create a new string variable every time, you can just
# reassign a value to the original variable

# Find indexes of characters
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("Dog"))
# print(pets.index("Q")) - if character no found, value error is thrown
print(pets.index("s"))

# to avoid the error
print("Dragons" in pets)
print("Cats" in pets)

# replace old domain by new domain
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# more string methods
print("Mountain".upper())
print("Montain".lower())
print("  yes  ".strip()) # removes white space characters
print("  yes  ".lstrip()) # removes white spaces on the left
print("  yes  ".rstrip()) # remotes white spaces on the right
count = "Hello my dear friend. How are you doing?".count("e")
print(count)
print("Forrest".endswith("rest"))
print("Forrest".isnumeric())
print("12345".isnumeric())
print(int("1234") + int("5632"))
print(" ".join(["This","is","a","phrase","joined","by","spaces"]))
print("...".join(["This","is","a","phrase","joined","by","ellipses"]))

# split into list of string
words = "This is another example".split()
print(words)

# Formatting strings
name = "Manny"
number = len(name)*3
print("Hello {}, your lucky number is {}.".format(name, number))

print("You lucky number is {number}, {name}.".format(name=name,number=len(name)*3)) # the order of the parameters passed
# doesn't matter in this case

price = 7.5
with_tax = price*1.1
print(price, with_tax)
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price,with_tax))
print("Base price: ${price:.2f}. With tax: ${tax:.2f}".format(price=price, tax=with_tax))

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# align to the right for a total of 3 spaces
