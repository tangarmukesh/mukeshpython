a = input("Enter your first number: ")
b = input("Enter your second number: ")
c = input("Enter your thrid number: ")
if(a>b) and (a<c):
    largest = a
elif(b>a) and (b<c):
    largest = b
else:
    largest = c
print("The largest number betwwen ",a,",",b,"and",c,"is", largest)
