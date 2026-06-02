# Day 08 - String Methods
# Python provides several built-in methods for manipulating strings. Here are some commonly used string methods:
# 1. `upper()`: Converts all characters in a string to uppercase.
# 2. `lower()`: Converts all characters in a string to lowercase.
# 3. `capitalize()`: Capitalizes the first character of a string and converts the rest to lowercase.
# 4. `title()`: Capitalizes the first character of each word in a string.
# 5. `strip()`: Removes leading and trailing whitespace from a string.
# 6. `replace(old, new)`: Replaces occurrences of a specified substring with another substring.
# 7. `split(separator)`: Splits a string into a list of substrings based on a specified separator.
# 8. `join(iterable)`: Joins elements of an iterable (like a list) into a single string, using a specified separator.
# Example usage of string methods:
# Example string
name = " Vaheeda Fatima " # Strings are immutable
a = len(name)
print(a) # Output: 13
print(name.upper()) # Output: VAHEEDA FATIMA
print(name.lower()) # Output: vaheeda fatima
print(name.capitalize()) # Output: Vaheeda fatima
print(name.title()) # Output: Vaheeda Fatima
print(name.strip()) # Output: Vaheeda Fatima
print(name.replace("Vaheeda", "Fatima")) # Output:  Fatima Fatima
print(name.split()) # Output: ['Vaheeda', 'Fatima']

name = " Vaheeda Fatima "
print(name.strip()) # Output: Vaheeda Fatima
print(name.lstrip()) # Output: Vaheeda Fatima
print(name.rstrip()) # Output:  Vaheeda Fatima

text = "python is great"
print(text.find("is")) # Output: 7
print(text.replace("great", "awesome")) # Output: python is awesome

text = "Apple, Banana, Cherry"
print(text.split(", ")) # Output: ['Apple', 'Banana', 'Cherry']
print(",".join(["Apple", "Banana", "Cherry"])) # Output: Apple, Banana, Cherry

# These string methods can be used to manipulate and format strings in various ways, making it easier to work with text data in Python.

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False