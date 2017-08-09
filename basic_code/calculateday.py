#Write a Python program to calculate number of days between two dates.
from datetime import date
from basic_code import calendar
#f_date = (input("Enter your first date: "))
#l_date = (input("Enter your last date: "))
f_date = date(2014, 2, 2)
l_date = date(2014, 7, 11)
days = l_date - f_date
print(days)
calendar()