# Day 09 - Exercise

# Question 1
name = "Vaheeda"
print(name[0])
print(name[-1])
print(len(name))

# Question 2
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
print(str1,str2)

# Question 3
test = "Python Programming"
print(test[0:6])
print(test[-6:6])
print(test[::2])

# Question 4
text = "Python Programming"
print(text[::-1])

# Question 5
text = " i love python programming "
print(text.strip())
print(text.title())
print(text.count("o"))

# Question 6
str1 = "123abc"
if str1.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")