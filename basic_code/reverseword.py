
#Write a Python program that accepts a word from the user and reverse it.
word = input("Input a word to reverse: ")
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
