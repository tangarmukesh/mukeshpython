def factorial():
 num = input("Enter your number: ")
 num1 = num.replace(" ", "")
 while not num1.isdigit():
        print("Please enter only positive number")
        num = input("Enter your number: ")
        num1 = num.replace(" ", "")
        continue
 n = int(num1)
 factorial = 1
 if n == 0:
        print("factorial of 0 is 1")
 else:
     for i in range(1, n + 1):
        factorial = factorial * i
        print(i,"factorial of every step is", i, factorial)
 print("The factorial of", n, "is", factorial)
factorial()
x=True
while x:
   x = input("Do you want using again? Please type y for yes and n for no: ")
   if x == "n":
    print("Thanks for using")
    break
   elif x == "y":
    print("Welcome again ")
    factorial()
   else:
    print("Please select correct  in choice")