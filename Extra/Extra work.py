x = input("Enter a sentence: ").upper()
#y= x.count(" ")
#print(y)
a=x.split(" ")
num = []
count=0
#loop through every char
for i in a:
   #for every char, loop through vowels
   for v in i:
    #if char matches vowels, increase num
      if v == 'A' or v == 'E' or  v == 'I' or v == 'O' or  v == 'U':
        count+= 1
   num.append(count)
   count=0

print(num)