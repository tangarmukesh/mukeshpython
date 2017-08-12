x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your thrid number: "))
def max_of_three( x, y,z ):
    if x > y > z:
        return x
    elif y > z:
        return y
    elif z > x:
        return z
    else:
        return "All numbers are equal"
    return z
print("largest number is: ",max_of_three(x,y,z))
