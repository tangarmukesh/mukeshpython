x = input("Enter a sentence: ").upper()
y= x.count(" ")
#print(y)
a=x.split(" ")
num = 0;
#loop through every char
for i in range(y+1):
   b=a[i]
   #print(b)
   #print(len(b))
#for every char, loop through vowels
   for v in range(len(b)):
    #if char matches vowels, increase num
      if b[v] == 'A' or b[v] == 'E' or  b[v] == 'I' or b[v] == 'O' or  b[v] == 'U':
        num+= 1
   print("Total vowel in string: ",b,num)
   num=0;


