#problem 3

""" In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000. """

#solution
def is_leap_year(year):
    return (year/4).is_integer() and not ((year/100).is_integer()) or (year/400).is_integer()