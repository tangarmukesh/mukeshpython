inputString = input("Please type a sentence: ").lower()
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0


if  a in inputString :
     acount = acount + 1

if  e in inputString :
     ecount = ecount + 1

if  i in inputString :
    icount = icount + 1

if o  in inputString :
     ocount = ocount + 1

if u  in inputString :
     ucount = ucount + 1
totalcount= acount+ecount+icount+ocount+ucount

print(acount, ecount, icount, ocount, ucount)
print(totalcount)