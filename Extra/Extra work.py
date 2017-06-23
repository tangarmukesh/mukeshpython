# message= "My name is Mukesh Tangar".lower()
message = input("Enter your message: ")
item = input("Enter your search item: ")
mydict = {}
for item in message:
    mydict.setdefault(item, 0)
    mydict[item] = mydict[item] + 1
'''print("Char how many times:",mydict1['a'])
print("Char how many times:",mydict1['u'])
print("Char how many times:",mydict1['i'])
print("Char how many times:",mydict1['o'])
print("Char how many times:",mydict1['e'])
sum= mydict1['a']+mydict1['i']+mydict1['u']+mydict1['o']+mydict1['e']
print(sum)'''
print(mydict)
print(mydict['s'])
print(mydict['a'])









