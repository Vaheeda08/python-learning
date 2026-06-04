# Day 10 - Functions Arguments
# Functions can have arguments, which are values that you can pass to the function when you call it.
# You can define a function with parameters, which are placeholders for the arguments that will be passed to the function.
# Here's an example of a function that takes two parameters and returns their sum:

def add(x, y, plus=0):
    return x + y + plus
result = add(3, 5)
print(result)

c = add(10, 20, 8)
print(c)