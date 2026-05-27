# Day 03 - Match Case
# Match case is a new feature in Python 3.10 that allows you to match a value against a pattern and execute code based on the match.

a = int(input("Enter a lucky number between 1 and 10: "))

match a:
    case 1:
        print("you won a car")
    case 3:
        print("you won a bike")
    case 6:
        print("you won a laptop")
    case _:
        print("better luck next time")