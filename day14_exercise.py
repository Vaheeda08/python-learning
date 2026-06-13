# Day 14 - Exercise

# Question 1
def greet():
    print("Hello, Python Learner!")

greet()

# Question 2
def square(x):
    return x*x

print(square(3))
print(square(5))
print(square(2))

# Question 3
def full_name(first, last):
    return f"{first} {last}"

print(full_name("John", "Doe"))

# Question 4
def calculate_area(length, Width=10):
    return length * Width

print(f"The area of this rectangle is {calculate_area(13, 20)}")
print(calculate_area(13))

# Question 5
add = lambda a, b: a + b

print(add(3, 5))

# Question 6
square = lambda x: x*x
numbers = [1, 2, 3, 4, 5]

print(list(map(square, numbers)))

# Question 7
def factorial(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(0))

# Question 8

8:19