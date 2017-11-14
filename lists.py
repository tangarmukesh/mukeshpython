'''num=[1,2,34,5]
print(num)
print(type(num))
print(num[0])
print(num[3])
#print(num[4])
mix=[2,23.4,'python',True,None,2+2j]
print(mix)
print(type(mix))
print(mix[-1])
print(mix[-6])
print(len(mix))
print(mix[-len(mix)])
print(mix[len(mix)-1])
a='hello'
print(a[0])
#a[0]='y'
#print(a[0])
a=['test','mukesh','manish','python']
#print(a)
#print(type(a))
#print(a[1])
#print(a[1][0])
#a[0]='python'
#print(a)
a.append('mytest')
print(a)
a.insert(1,'Gurgaon')
print(a)
a.insert(500,'Dev')
print(a)
print(len(a))
x=a.index('manish')
print(x)
a.append('manish')
print(a)
print(x)
y=a.index('manish')
print(y)
z=a.count('manish')
print(z)
a.remove('manish')
print(a)
a.pop(0)
print(a)
p=a.pop(4)
print(p)
print(a)
a.pop()
print(a)
#a.pop(700)
#print(a) existing index only
a.sort()
print(a)
b=[1,2,33,4,4,84,23,571,11,10]
#b.sort()
print(b)
c=['12','32','10','4']
#c.sort()
print(c)
z=['11','4','test','python','100']
#z.sort()
print(z)
#r=[12,'test',10,'mukesh',2,'1']
#r.sort() sort only same datatypes
#print()
b=[1,2,33,4,4,84,23,571,11,10]
#b.reverse()
print(b)
c.extend(b)
print(c)
print(type(c[0]))
print(type(c[10]))
del b[1]
print(b)
#f=del b[0] can't be assign del value
print(b[1:4])
print(b[2:3])
print(b[0:2])
print(b[:2])
print(b[3:])
print(b[3:8])
print(b[:])
print(b[1:5])
print(b[1:5:1])
print(b[1:5:2])
print(b[:5:2])
print(b[::2])
del b[1:3]
print(b)
del b[:]
print(b)
b.append(c)
print(b)
del b
print(b)
a=(11,1,2,33,44,5,2)
print(a)
print(type(a))
b=[1,
   22,
   31,
   1,
   2]
print(b)
print(a[3])
print(a[2:200])
#a[1]= 79 can't perform actions
#print(a)
#del a[1:3]
#print(a)
#del a tuple can be delete able
#print(a)
t=tuple()
print(t)
print(type(t))
t2=()
print(t2)
print(type(t2))
e= tuple(b)
print(e)
print(type(e))
f= list()
print(f)
print(type(f))
f2=[]
print(f2)
print(type(f2))
d= list(a)
print(d)
print(type(d))
#a=list()
#print(a)
e,r,t,s,y,u,i=a
print(e,r,t,s,y,u,i)
m=1
k=3
t3=(m,k)
t4=[m,k]
print(t3)
print(type(t3))
print(t4)
print(type(t4))
q,a,z,s,d=b
print(q,a,z,s,d)'''
#print(type(q,a,z,s,d)) type only one datatype
h='my first'
#l=h
#print(l)
q,w,e,r,t,u,b,c=h
print(q,w,e,r,t,u,b,c)


















































