string = input("Enter your string: ").lower()
string = string.strip()
def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True
print(is_palindrome(string))