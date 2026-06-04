# Day 10 = Function Arguments
# In Python, there are several types of function arguments that you can use to make your functions more flexible and versatile. The main types of function arguments are:

# 1. Positional Arguments
def greet(name):
    print(f"Hello, {name}!")
greet("Vaheeda")
print()

# 2. Keyword Arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet(name="Vaheeda", greeting="Hi")
print()

# 3. Default Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Vaheeda")
greet("Vaheeda", "Hi")
print()

# 4. Variable-length Arguments
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Maryam", "Anas", "Afifa")
print()