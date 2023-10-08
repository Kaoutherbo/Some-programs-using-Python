def is_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It's a leap year.")
    else:
        print("It's not a leap year.")

is_leap_year()
