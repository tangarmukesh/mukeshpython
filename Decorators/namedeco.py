'''def hi(name= "Mukesh"):
    return "Hi" + name
print(hi())

greet = hi
print(greet())
del hi
#print(hi())
print(greet())

def hi(name = "Mukesh"):
    print("now you are inside the hi function")

    def greet():
        return "now you are in the greet function"

    def welcome():
        return "now you are in the welcome function"

    print(greet())
    print(welcome())
    print("now you are back in the hi function")

hi()
greet()

def hi(name = "Mukesh"):
    def greet():
        return "now you are in the greet function"

    def welcome():
        return "now you are in welcomee function"

    if name == "manish":
        return greet
    else:
        return welcome
a = hi()
print(a)
print(a())
print(hi()())

def hi():
    return "hi Manish"

def dosomethingbeforehi(func):
    print("Doing something before hi")
    print(func())

dosomethingbeforehi(hi)


def a_new_decorator(a_func):

    def wrapTheFunction():
        print("interesting work before executing a_func")
        a_func()
        print("after work")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("function which need to decoration ")

a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("interesting work before executing a_func")
        a_func()
        print("after work")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("function which need to decoration ")

a_function_requiring_decoration()'''

from functools import wraps
def a_new_decorator(a_func):
    
    @wraps(a_func)
    def wrapTheFunction():
        print("interesting work before executing a_func")
        a_func()
        print("after work")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("function which need to decoration ")

a_function_requiring_decoration()

































