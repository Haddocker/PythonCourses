# On every year that is divisible by 4 with no remainder.
# EXCEPT every year that is evenly divisible by 100 with no remainder.
# UNLESS the year is also divisible by 400 with no remainder.

year = int(input("Insert a year: "))

if year / 4 % 2 == 1:
    print("Not a leap year.")
else:
    if