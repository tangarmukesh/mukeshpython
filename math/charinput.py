class user():
 def username(self):
   name = input("Name ")
   print("Name is " + name)
   age = input("Enter your age: ")
   if int (age) > 18:
    print("Welcome you are " + age)
   else:
    print("Not in house because you are below " + age)
    return user


