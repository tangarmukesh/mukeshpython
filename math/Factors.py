num= input("Enter your number: ")
while not num.isdigit():
   print("Please enter only number")
   num= input("Enter your number: ")
   continue
n = int(num)
for i in range(1, n + 1):
        if n % i == 0:
            print(i);
