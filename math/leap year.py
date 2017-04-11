year = input("Enter year: ")
if year.isalpha():
 print("Enter only number")
 year = input("Enter year: ")
y = int(year)
if(y % 4) == 0:
    print("{0} is a leap year")
else:
    print("{0} is not a leap year")