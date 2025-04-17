# Write a program that reads a year from the user and tells whether a given year is a leap year or not.
def main():
    year = int(input("Please input a year:"))

# In the Gregorian calendar, three criteria must be checked to identify leap years:
# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
    if year % 4 == 0:
        if year % 100 == 0:
          if year % 400 == 0:
             print("That's a leap year!")
          else:
              print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")
main()