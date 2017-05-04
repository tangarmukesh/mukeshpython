from Call_Function.sumclass import math
from math.charinput import user
from math.largest import lar
class callfunction(math):
    def usename(self):
        name = input("Enter username: ")
        print("Name is " + name)
        age = input("Enter your age: ")
        if int(age) == 18:
           #print("Welcome" + age)
           math.multi(self)
        elif int(age> 18) and (age==25) :
            user.username(self)
        else:
            lar.largestnumber(self)

callfunction.usename("hemant")