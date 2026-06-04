# Day 10 - Lambda Functions
# Lambda functions are anonymous functions that can be defined in a single line. They are often used for short, simple functions that are not reused elsewhere in the code.

# Syntax: lambda arguments: expression

# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2: A lambda function that squares a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Example 3: A lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True
print(is_even(7))  # Output: False

# Example 4: Using a lambda function with the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 5: Using a lambda function with the filter() function to filter out even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example 6: Using a lambda function with the sorted() function to sort a list of tuples based on the second element
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# Example 7: Using a lambda function with the reduce() function to calculate the product of a list of numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Example 8: Using a lambda function to create a simple function that returns the length of a string
length = lambda s: len(s)
print(length("Hello, World!"))  # Output: 13

# Example 9: Using a lambda function to create a simple function that checks if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# Example 10: Using a lambda function to create a simple function that converts a temperature from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(25))  # Output: 77.0