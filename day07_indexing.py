# Day 07 - Indexing
# Indexing is a powerful technique in Python that allows you to access specific elements of a sequence, such as a string, list, or tuple.
# In Python, indexing starts at 0, which means the first element
# of a sequence is accessed with index 0, the second element with index 1, and so on
# You can also use negative indexing to access elements from the end of the sequence. For example, -1 refers to the last element, -2 refers to the second-to-last element, and so on.

# Example of indexing with a string
name = "Vaheeda"

#name = "V a h e e d a"
#        0 1 2 3 4 5 6
#       -7-6-5-4-3-2-1
print(name[0])  # Output: V
print(name[1])  # Output: a
print(name[2])  # Output: h
print(name[3])  # Output: e
print(name[4])  # Output: e
print(name[5])  # Output: d
print(name[6])  # Output: a

print(name[-1])  # Output: a
print(name[-2])  # Output: d
print(name[-3])  # Output: e
print(name[-4])  # Output: e
print(name[-5])  # Output: h
print(name[-6])  # Output: a
print(name[-7])  # Output: V