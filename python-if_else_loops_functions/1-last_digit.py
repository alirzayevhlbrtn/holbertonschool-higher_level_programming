#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = str(number)
if number > 0:
    lastdigit = int(strnum[-1])
elif number < 0:
    lastdigit = -1 * int(strnum[-1])
print(f"Last digit of {number} is {lastdigit}", end=" ")
if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print("and is less than 6 and not 0")
