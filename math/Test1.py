num1 = input("Enter first number: ")
x = num1.replace(" ","")
while not x.isdigit():
    print("Enter only number")
    num1 = input("Enter first number: ")
    x = num1.replace(" ", "")
num2 = input("Enter second number: ")
y = num2.replace(" ","")
while not y.isdigit():
    print("Enter only number")
    num2 = input("Enter second number: ")
n1 = int(x)
n2 = int(y)
if n1 % 4 == 0:
    print(n1, "is a multiple of 4")
elif n1 % 5 == 0:
    print(n1, "is a multiple of 5")
elif n1 % 2 == 0:
    print(n1, "is an even number")
else:
    print(n1, "is an odd number")

if (n1 + n2) % (n1 - n2) == 0:
    print("Hello")
else:
    print("Bye")
if num2 == 0:
    print("Not Divide")

elif n1 % n2 == 0:
    print(n1, "divides evenly by", n2)
else:
    print(n1, "does not divide evenly by", n2)