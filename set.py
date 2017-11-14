'''a={'Test','Mukesh','Manish','Python'}
print(a)
print(type(a))
print(len(a))
b={'Dev',1,'Dev','Test'}
print(b)
a.add('My test')
print(a)
a.update('Tangar')
print(a)
a.update(b)
print(a)
a.update(['Tangar'])
print(a)
x=a.copy()
print(x)
y=a.pop()
print(a)
print(y)
a.discard('T')
print(a)
a.discard('T')
print(a)
z=a.intersection(b)
print(z)
t=a.difference(b)
print(t)
x=set()
print(x)
print(type(x))
mylist=[1,5,'Python','Gurgaon',5]
mytuple=('Mukesh','Manish',3,4,6,3)
a=set(mylist)
b=set(mytuple)
print(a)
print(b)
x=list(a)
y=tuple(b)
print(x)
print(y)
c=(a)
n=[b]
print(c)
print(n)
print(type(c))
print(type(n))
n[0]=list(n[0])
print(n)
print(list(set(mylist)))
x1=list(set(mylist))
d=frozenset()
print(d)
print(type(d))
mylist={1,5,'Python','Gurgaon',5}
f=frozenset(mylist)
print(f)
#f.add('Test') frozenset unmuteable
print(5 in mylist)
print(30 in  mylist)
print(5 not in mylist)
print(30 not in  mylist)
mydict={'1':'4','a':'6','v':'b'}
print(mydict)
print(type(mydict))
print(len(mydict))
mydict['a']= 'Test'
print(mydict)
print(mydict['v'])
mydict['2']= 4
print(mydict)
mydict['3']= ['1',2,3]
print(mydict)
print(mydict['3'][1])
mydict['3'].append('My first')
print(mydict)
del mydict['1']
print(mydict)
#y= del mydict['2']
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(sorted(mydict.keys()))
print(sorted(mydict))
#print(sorted(mydict.values()))
#print(sorted(mydict.items()))
print('3' in mydict)
print('3' in mydict.values())
saleitem={'Milk':20,'Apple':25,4:50,'A':''}
print(saleitem.get('Milk',30))
print(saleitem.get('food',30))
saleitem.setdefault('Milk',30)
print(saleitem)
saleitem.setdefault('food',30)
print(saleitem)'''












































































































