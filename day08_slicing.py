# Day 08 - Slicing
# Slicing is a powerful feature in Python that allows you to extract a portion of a sequence (like a list, string, or tuple) by specifying a start index, an end index, and an optional step.
# The syntax for slicing is: sequence[start:stop:step]
# Example with a list

name = "Vaheeda"

print(name[0:2])  # goes from 0 to 2-1 (2 is not included)

print(name[2:-1])  # Same as name [2:4]

print(name[0:10:1])  # skip n-1 characters 
print(name[0:10:2])  # skip 1 character
print(name[0:10:3])  # skip 2 characters

print(name[:4]) # Replace the first empty number with 0
print(name[1:5]) # Replace the second empty number with the length #name[1:5]