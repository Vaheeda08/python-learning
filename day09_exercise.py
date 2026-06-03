# Day 09 - Exercise

# Question 1
from operator import index


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

# Question 7
name = "Vaheeda"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Question 8
name = "Vaheeda"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Question 9
sentence = "Python is a great programming language."
new = sentence.replace("Python", "Java")
print(new)

# Question 10
sentence = "Python is a great programming language."
ind = sentence.index("Python")
print(ind)

# Question 11
sentence = "Python is a great programming language."
print(sentence.upper())

# Question 12
sentence = "Python is a great programming language."
sum = 0
vowel = "aeiouAEIOU"
for char in sentence.lower():
    print(char)
    if (char in vowel):
        sum += 1
print(f"There are {sum} vowels in the sentence.")

# Question 13
string1 = "madam"
if(string1 == string1[::-1]):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")