# Day 13 - Function Scope

def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 #It creates a local variable called z which is destroyed after this functions returns
    return c

def greet():
    z = 32 #Local variable
    print("Hello, World!")

z = 8 # z is a global variable
print(sum(4, 6))
print(z) # This will print 8 because z is defined in the global scope