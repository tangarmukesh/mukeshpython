'''from bird import *
print(Bird.__doc__)
polly = Bird('Squawk')
print(id(polly))
print(polly.count)
print(polly.talk())
harry = Bird('Test,test1')
print(id(harry))
print(harry.count)
print(harry.talk())
chick = Bird('cheep')
chick.age = '1 week'
print(chick.talk())
print(chick.count)
print(chick.age)
#print(harry.age)
chick.age = '2 weeks'
print(chick.age)
setattr(chick,'age','4 weeks')
print(chick.age)
print(getattr(chick,'age'))
print(hasattr(chick,'age'))
delattr(chick,'age')
print(hasattr(chick,'age'))
zola = Bird('Beep.Beep')
print(dir(zola))
for i in dir(zola):
    if i[0] == '_':
        print(i)

# class dictionary
for i in Bird.__dict__:
    print(i,Bird.__dict__[i])
    
for i in zola.__dict__:
    print(i,zola.__dict__[i])


from songbird import *
bird_1 = Songbird('Testname','Testsong')
print(bird_1.name,bird_1.song)
print(id(bird_1))

del bird_1

testbird = Songbird('Dev','devsong')
print(testbird.name,testbird.song)
print(id(testbird))

mybird = Songbird('mybird','birdsong')
print(mybird.name,mybird.song)
print(id(mybird))

del testbird
del mybird

from polygon import *
rect = Rectangle()
tri = Triangle()
rect.set_values(4,6)
rect.set_values(4,6)
print('Rectangle area',rect.area())
print('Triangle area',tri.area())


from person import *
guy1 = Man('Mukesh')
guy2 = Woman('Lady')

guy1.speak()
guy2.speak()
Person.speak(guy2)
Person.speak(guy1)

from duck import *
donald = Duck()
mickey = Mouse()

donald.talk()
donald.coat()
mickey.talk()
mickey.coat()'''


import random
'''num1 = random.randint(1,50)
print(num1)


while 1:
    num2 = random.randint(5,60)
    print(num2)
    if num2 == 40:
        break


num3 = random.random()
print(num3)

num4 = random.random()*10
print(num4)

num5 = random.randrange(10)
print(num5)

num6 = random.randrange(1,10)
print(num6)

num7 = random.randrange(1,100,10)
print(num7)



numlist= [1,3,22,66,77,44,2]
mychoice= random.choice(numlist)
print(mychoice)

mystring = "Python"
mychar = random.choice(mystring)
print(mychar)

numlist = [1,23,3,54,22,88]
random.shuffle(numlist)
print(numlist)'''


num = random.sample(range(10,100),5)
print(num)


















































































































