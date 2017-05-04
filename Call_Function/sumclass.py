class math():
 def sum(self):
     a = (input("Enter first number: "))
     b = (input("Enter second number: "))
     sum = int(a) + int(b)
     if sum > 20:
      print(a, "+", b, "=", sum)
     else:
         math.multi(self)
     return sum

 def multi(self):
      a = (input("Enter first number: "))
      b = (input("Enter second number: "))
      multi = int(a) * int(b)
      print(a, "*", b, "=", multi)
      return multi





