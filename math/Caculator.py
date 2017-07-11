#def calculator():
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def percentage(x,y):
    return x % y
def floordivision(x,y):
    return x//y
def exponent(x,y):
    return x**y

def calculator():
 print ("Welcome to calculator")
 print("Select operation.")
 print("1.Add")
 print("2.Subtract")
 print("3.Multiply")
 print("4.Divide")
 print("5.Percentage")
 print("6.Floor Division ")
 print("7.Exponent")
# Select choice
 choice = (input("Enter choice(1/2/3/4/5/6/7): "))
 while  not choice.isdigit():
    print("Entre only number")
    choice = (input("Enter choice(1/2/3/4/5/6/7): "))
    continue
# User input
 num1 = (input("Enter first number: "))
 while not num1.isdigit():
    print("Enter only number")
    num1 = (input("Re-enter first number: "))
    continue

 num2 = (input("Enter second number: "))
 while not num2.isdigit():
    print("Enter only number")
    num2 = (input("Re-enter second number: "))
    continue


 n1 = int(num1)
 n2 = int(num2)
 if choice == '1':
   print(num1,"+",num2,"=", add(n1,n2))

 elif choice == '2':
   print(num1,"-",num2,"=", subtract(n1,n2))

 elif choice == '3':
   print(num1,"*",num2,"=", multiply(n1,n2))

 elif choice == '4':
   print(num1,"/",num2,"=", divide(n1,n2))
 elif choice == '5':
    print((n1/n2)*100)
 elif choice == '6':
     print(n1//n2)
 elif choice == '7':
     print(n1**n2)
 else:
   print("Invalid input")

calculator()

user_choice = True
while user_choice:
 user_choice= input("Do you want calculate again? Please type y for yes and n for no: ")
 if user_choice == "n":
     print("Thanks for using")
     break
 elif user_choice == "y":
     print("Calculate again ")
     calculator()
 else:
     print("Please select correct choice")





