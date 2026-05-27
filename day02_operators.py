# Day 02 - Operators in Python

a = 34

b = 7

# Arithmetic Operators
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)

# Comparison Operators
print(a>4) 
print(a<4)
print(a<=4)
print(a>=4)
print(a==4) #Is a equal to 4?
print(a!=4) #Is a not equal to 4?

# Logical Operators

c = True
d = False
print(c and d) #Logical AND
print(c or d) #Logical OR
print(not c) #Logical NOT

print(True and True) 
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# Assignment Operators
a = 32
print(a)
a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
a //= 2
print(a)
a **= 2
print(a)

# Membership Operators
a = [1, 2, 3, 4, 5]
print(3 in a) #Is 3 in the list a?
print(6 in a) #Is 6 in the list a?
print(3 not in a) #Is 3 not in the list a?
print(6 not in a) #Is 6 not in the list a?

#Identity Operators
x = 5
y = 5
print(x is y) #Is x the same object as y?
print(x is not y) #Is x not the same object as y?
