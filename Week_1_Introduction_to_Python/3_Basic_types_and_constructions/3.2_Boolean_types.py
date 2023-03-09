#-----------------------------------------------------------------------
# bool types of variables
#-----------------------------------------------------------------------
  
print(13 == 13)
print(1 != 2)

print("\n")
print(3 > 4)
print(3 <= 3)
print(6 >= 6)
print(6 < 5)

print ("\n")
x = 2
print(1 < x < 3)

print("\n")
x, y, z = True, False, True
print(x and y)
print(x or y)
print(not y)
result = x and y or z
print(result)

# Is it a leap year?
print("\nIs it a leap year?")
year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

# or
import calendar
print(calendar.isleap(1980))






