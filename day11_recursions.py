# Day 11 - Recursions
# A recursive function is a function that calls itself in order to solve a problem. It typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

'''
0 1 1 2 3 4 5 6 7 8 9
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-2) + fib(n-1) for n > 1
'''

def fib(n):
    # Base case: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(6))

print(fib(3) + fib(2))
print(fib(2) + fib(1) + fib(1) + fib(0))
0 + 1 + 1 + 0 + fib(1) + fib(0) + fib(0)