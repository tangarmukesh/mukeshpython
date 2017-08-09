#Write a general version of the program which asks for the starting day number, and the length of your stay,
# and it will tell you the name of day of the week you will return on.

days = int(input("Enter your start day: "))
sleep = int(input("Enter number of sleep: "))

def which_day(start, sleep):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    return days[(start + sleep) % 7]


print(which_day(days, sleep))
