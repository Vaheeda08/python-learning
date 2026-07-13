# Day 13 - Global Variables
# Global variables are variables that are defined outside of a function and can be accessed and modified by any function in the program.
# Global variables are useful when you want to share data between different functions or when you want to maintain a state that is accessible throughout the program.

def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z # tells Python that we want to use the global variable z instead of creating a local variable z
    z = 0 # This will refer to global z and not create a local variable z
    return c

z = 3
print(sum(2, 12))
print(z) # This will print 0 because we modified the global variable z in the sum function