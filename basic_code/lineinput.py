#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
lines = []
while True:
    l = input("Enter your line: ")
    if l:
        lines.append(l.lower())
    else:
        break;

for l in lines:
    print(l,end=" ")