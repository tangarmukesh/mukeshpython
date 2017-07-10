
#Write a Python program that accepts a word from the user and reverse it.
'''word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


#or
word = input("Input a word to reverse it: ")
print(len(word))
print (word[-1::-1])

#or
a=str(input("Enter a string: "))
print(len(a))
print("Reverse of the string is: ",a[::-1])

#or
#reverse a string words
sentence = input("Enter your string: ")
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print (sentence_rev)

#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
lines = []
while True:
    l = input("Enter your line: ")
    if l:
        lines.append(l.lower())
    else:
        break;

for l in lines:
    print(l,end=" ")'''

#Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'python', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print("Type of ",item, " is ", type(item))
