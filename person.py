class Person:
    def __init__(self,namearg):
        self.name = namearg

    def speak(self,msg ="calling the base class"):
        print(self.name,msg)

class Man(Person):
    def speak(self,msg= "Calling the Man child class"):
        print(self.name,msg)

class Woman(Person):
    def speak(self,msg = "Caliing the Woman child class"):
        print(self.name,msg)
