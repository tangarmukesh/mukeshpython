#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
#Write a function which is given the day number, and it returns the day name (a string).

weekday = int(input("Enter your number: "))
def dayName(weekday):
    '''This for weekdays'''
    if weekday == 0:
        return "Sunday"
    elif weekday == 1:
        return "Monday"
    elif weekday == 2:
        return "Tuesday"
    elif weekday == 3:
        return "Wednesday"
    elif weekday == 4:
        return "Thursday"
    elif weekday == 5:
        return "Friday"
    elif weekday == 6:
        return "Saturday"
    else:
        return "incorrect number"
print(dayName(weekday))
print(dayName.__doc__)
