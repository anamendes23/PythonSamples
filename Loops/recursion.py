# recursion is the repeated application of the same procedure to a smaller problem
# in programming, recursion is a way of doing a repetitive task by having a function call itself
# the stop condition is called the base case

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# let's check step by step
def factorial2(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial2(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial2(4)

# EXAMPLES
# Directories are an example of recursive structure, because they can contain subdirectories
# to count how many files are in a directory, recursion is a good solution because you have to
# count the files inside the subdirectories as well
# the base case will be a directory without any subdirectories

# recursive structures: anything that contains itself
# Active Directory
# LDAP

# in Python, the default is to be able to call a recursive function a max of 1,000 times
factorial(1000)
