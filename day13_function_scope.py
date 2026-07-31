# Day 13 - Function Scope
# Scope refers to the region of a program where a variable is defined and can be accessed. In Python, there are two main types of scope: global and local.

def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 #It creates a local variable called z which is destroyed after this functions returns
    return c

def greet():
    z = 32 #Local variable
    print("Hello, World!")

z = 8 # z is a global variable
print(sum(4, 7))
print(z) # This will print 8 because z is defined in the global scope

greet()  # add this at the bottom