weekday = input("Enter your day: ").lower()
task = input("Enter your task: ").upper()
if weekday == "monday":
   print ("Today is Monday and your task is",task)
elif weekday == "tuesday":
   print ("Today is Tuesday and your task is",task)
elif weekday == "wednesday":
   print ("Today is Wednesday and your task is",task)
elif weekday == "thursday":
   print ("Today is Thursday and your task is",task)
elif weekday == "friday":
   print ("Today is Friday and your task is",task)
elif weekday == "saturday":
   print ("Today is Saturday and your task is",task)
elif weekday == "sunday":
   print ("Today is Sunday and your task is",task)
else:
   print("You entered an invalid day.")
