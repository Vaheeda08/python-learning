# Day 13 - Docstrings
# Docstrings are a special type of string that is used to document a function, class, or module. They are enclosed in triple quotes (""" """) and are placed immediately after the function, class, or module definition.

def sum(a, b):
    """
    This function takes two arguments and returns their sum.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of a and b.
    """
    # a and b are local variables
    c = a + b
    z = 1 #It creates a local variables called z which is destroyed after this functions returns
    return c

print(sum.__doc__)
print(sum(2, 3)) # Output: 5