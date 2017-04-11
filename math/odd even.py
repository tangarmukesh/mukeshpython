num = int(input("Enter a number: "))
if num.isdigit():
    print("Please enter only digit")
    num = int(input("Re-enter your number:  "))
mod = (num % 2)
if mod > 0:
    print("Odd number")
else:
    print("Even number")