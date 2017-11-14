'''a=5
b=5
if a>b:
    print("A is bigger",a)
    print("This is inside a block")
elif a==b:
    print("A and equal",a,b)
else:
    print("B is bigger",b)
num =int(input("Enter your number: "))
if num>5:
    print("Your number is bigger",num)
elif num==5:
    print("Your number is equal",num)
else:
    print("5 is bigger your number",num)
if num>7 and num<9:
    print("Your number is: ",num)
if num==4 or num==7:
    print("Your number is:",num)


num= int(input("Enter your num: "))
if num>5:
    if num<10:
        print("Num is bigger 5 and lesser 10",num)
    else:
        print("Num is equal or greater than 10",num)
elif num<5:
    if num == 1:
        print("Num is 1",num)
    elif num<1:
        print("Num is less than 1 ",num)
    else:
        print("num is bigger 1",num)
else:
    print("num equal to 5",num)
num= int(input("Enter you num: "))
if num%2==0:
    print("num is even",num)
else:
    print("num is odd",num)
num=int(input("Enter your num"))
if num%4==0:
    print("num is multiple of 4",num)
else:
    print("not multiple of 4",num)
day= input("Enter your day ")
dayname=['Sat','Sun']
if day in dayname:
    #if day !='Sat' and day!='Sun':
    #if day not in dayname:
    print("School is Close ",day)
else:
    print("School is open ",day)'''
    

'''num=[0,1,2,3,4,5,6,7]
for i in range(8):
    if i== 3 or i== 6:
        continue
    print(i)

for i in num:
    if i== 3 or i== 6:
        continue
    print(i)'''

'''i = 0
while i>=0 and i<100:
    i+= 1 
    print(i)
i =0
while i>=0:
    i+=1
    if i ==101:
        break
    print(i)
i=1
while True:
    i+=1
    if i ==101:
        break
    print(i)

i=1
while 1:
    i+=1
    if i ==101:
        break
    print(i)

for i in range(1001):
    if i==501:
        break
    print(i)

i = 0
while True:
    i+=1
    if i == 50:
        continue
    elif i ==101:
        break
    print(i,end=" ")

i=0
while True:
    i+=1
    if i == 50:
        continue
    elif i == 125:
        continue
    elif i == 175:
        continue
    elif i >201:
        break
    print(i,end=" ")

i= 0
while True:
    i+=1
    if i == 50 or i== 125 or i == 175:
        continue
    elif i >200:
        break
    print(i)
for i in range(1,501):
    if i%10==0:
        if i == 100 or i == 400:
            continue
        print(i,end=" ")

for i in range(10,501,10):
    if i == 100 or i == 400:
        continue
    print(i,end=" ")


for i in range(1,51):
    if i%3==0 and i%5==0:
        print("Multiple of both 3 and 5")
    elif i%3==0:
        print("Multiple of 3")
    elif i%5==0:
        print("Multiple of 5")
    print(i)

num = int(input("Enter your number: "))
x = [1,4,3,5,66,75,11,32]
y=[]
for i in x:
    if num>i:
        y.append(i)
print(y)

a=[1,2,33,45,6,3,3,6,7]
b=[2,22,3,45,5,6,7,5,7]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

a=[1,2,33,45,6,3,3,6,7]
b=[2,22,3,45,5,6,7,5,7]
c= []

z= set(a)
y=set (b)
for i in z:
    if i in y:
        c.append(i)
print(c)

a=[1,2,33,45,6,3,3,6,7]
b=[2,22,3,45,5,6,7,5,7]

z= set(a)
y=set (b)
x= z.intersection(y)
print(list(x))


a=[1,2,33,45,6,3,3,6,7]
b=[2,22,3,45,5,6,7,5,7]
c=[]

for i in a:
    if i not in b:
        c.append(i)
print(c)'''





































    
    





















    
    
    
    























    
















    
        







              
              
    























