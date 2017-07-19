n = int(input("Enter your line number: "))

for x in range(n-1):
    print((n-x) * ' ' + (2*x+1) * '*')
for x in range(n-1, -1, -1):
    print((n-x) * ' ' + (2*x+1) * '*')