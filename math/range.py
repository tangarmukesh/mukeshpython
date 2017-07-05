#Write a program to read the number of notebook and print out the cost.

notebook= (input("Enter number of notebook: "))
while not notebook.isdigit():
    print("Enter only number ")
    notebook= (input("Enter number of notebook: "))
    continue
n = int(notebook)
if n > 0 and n <= 100:
    cost = n * 5
    print(cost)
elif n > 100 and n <= 300:
    cost = 100 * 5
    extranotebook= n - 50
    cost = extranotebook * 4 + cost
    print(cost)
elif n > 300:
    cost = 100 * 5
    cost = 200 * 4 + cost
    extranotebook= n - 300
    cost = extranotebook * 3 + cost
    print(cost)
else:
    print("Not available")