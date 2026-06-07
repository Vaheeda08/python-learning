# Day 13 - Docstrings

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