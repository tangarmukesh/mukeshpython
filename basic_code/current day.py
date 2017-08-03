import datetime

def daynamefromweekdays(weekday):
    weekday = datetime.date.today().strftime("%A")
    if weekday == "Monday":
        print ("Test")
    elif weekday == "Tuesday":
        print ("Test1")
    elif weekday == "Wednesday":
        print ("Test2")
    elif weekday == "Thursday":
        print ("Test3")
    elif weekday == "Friday":
        print ("Test4")
    elif weekday == "Saturday":
        print ("Test5")
    elif weekday == "Sunday":
        print ("Test6")
    else:
        print("Invalid")
daynamefromweekdays(2)



