'''i=0
while i<5:
    #i=i+1
    print(i)
    i=i+1
print("This is outside of loop")
j=5
while j>=0:
    print(j)
    j=j-1
a=1
while a<=50:
    print(a)
    a=a+1
z=10
y=1
while z<=100 and y<=10:   
    print(z,"*",y,"=",z)
    z=z+10
    y=y+1    
    
print((range(10)))
print(list(range(10)))
print(list(range(2,20,1)))
print(list(range(2,20,4)))
print(list(range(50,5,-1)))
print(list(range(50,5,3)))
for i in range (10,20,2):
    print(i*3)
for i in range (1,51):
    print(i)
for i in range (10,501,10):
    print(i)
for i in range (1000,2001):
    if i%7==0 and i%5==0:
        print(i)

mylist=[1,2,3,4]
mytuple=(5,6,7,8)
myset={1,2,3,4}
mydict={'a':1,'b':2,'c':3}
mystr="12"
for item in mylist:
    print(item)
for item in mytuple:
    print(item)
for item in myset:
    print(item)
for item in mystr:
    print(item)
for item in mydict:
    print(item)
for item in mydict.values():
    print(item)
for item in mydict.items():
    print(item)
for item,item1 in mydict.items():
    print("The key is",item, "and the value is ",item1)
for i in "Hello World":
    if i=="W" or i=="o":
        print(i)
#for i in enumerate(mylist):
   # print(i)
for i in zip (mylist,mytuple):
    print(i)'''
i=1
while i<4:
    print("\n outer loop",i)
    i=i+1

    j=1
    while j<5:
        print("\t inner loop",j)
        j=j+1
for i in range (1,10):
    for j in range (1,4):
        print(i,j)
for i in range(1,10):
    print("Item",i)
    if i ==3:
        break
for i in range (1,6):
    print(i)
    if i ==4:
        continue
for i in range (1,10):
    for j in range (1,6):
        if i<6 and j==5:
            print("item is both range: ")
            break
        print(i,j)
    
    
    


















































    
    


