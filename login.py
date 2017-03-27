userdetails = {'mukesh':'1234', 'dev':'4321'}
username = input("Enter your username: ")
password = input("Enter your password: ")
if password and username in userdetails:
    print("Welcome")
else:
    print("Not Match")