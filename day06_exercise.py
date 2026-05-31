# Day 06 - Exercise

# Question 1
from re import match


for i in range(1, 11):
    print(f"56 x {i:2} = {56 * i:3}")

# Question 2
num = int(input("Enter a number: "))
print(num)

if(num<0):
    print("Negative")

elif(num>0):
    print("Positive")

else:
    print("Zero")

# Question 3
age = int(input("Enter your age: "))

if (age>=18):
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")

# Question 4
num = int(input("Enter a number\n"))

if(num%2==0):
    print("Even")

else:
    print("Odd")

# Question 5
num = int(input("Enter a number\n"))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")

# Question 6
num = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose an operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"{num} + {num2} = {num + num2}")
    case "-":
        print(f"{num} - {num2} = {num - num2}")
    case "*":
        print(f"{num} * {num2} = {num * num2}")
    case "/":
        if(num2!=0):
            print(f"{num} / {num2} = {num / num2}")
        else:
            print("Cannot divide by zero.")
# Question 7
for i in range(1, 11):
        print(i)

# Question 8
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# Question 9
sum = 0
for i in range(1, 101):
    sum += i

print("The sum of the first 100 natural numbers is:", sum)

# Question 10
'''
Print the following pattern
*
**
***
****
*****
'''

for i in range(1, 6):
    print("*" * i)

# Question 11
sum = 0 
i = 1

while i <= 100:
    sum += i
    i += 1

print(sum)  

# Question 12
password = "Y2k123"
entered_password = input("Enter the password: ")

while entered_password != password:
    print("Incorrect password. Try again.")

entered_password = input("Enter the password: ")
print("Access granted.")

# Question 13
num = 45222


print(int(str(num)[::-1]))

# Question 14
for i in range(1, 11):
    if (i == 7):
        break
    print(i)
    