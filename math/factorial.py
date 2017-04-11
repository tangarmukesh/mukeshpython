def factorial():
 num = (input("Enter your number: "))
 n1 = num.replace(" ","")
 while not n1.isdigit():
  print("Enter only number")
  n1 = (input("Re-enter your number: "))
#def factorial():
 n= int(n1)
 factorial = 1
 if n < 0:
  print("Sorry, factorial does not exist for negative numbers")
 elif n == 0:
   print("The factorial of 0 is 1")
 else:
  for i in range(1,n + 1):
   factorial = factorial*i
  print("The factorial of",n,"is",factorial)

factorial()

num1 = True
while num1:
    num1 = input("Do you want using again? Please type y for yes and n for no: ")
    if num1 == "n":
        print("Thanks for using")
        break
    elif num1 == "y":
        print("Welcome again ")
        factorial()
    else:
           print("Please select correct  in choice")
