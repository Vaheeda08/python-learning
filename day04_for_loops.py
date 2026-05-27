# In python, we can use loops to repeat a block of code multiple times. The two main types of loops are "for" loops and "while" loops.

print(1)
print(2)
print(3)

# This is a simple example of printing numbers from 1 to 3. However, if we want to print numbers from 1 to 100, it would be inefficient to write 100 print statements. Instead, we can use a loop.

for i in range(1, 101): #range function goes from 1 to 100 in this case.
    print(f"5 * {i} = {5 * i}")