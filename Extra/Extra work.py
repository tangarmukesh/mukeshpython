num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
def divide(num1,num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("division by zero")
   # else:
        print("result is", result)
    finally:
        print("Pass")