'''file = open("example.txt","w")
print("file name",file.name)
print("file open mode",file.mode)

print("file is readable",file.readable())
print("file is writeable",file.writable())

def get_status(x):
    if (x.closed == True):
        print("File is close")
    else:
       print("File is open")
get_status(file)
file.close()
get_status(file)

line = "hi this is for testing\n"
line1 = "my first file program\n"
line2 = "my first python code\n"
line3 = "Hi my name is Mukesh\n"
line4 = "Me and manish write python code\n"

string = line+line1+line2+line3+line4
print(string)

mylist = [line,line1,line2,line3,line4]
print(mylist)
file = open("example.txt","w")
file.write(string)
file.close()

file = open("example2.txt","w")
file.writelines(mylist)
file.close()

file = open('example.txt','a')
file.write("Add this in example file")
file.close()

file = open('example.txt','r')
print(file.read())
file.close()

file = open('example.txt','r')
for line in file:
    print(line,end='')
file.close()

file = open('example.txt','r')
firstline = file.readline()
print("This is for first line:",firstline)
secondline = file.readline()
print("This is for second line:",secondline)
file.close()

file = open('example.txt','r')
all_lines = file.readlines()
print(all_lines)
print(len(all_lines))
print("Read line number 3: ",all_lines[3])
file.close

file = open('example.txt','r')
all_lines = file.readlines()
length = len(all_lines)
file.close()
file = open('example.txt','r')
for line in range (length):
    firstline= file.readline()
    print("This is first line of file:",firstline)
file.close()


file = open('example.txt','r')
all_lines= file.readlines()
length = len(all_lines)
for line in range (length):
    print("This is for line",line,"Txt is ",all_lines[line])

for line in range (length):
    print("This is for line",line+1,"Txt is ",all_lines[line])
file.close()

text = "This is for with keyword testing"

with open('example.txt','w') as file:
    file.write(text)
    print("is file closed: ",file.closed)
print("is file closed: ",file.closed)


with open('example.txt','r+') as file:
    text = file.read()
    print(text)
    print("Position if file now:",file.tell())

    file.seek(15)
    print("verify positon of file now.",file.tell())

    file.seek(25)
    file.write('write from 25')
    print("verify positon of file now.",file.tell())

    file.seek(15)
    print("verify positon of file now.",file.tell())

    test = file.read()
    print("Read file data",test)

    file.seek(0)
    test = file.read()
    print("Read file data in starting",test)'''

import os
if os.path.exists('example.txt'):
    file = open)

















































