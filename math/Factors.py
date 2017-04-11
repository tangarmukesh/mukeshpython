def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i);


# Input from the user

num = int(input("Enter a number:"))
print("\nFactors of given number are:")
print_factors(num)