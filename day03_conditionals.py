# In Python, Operators are used to perform operations on variables and values.

# if_statement

age=12

if(age>18):
    print("You are an adult.")
    print("You can vote.")


print("End of program.")
 
 # if_else_statement

age = int(input("Enter your age: "))

if(age>18):
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are a minor.")
    print("You cannot vote.")

print("End of program.")

# if_elif_else_statement

age = int(input("Enter your age: "))

if(age>18):
    print("You are an adult.")
    print("You can vote.")
elif(age==13):
    print("You are a teenager.")
else:
    print("You are a child.")
    print("You cannot vote.")

print("End of program.")
