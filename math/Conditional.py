time = input("What is the time: ")
while not time.isdigit():
    print("Please enter time in number")
    time = input("What is the time: ")
    continue
t = int(time)
if t < 10:
  print("Breakfast Time")
elif t >= 12 and t < 17:
  print("Lunch Time")
elif t >= 17 and t< 20:
 print("Tea Time")
elif t >= 20 and t< 22:
 print("Dinner Time")
else:
    print("Rest Time")