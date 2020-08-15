# For loops allow you to iterate over a sequence of values

# by default, the value in range starts with x = 0
# the range number is not inclusive
for x in range(5):
    print(x)

# you can loop through strings in an array
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi "+ friend)

# when you want to start to iterate in a number different than zero,
# add more parameters to range(start, end). Note that end is not inclusive
product = 1
for n in range(1,10):
    product = product * n
print(product)

# the default step is 1
# to change the step, type range(start, end, step)

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

# NESTED LOOPS
# printing domino tiles
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

# note that end= parameter in print changes the default newline character to what you define

# print all possible combinations of teams
# not that a team cannot play itself

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# another way to iterate over a list
for x in [25, 26, 27]:
    print(x)

# another example and what would happen if instead of passing a list, you pass a single value outside a list
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

#call with a list
greet_friends(['Taylor', 'Pat', 'Ana'])
# call with single element in list
greet_friends(['Ana'])
# call with single variable outside list
greet_friends("Ana")
# strings are iterable, so it'll print each character in the string
# this won't work for a number, for example

