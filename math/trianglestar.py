num = int(input("What is your height: "))
count = 1
space_count = num
for rows in range (num):
    for spaces in range (space_count):
        print(end=' ')
    for stars in range (count):
        print ("*", end=' ')
    space_count = space_count - 1
    count = count + 1

    print()