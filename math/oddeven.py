num = (input("Enter a number: "))
while not num.isdigit():
    print("Please enter only digit")
    num = (input("Re-enter your number:  "))
    continue
n1 = int(num)
mod = (n1 % 2)
if mod != 0: # mod != 0
    print("Odd number")
else:
    print("Even number")