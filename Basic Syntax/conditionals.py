# COMPARING THINGS IN PYTHON

# boolean type returned
print(10>1)
# prints True

# Equality operation
print("cat" == "dog")
# prints False

# Not equals operator
print(1 != 2)
# prints True

# type error
print(1 < "1")

print( 1 == "1")
# prints False
# Python can compare, but considers 1 as int different than 1 as string

print("cat" > "Cat")
# prints True
# In Python uppercase letters are alphabetically sorted before lowercase letters.

# LOGICAL OPERATORS
# and or not
print("Yellow" > "Cyan" and "Brown" > "Magenta")
# prints False
print(25 > 50 or 1 != 2)
# prints True
# not operator inverts the value of the expression that's in front of it. 
print(not 42 == "Answer")
# prints True

# BRANCHING WITH IF STATEMENTS

# valid user name
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username.")

# else statement is not necessary
def is_even(number):
    if number%2 == 0:
        return True
    return False

# elfi

def hint_username2(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("Valid username.")

