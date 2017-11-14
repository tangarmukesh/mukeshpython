'''def testfunction():
    print("inner This is my first function:")

print("Outer function")
testfunction()'''

'''g_var = 1

def var_function():
    print("global varibale: ",g_var)
    l_var = 3
    print("local variable; ",l_var)

print("variable in function")
var_function()
print("global varibale: ",g_var)
print("local variable; ",l_var)

var1 = 4

def make_global():
    print(var1)
    global var2
    var2 = 7
    print(var2)

make_global()
print(var2)'''

'''def take_input(user):
    print(user)
take_input(12345)

def multi_arg(x,y,z):
    print(x,y,z)
multi_arg(12,54,7)

def multi_arg(x,y,z):
    print(x,y,z)
multi_arg(z=12,x=54,y=7)

def multi_arg(x,y,z= 23):
    print(x,y,z)
multi_arg(x=54,y=7)

def multi_arg(x=23,y=32,z=33):
    print(x,y,z)
multi_arg()
multi_arg(z=1)

def add(a,b):
    return a+b

a= 1
b= 5
sum = add(a,b)
print(sum)

def add(a,b):
    return
print(add(1,3))

n = int(input("Number: "))
for i in range (1,10):
    if n == i:
        print("pass")
    elif n<1 or n >=10:
        print("miss")
        break
    else:
        pass

def myfunction(user):
    print("user is ",user)
    user2 = input("Enter your name: ")
    print("user is",user2)
#user1 = input("Enter your name: ")
#myfunction("mukesh")
#myfunction("manish")
#myfunction(user1)
myfunction("a")

def mulitplearg(user,lang,sys):
    print("user is",user,"and lang",lang,"or system is",sys)
mulitplearg("mukesh","python","test")
mulitplearg(lang="mukesh",sys="python",user="test")

def mulitplearg(user,lang,sys = "window"):
    print("user is",user,"and lang",lang,"or system is",sys)
mulitplearg("manish","python")
mulitplearg("mukesh","c++","OS")

def mulitplearg(user="mukesh",lang="java",sys = "window"):
    print("user is",user,"and lang",lang,"or system is",sys)

mulitplearg()


def sum(a,b):
    return a+b
total = sum(3,6)
print("your sum is",total)


a =12
b = 15
print("my sum is",sum(a,b))

def sum(a,b):
    sum = a+b
    return
print("my sum is",sum(2,4))

def sum(a,b):
    if a<4:
        return
    return a+b
print("sum is",sum(2,6))
print("sum is",sum(7,6))


num = input("Enter your number: ")

def square(num):
    if  num.isdigit():
        num1 = int(num)
        return num1 * num1
    return "not correct"
print("square is ",square(num))

def my_max(x,y):
    if x>y:
        return x
    return y
print("Bigger number is ",my_max(5,7))
print("Bigger number is ",my_max(10,7))

def my_max(x,y):
    return max(x,y)
print("Bigger number is ",my_max(23,65))

def mylist(list):
    for i in list:
        print(i)
mylist([0.7,4,5,6])
print("item is ",mylist([1,2,3,4,5]))

def mylist(list):
    for i in range(len(list)-1,-1,-1):
        print(list[i])
mylist([1,2,3,4,5,6])


square = lambda x: x**2
print(square(6))

title = "My name is Mukesh"
try:
    print(tile)
except NameError as msg:
    print(msg)


day = 12

try:
    if day> 31:
        raise ValueError("Invalid day number")
    print("Day is less than 31",day)

except ValueError as msg:
    print(msg)

finally :
    print("We should use normal code here")

char= ["test","apple","python","gurgaon"]
def display(elem):
    assert type(elem) is int ,"Must be int"
    print(char[elem])

elem = 3
display(elem)'''

def display(s):
    '''This is doc string'''
    print(s)
print(display.__doc__)
    












































        

        
    






































    
