#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
elif number < 0:
    lastdigit = -1 * ((-1 * number) % 10)
print(f"Last digit of {number} is {lastdigit} and is", end=" ")
if lastdigit > 5:
    print("greater than 5")
elif lastdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
