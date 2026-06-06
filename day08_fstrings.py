# Day 08 - String Formatting with f-strings
# F-strings are a way to format strings in Python. They are a more concise and readable way to format strings than the older .format() method.
# To create an f-string, you simply prefix the string with the letter 'f' or 'F' and then use curly braces {} to include expressions that will be evaluated and included in the string.

template = "Dear {name}, You are awesome. Take this {amount} bag of money as a gift from me. Best, Your friend" # template string with placeholders [{name}, {amount}]
a = "Koina"
a1 = "1000$"
b = "Katherine"
b1 = "500$"
c = "Caroline"
c1 = "200$"

# Using f-strings to format the string with variables

s1 = template.format(name=a, amount=a1)
print(s1)

print(f"Dear {a}, You are awesome. Take this {a1} bag of money as a gift from me. Best, Your friend")
print(f"Dear {b}, You are awesome. Take this {b1} bag of money as a gift from me. Best, Your friend")
print(f"Dear {c}, You are awesome. Take this {c1} bag of money as a gift from me. Best, Your friend")