# Day 05 - pass
# The pass statement is a null operation in Python. It does nothing when executed.
# It is used as a placeholder where syntactically some code is required but no action is desired.

for i in range(1, 10):
    if i == 5:
        pass #Do nothing when i is equal to 5
    print(i) #print 1-9 including 5, but when i is 5, it will not execute any code in the if block.