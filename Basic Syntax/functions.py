# defining functions
def greeting(name):
    print("Welcome, " + name)

# call function
greeting("Ana")

# type none
result = greeting("Banana")
# Python will print "None", because greeting doesn't return anything
print(result)

# function with two parameters
def greeting2(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting2("Ana", "CS")

# returning values
def area_triangle(base, height):
    return (base*height)/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    # floor division //
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# Principles of Code Reuse
# Rule of Thumb: if you see the same line repeating, it can be a good candidate
# for code reuse. Add to a function

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

# call function multiple times.
# code is cleaner and more readable
lucky_number("Ana")
lucky_number("Banana")

