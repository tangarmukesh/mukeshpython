num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 4 == 0:
    print(num1, "is a multiple of 4")
elif num1 % 5 == 0:
    print(num1, "is a multiple of 5")
elif num1 % 2 == 0:
    print(num1, "is an even number")
else:
    print(num1, "is an odd number")

if (num1 + num2) % (num1 - num2) == 1:
    print("Hello")
else:
    print("Bye")
if num2 == 0:
    print("Not Divide")

elif num1 % num2 == 0:
    print(num1, "divides evenly by", num2)
else:
    print(num1, "does not divide evenly by", num2)    