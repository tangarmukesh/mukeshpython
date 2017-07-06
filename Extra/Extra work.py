'''day = input("Enter your day: ").lower()
if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
    print("Today is", day, "and", day, "is working day")
elif day in ('saturday', 'sunday'):
    print("Today is", day, "and", day, "is not working & enjoy your day")
else:
    print("Enter wrong day")'''
day = input("Enter your day: ")
if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday'):
    if day in ('saturday', 'sunday'):
        print("Today is", day, "and", day, "is not working & enjoy your day")
    else:
        print("Today is", day, "and", day, "is working day")
else:
    print("You are enter wrong day")
