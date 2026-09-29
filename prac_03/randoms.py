# Saw the numbers 13, 17, 14 and 11
# Smallest number was 5 and the largest is 20

# Saw 7, 9, 3 and 5
# Smallest number could be a 3 and the largest could be a 9
# No

# 3.26893402161196, 4.282212737418481, 2.5595443158914333, 3.3535077639667232
# Smallest could be a 2.5, largest could be a 5.5
import random
print(random.randint(1, 100))

"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format() (don't do this unless you need to):
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# And with f-string formatting, introduced in Python 3.6 (do this)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))  # str.format version
print(f"My {name} would cost ${cost:,.2f}")  # preferred f-string version

# Aligning columns by using width after the :
# This loop uses enumerate, which is useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# TODO: Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about {cost}")

# TODO: Using a for loop with the range function and f-string formatting,
# produce the following right-aligned output (DO NOT use a list):
# 2 ^ 0 is    1
# 2 ^ 1 is    2
# 2 ^ 2 is    4
# 2 ^ 3 is    8
# 2 ^ 4 is   16
# 2 ^ 5 is   32
# 2 ^ 6 is   64
# 2 ^ 7 is  128
# 2 ^ 8 is  256
# 2 ^ 9 is  512
# 2 ^10 is 1024
for i in range(0, 11):
    print(f"2 ^ {i:2} is {2 ** i:4}")