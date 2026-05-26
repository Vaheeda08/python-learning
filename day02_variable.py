# In Python, variables are used to store data that can be used and manipulated throughout a program. A variables is created the moment you assign a value to it using the assignment opertor (=)

age = 34 # integer
name = "Vaheeda" # string
cgpa = 4.55 # float

# Rules for defining a variable in python:
# 1. A variable name must start with a letter (a-z, A-Z) or an underscore (_).
# 2. A variable name cannot start with a number (e.g., 1age is invalid).
# 3. A variable name can only contain alphanumeric characters (letters and numbers) and underscores.
# 4. Variable names are case-sensitive (age and Age are different variables).
# Avoid using python reserved keywords as variable names (e.g., if, else, while, for, etc.)
# Example of invalid variable names:
# 1age = 30 # invalid because it starts with a number
age = 30 # valid — variable NAME starts with a letter, VALUE can be a number ✅ 
# 2name = "John" # invalid because it starts with a number
# @age = 30 # invalid because it starts with a special character

print(age, name, cgpa)
