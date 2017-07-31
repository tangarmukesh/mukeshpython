n = int(input("Enter your number here: "))
for i in range (1,10):
    if n == i:
        print("Great, you are win")
    elif n<1 or n >=10:
        print("Sorry, you missed")
        break
    else:
        pass



