# while loops perform repetitive work until a condition is met

# initializing: to give an initial value to a variable
x = 0
while x < 5:
    print("Not there yet, x= " + str(x))
    x = x + 1
print("x= " + str(x))

# abstracting script above
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        #shorthand version of x = x + 1
        x += 1
    print("Done")

attempts(5)

'''
Practical example:

    username = get_username()
    while not valid_username(username):
        print("Invalid username")
        username = get_username()

the script above uses external functions and requests that the user enters the
username until it is correct
'''
# how to break infinite loops:
# press ctrl + c if it happens when running or add break to the body of the loop
x = 0
while x % 2 == 0:
    x = x / 2
    break

# ping is an infinite loop used to send packages
