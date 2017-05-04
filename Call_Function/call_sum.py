from Call_Function.sumclass import math
class callfunction(math):
    def usename(self):
        name = input("Enter username: ")
        print("Name is " + name)
        age = input("Enter your age: ")
        if int(age) > 18:
            print("Welcome" + age)
        else:
            math.sum(self)

callfunction.usename("hemant")