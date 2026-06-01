# Day 7: String Methods
# String methods are built-in functions that allow you to manipulate and work with strings in Python. Here are some commonly used string methods:
# 1. `lower()`: Converts all characters in a string to lowercase.
# 2. `upper()`: Converts all characters in a string to uppercase.
# 3. `strip()`: Removes leading and trailing whitespace from a string.
# 4. `replace(old, new)`: Replaces occurrences of a specified substring with another substring.
# 5. `split(separator)`: Splits a string into a list of substrings based on a specified separator.
# 6. `join(iterable)`: Joins elements of an iterable (like a list) into a single string, using a specified separator.
# Example usage:
# Using string methods
text = "  Hello, World!  "
print(text.lower())  # Output: "  hello, world!  "
print(text.upper())  # Output: "  HELLO, WORLD!  "
print(text.strip())  # Output: "Hello, World!"
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "
print(text.split(", "))  # Output: ['  Hello', 'World!  ']
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"
# These string methods can be very useful for various text processing tasks, such as formatting, cleaning, and manipulating strings in your Python programs.

name = 'Vaheeda'
name = "Vaheeda"
name = '''Vaheeda is a good girl'''
print(name)  # Output: Vaheeda is a good girl