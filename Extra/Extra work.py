n = 0
x = int(input("Enter your lines: "))
for x in range (0,x):
    n = n + 1
    for a in range (0, n-1):
        print ('*', end = '')
    print()
for b in range (0,x):
    n = n - 1
    for d in range (0, n):
        print ('*', end = '')
    print()
print ('')