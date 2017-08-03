a = input("What is the time ")
if int(a) < 10:
  print("Breakfast Time")
elif int(a) >= 12 and int(a) < 17:
  print("Lunch Time")
elif int(a) >= 17 and int(a)< 20:
 print("Tea Time")
elif int(a) >= 20 and int(a)< 22:
 print("Dinner Time")
else:
    print("Rest Time")