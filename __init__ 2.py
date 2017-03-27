name = input("Enter your name: ")
while not name.isalpha():
    print("Enter only alpha:")
    name = input("Re-enter you name: ")
    continue
#if not 4<=len(name)<=7:
for name in range(4,7):
    print("Name must be more than 4 char and less than 7 char")
    name = input("Re-enter you name: ")
    break

    print("Hello " + name)

print("trsting")

