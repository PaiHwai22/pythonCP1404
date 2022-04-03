"""Displays all numbers between 1 and 20"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""Counts from 0 to 100 in 10s"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""Counts down from 20 to 1"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""Ask user for number of stars and print """
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()

"""Print lines of increasing stars to the user's input amount"""
stars = int(input("Number of stars: "))
if stars > 0:
    k = 0
    for i in range(0, stars):
        k = k + 1
        for j in range(0, k):
            print("*", end="")
        print()
