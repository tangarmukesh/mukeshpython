class lar():
    def largestnumber(self):
     a = int(input("Enter your first number: "))
     b = int(input("Enter your second number: "))
     c = int(input("Enter your thrid number: "))
     if(a>b) and (a>c):
      largest = a
      print("The largest number betwwen ", a, ",", b, "and", c, "is", largest)
     elif(b>a) and (b>c):
      largest = b
      print("The largest number betwwen ", a, ",", b, "and", c, "is", largest)
     else:
      largest = c
      print("The largest number betwwen ",a,",",b,"and",c,"is", largest)
      return lar

