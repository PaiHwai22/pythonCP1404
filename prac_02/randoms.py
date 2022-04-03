import random

print(random.randint(5, 20))  # line 1
# random integer generation, half inclusive from 5 to 20. smallest is 6, largest is 20.
print(random.randrange(3, 10, 2))  # line 2
# random integer between 3 and 10 but includes number only +2 to previous smaller number.
# The smallest number generated is 3 and the largest is 9.
# 4 could not be generated as it doesn't satisfy the conditions of the parameter.
print(random.uniform(2.5, 5.5))  # line 3
# generates an exclusive random float number between 2.5 and 5.5. The smallest number possible is 2.5

print(random.uniform(1, 100))  # prints random number, inclusive
