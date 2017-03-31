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

print ("Welcome to calculator")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Percentage")
# Select choice
choice = input("Enter choice(1/2/3/4/5): ".format("choice"))
while  not choice.isdigit():
    print("Entre only number")
    choice = input("Enter choice(1/2/3/4/5): ".format("choice"))
    break
# User input
num1 = (input("Enter first number: ".format("num1")))

while not num1.isdigit():
    print("Enter only number")
    num1 = input("Re-enter first number: ".format("num1"))
    break
num2 = (input("Enter second number: ".format("num2")))
while not num2.isdigit():
    print("Enter only number")
    num1 = input("Re-enter second number: ".format("num2"))
    break



if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
    print((num1/num2)*100)
else:
   print("Invalid input")

