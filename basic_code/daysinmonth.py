#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years


months_in_year = int(input("Enter your year: "))
days_in_month = int(input("Enter month number: "))

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4,6,9,11):
        return 30
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return "Invaild month"


print(daysInMonth(months_in_year,days_in_month))