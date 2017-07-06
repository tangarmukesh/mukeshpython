year = input("Enter year: ")
year1 = year.replace(" ","")
while not year1.isdigit():
 print("Enter only number")
 year = input("Enter year: ")
 year1 = year.replace(" ","")
y = int(year1)
if(y % 4) == 0:
    print(year1,"is a leap year")
else:
    print(year1,"is not a leap year")