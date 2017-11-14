class Bird:
    '''A base class of bird'''
    count = 0

    def __init__(self,chat):
        self.sound = chat
        Bird.count +=1

    def talk(self):
        return self.sound

