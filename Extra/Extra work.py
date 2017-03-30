dog_age = (input("Enter dog age: "))
print("Pass")

if dog_age.isalpha:
    print("Enter only number " .format(dog_age))
    dog_age = (input("Re-enter dog age: "))

elif dog_age < 0:
    print("A")
elif dog_age > 2 and dog_age < 5:
    print("B")
else:
    print("Invalid number {}".format(dog_age))
    #dog_age = input("Again enter age: ")
