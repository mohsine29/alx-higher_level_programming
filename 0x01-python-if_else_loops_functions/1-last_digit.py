#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if number < 0:
    x = -x
print(f"Last digit of {number} is {x}", end=" ")
if x > 5:
    print("and is greater than 5")
elif x == 0:
    print("and is 0")
elif x < 6 and x != 0:
    print("and is less than 6 and not 0")
