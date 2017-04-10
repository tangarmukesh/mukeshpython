num1 = input("Enter first number: ")
while not num1.isdigit():
    print("Enter only number")
    num1 = input("Re-enter first number: ")
    continue
num2 = input("Enter second number: ")
while not num2.isdigit():
    print("Enter only number")
    num2 = input("Re-enter second number: ")
    continue
num3 = input("Enter thrid number: ")
while not num3.isdigit():
    print("Enter only number")
    num3 = input("Re-enter thrid number: ")
    continue
n1 = int(num1)
n2 = int(num2)
n3 = int(num3)
if (n1%n2 == 0):
    print("A")
elif ((n1+n2)%n3 == 0):
    print("B")
else:
    print("Bye")

