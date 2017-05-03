#class math():
def add(x, y):
     sum = x + y
     return sum
a = (input("Enter first number: "))
while not a.isdigit():
    print("Enter only number")
    a = (input("Re-enter first number: "))
    continue
b = (input("Enter second number: "))
while not b.isdigit():
    print("Enter only number")
    b = (input("Re-enter second number: "))
    continue
num1 = int(a)
num2 = int(b)
print(a, "+", b, "=", sum(num1, num2))