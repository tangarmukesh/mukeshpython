import re
string = input("Enter your string: ").lower()
#s= string.replace(" ", "").replace(",","").replace("?","")
#print(s)
s = re.sub(r'[^a-z0-9=]', '',string)
print((s))
def is_palindrome(s):
    for i,char in enumerate(s):
        if char != s[-i-1]:
            return False
    return True
print(is_palindrome(s))
